# -*- coding:utf-8 -*-
# Created by LuoJie at 11/23/19

from src.utils.gpu_utils import config_gpu
from src.utils.params_utils import get_params
from src.utils.wv_loader import Vocab, load_embedding_matrix
import tensorflow as tf


class Encoder(tf.keras.Model):
    def __init__(self, embedding_matrix, enc_units, batch_sz):
        super(Encoder, self).__init__()
        self.batch_sz = batch_sz
        self.enc_units = enc_units
        vocab_size, embedding_dim = embedding_matrix.shape
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim, weights=[embedding_matrix],
                                                   trainable=False)
        self.gru = tf.keras.layers.GRU(self.enc_units,
                                       return_sequences=True,
                                       return_state=True,
                                       recurrent_initializer='glorot_uniform')

    def call(self, x, hidden):
        x = self.embedding(x)
        output, state = self.gru(x, initial_state=hidden)
        return output, state

    def initialize_hidden_state(self):
        return tf.zeros((self.batch_sz, self.enc_units))


class BahdanauAttention(tf.keras.Model):
    def __init__(self, units):
        super(BahdanauAttention, self).__init__()
        self.W1 = tf.keras.layers.Dense(units)
        self.W2 = tf.keras.layers.Dense(units)
        self.V = tf.keras.layers.Dense(1)

    def call(self, query, values):
        # query为上次的GRU隐藏层
        # values为编码器的编码结果enc_output
        # 在seq2seq模型中，St是后面的query向量，而编码过程的隐藏状态hi是values。

        # hidden shape == (batch_size, hidden size)
        # hidden_with_time_axis shape == (batch_size, 1, hidden size)
        # we are doing this to perform addition to calculate the score
        hidden_with_time_axis = tf.expand_dims(query, 1)

        # score shape == (batch_size, max_length, 1)
        # we get 1 at the last axis because we are applying score to self.V
        # the shape of the tensor before applying self.V is (batch_size, max_length, units)
        # 计算注意力权重值
        score = self.V(tf.nn.tanh(
            self.W1(values) + self.W2(hidden_with_time_axis)))

        # attention_weights sha== (batch_size, max_length, 1)
        attention_weights = tf.nn.softmax(score, axis=1)

        # # 使用注意力权重*编码器输出作为返回值，将来会作为解码器的输入
        # context_vector shape after sum == (batch_size, hidden_size)
        context_vector = attention_weights * values
        context_vector = tf.reduce_sum(context_vector, axis=1)

        return context_vector, attention_weights


class Decoder(tf.keras.Model):
    def __init__(self, embedding_matrix, dec_units, batch_sz):
        super(Decoder, self).__init__()
        self.batch_sz = batch_sz
        self.dec_units = dec_units
        vocab_size, embedding_dim = embedding_matrix.shape
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim, weights=[embedding_matrix],
                                                   trainable=False)
        self.gru = tf.keras.layers.GRU(self.dec_units,
                                       return_sequences=True,
                                       return_state=True,
                                       recurrent_initializer='glorot_uniform')
        self.fc = tf.keras.layers.Dense(vocab_size)

        # used for attention
        self.attention = BahdanauAttention(self.dec_units)

    def call(self, x, hidden, enc_output):
        # 使用上次的隐藏层（第一次使用编码器隐藏层）、编码器输出计算注意力权重
        # enc_output shape == (batch_size, max_length, hidden_size)
        context_vector, attention_weights = self.attention(hidden, enc_output)

        # x shape after passing through embedding == (batch_size, 1, embedding_dim)
        x = self.embedding(x)

        # 将上一循环的预测结果跟注意力权重值结合在一起作为本次的GRU网络输入
        # x shape after concatenation == (batch_size, 1, embedding_dim + hidden_size)
        x = tf.concat([tf.expand_dims(context_vector, 1), x], axis=-1)

        # passing the concatenated vector to the GRU
        output, state = self.gru(x, hidden)

        # output shape == (batch_size * 1, hidden_size)
        output = tf.reshape(output, (-1, output.shape[2]))

        # output shape == (batch_size, vocab)
        prediction = self.fc(output)
        return prediction, state, attention_weights


if __name__ == '__main__':
    # GPU资源配置
    config_gpu()
    # 获得参数
    params = get_params()
    # 读取vocab训练
    vocab = Vocab(params["vocab_path"], params["vocab_size"])
    # 计算vocab size
    vocab_size = vocab.count
    # 使用GenSim训练好的embedding matrix
    embedding_matrix = load_embedding_matrix()

    input_sequence_len = 250
    batch_size = 64
    embedding_dim = 500
    units = 1024

    # 编码器结构 embedding_matrix, enc_units, batch_sz
    encoder = Encoder(embedding_matrix, units, batch_size)
    # example_input
    example_input_batch = tf.ones(shape=(batch_size, input_sequence_len), dtype=tf.int32)
    # sample input
    sample_hidden = encoder.initialize_hidden_state()

    sample_output, sample_hidden = encoder(example_input_batch, sample_hidden)
    # 打印结果
    print('Encoder output shape: (batch size, sequence length, hidden_dim) {}'.format(sample_output.shape))
    print('Encoder Hidden state shape: (batch size, hidden_dim) {}'.format(sample_hidden.shape))

    attention_layer = BahdanauAttention(10)
    attention_result, attention_weights = attention_layer(sample_hidden, sample_output)

    print("Attention result shape: (batch size, units) {}".format(attention_result.shape))
    print("Attention weights shape: (batch_size, sequence_length, 1) {}".format(attention_weights.shape))

    decoder = Decoder(embedding_matrix, units, batch_size)
    sample_decoder_output, state, attention_weights = decoder(tf.random.uniform((64, 1)),
                                                              sample_hidden, sample_output)

    print('Decoder output shape: (batch_size, vocab size) {}'.format(sample_decoder_output.shape))
