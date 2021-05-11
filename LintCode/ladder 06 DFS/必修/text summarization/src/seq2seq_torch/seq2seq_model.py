# -*- coding:utf-8 -*-
# Created by Wenjia Zhai on 05/05/2021 inspired by LuoJie's script

import sys
sys.path.append('/Users/wenjiazhai/Documents/GitHub/nlp_projects/text summarization')
import torch
from torch import nn

from src.seq2seq_torch.model_layers import Encoder, BahdanauAttention, Decoder
from src.utils.gpu_utils import config_gpu
from src.utils.params_utils import get_params
from src.utils.wv_loader import load_embedding_matrix, Vocab

class Seq2Seq(nn.Module):
    def __init__(self, params, vocab):
        super().__init__()
        self.embed_matrix = load_embedding_matrix()
        self.params = params
        self.vocab = vocab
        self.batch_size = params['batch_size']
        self.hidden_dim = params['hidden_dim']

        self.encoder = Encoder(self.embed_matrix, self.batch_size, self.hidden_dim)
        self.attention = BahdanauAttention(self.hidden_dim)
        self.decoder = Decoder(self.embed_matrix, self.batch_size, self.hidden_dim)

    def teacher_encoder(self, dec_hidden, enc_output, dec_target):
        predictions = []

        dec_input = torch.unsqueeze([self.vocab.START_DECODING_INDEX] * self.batch_size, 1)

        #  Teacher forcing- feeding the target as the next input
        for t in range(1, dec_target.size(1)):
            # passing enc_output to the decoder
            pred, dec_hidden, _ = self.decoder(dec_input,
                                               dec_hidden,
                                               enc_output)

            dec_input = torch.unsqueeze(dec_target[:, t], 1)

            predictions.append(pred)

        return torch.stack(predictions, 1), dec_hidden

if __name__ == '__main__':
    # GPU资源配置
    # config_gpu()
    # 获得参数
    params = get_params()
    # 读取vocab训练
    vocab = Vocab(params['vocab_path'], params['vocab_size'])
    # 计算vocab size
    vocab_size = vocab.count

    input_seq_len = 200

    params = {'vocab_size':vocab_size,
              'embed_size':500,
              'hidden_dim':512,
              'batch_size':128,
              'input_sequence_len':input_seq_len}

    model = Seq2Seq(params=params, vocab=vocab)

    # example_input
    exp_input_batch = torch.ones((params['batch_size'], params['input_sequence_len'])).int()

    # sample input
    sample_hidden = model.encoder.initialize_hidden_state()

    # encoder layer
    sample_output, sample_hidden = model.encoder(exp_input_batch, sample_hidden)

    # print encoder output shape
    print(f'Encoder output shape: (batch size, sequence length, units) {sample_output.size()}')
    print(f'Encoder Hidden state shape: (batch size, units) {sample_hidden.size()}')

    # # attention layer
    # attn_layer = BahdanauAttention(params['hidden_dim'])
    # context_vector, attn_weights = attn_layer(sample_hidden, sample_output)

    # # print attention output shape
    # print(f'Attention context_vector shape: (batch size, units) {context_vector.size()}')
    # print(f'Attention weights shape: (batch_size, sequence_length, 1) {attn_weights.size()}')

    # # decoder layer
    # sample_decoder_output, _, _ = model.decoder(torch.randn((params['batch_size'], 1)),
    #                                             sample_hidden, sample_output)

    # # print decoder output shape
    # print(f'Decoder output shape: (batch_size, vocab size) {sample_decoder_output.size()}')