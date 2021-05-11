# -*- coding:utf-8 -*-
import tensorflow as tf

# from src.pgn_tf2.batcher import batcher
from src.seq2seq_tf2.seq2seq_batcher import train_batch_generator
import time
from functools import partial


def train_model(model, vocab, params, checkpoint_manager):
    epochs = params['epochs']

    pad_index = vocab.word2id[vocab.PAD_TOKEN]

    # 获取vocab大小
    params['vocab_size'] = vocab.count

    optimizer = tf.keras.optimizers.Adam(name='Adam', learning_rate=0.01)

    # 训练
    # @tf.function(input_signature=(tf.TensorSpec(shape=[params["batch_size"], None], dtype=tf.int32),
    #                               tf.TensorSpec(shape=[params["batch_size"], params["max_dec_len"]], dtype=tf.int32),
    #                               tf.TensorSpec(shape=[params["batch_size"], params["max_dec_len"]], dtype=tf.int32)))

    train_dataset, val_dataset, train_steps_per_epoch, val_steps_per_epoch = train_batch_generator(
        params['batch_size'], params['max_enc_len'], params['max_dec_len']
    )

    for epoch in range(epochs):
        start = time.time()
        enc_hidden = model.encoder.initialize_hidden_state()

        total_loss = 0.
        running_loss = 0.
        for (batch, (inputs, target)) in enumerate(train_dataset.take(train_steps_per_epoch), start=1):

            batch_loss = train_step(model, inputs, target, enc_hidden,
                                    loss_function=partial(loss_function, pad_index=pad_index),
                                    optimizer=optimizer)
            total_loss += batch_loss

            if batch % 50 == 0:
                print('Epoch {} Batch {} Loss {:.4f}'.format(epoch + 1,
                                                             batch,
                                                             (total_loss - running_loss) / 50))
                running_loss = total_loss
        # saving (checkpoint) the model every 2 epochs
        if (epoch + 1) % 2 == 0:
            ckpt_save_path = checkpoint_manager.save()
            print('Saving checkpoint for epoch {} at {}'.format(epoch + 1,
                                                                ckpt_save_path))

        valid_loss = evaluate(model, val_dataset, val_steps_per_epoch, pad_index)

        print('Epoch {} Loss {:.4f}; val Loss {:.4f}'.format(
            epoch + 1, total_loss / train_steps_per_epoch, valid_loss)
        )

        print('Time taken for 1 epoch {} sec\n'.format(time.time() - start))


# 定义损失函数
def loss_function(real, pred, pad_index):
    loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True, reduction='none')
    mask = tf.math.logical_not(tf.math.equal(real, pad_index))
    loss_ = loss_object(real, pred)
    mask = tf.cast(mask, dtype=loss_.dtype)
    loss_ *= mask
    return tf.reduce_mean(loss_)


def train_step(model, enc_inp, dec_target, enc_hidden, loss_function=None, optimizer=None, mode='train'):
    with tf.GradientTape() as tape:
        # enc_inp = enc_inp['enc_input']
        # dec_target = dec_target['dec_target']

        enc_output, enc_hidden = model.encoder(enc_inp, enc_hidden)
        # 第一个隐藏层输入
        dec_hidden = enc_hidden

        # 逐个预测序列
        predictions, _ = model.teacher_decoder(dec_hidden, enc_output, dec_target)

        batch_loss = loss_function(dec_target[:, 1:], predictions)

        if mode == 'train':
            variables = (model.encoder.trainable_variables + model.decoder.trainable_variables
                         + model.attention.trainable_variables)

            gradients = tape.gradient(batch_loss, variables)

            gradients, _ = tf.clip_by_global_norm(gradients, 5.0)

            optimizer.apply_gradients(zip(gradients, variables))

        return batch_loss


def evaluate(model, val_dataset, val_steps_per_epoch):
    print('Starting evaluate ...')
    total_loss = 0.
    enc_hidden = model.encoder.initialize_hidden_state()
    for (batch, (inputs, target)) in enumerate(val_dataset.take(val_steps_per_epoch), start=1):
        batch_loss = train_step(model, inputs, target, enc_hidden, mode='val')
        total_loss += batch_loss
    return total_loss / val_steps_per_epoch
