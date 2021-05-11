# -*- coding:utf-8 -*-
# Created by Wenjia Zhai on 05/04/2021 inspired by LuoJie's script
# https://bastings.github.io/annotated_encoder_decoder/

import sys
sys.path.append('/Users/wenjiazhai/Documents/GitHub/nlp_projects/text summarization')

# from src.utils.gpu_utils import config_gpu
from src.utils.params_utils import get_params
from src.utils.wv_loader import Vocab, load_embedding_matrix
# import tensorflow as tf
from torch import nn
import torch
from torch.nn import functional as F

class Encoder(nn.Module):
    # def __init__(self, embedding_matrix, batch_size, seq_len, hidden_dim, dropout = 0.):
    def __init__(self, embedding_matrix, batch_size, hidden_dim, dropout = 0.):
        super().__init__()
        self.batch_size = batch_size
        # self.seq_len = seq_len
        self.hidden_dim = hidden_dim
        _, self.embed_dim = embedding_matrix.size()                     # (vocab_size, embed_dim)
        self.embed = nn.Embedding.from_pretrained(embedding_matrix)     
        self.gru = nn.GRU(self.embed_dim, hidden_dim, batch_first=True, bidirectional=True, dropout=dropout)

    def forward(self, x, hidden):
        x = self.embed(x)                       # (batch_size, seq_len, embed_dim)
        output, hidden = self.gru(x, hidden)    # output: (batch_size, seq_len, hidden_dim * 2) hidden: (2 * 1, batch_size, hidden_dim)
        hidden = hidden.transpose(0, 1).reshape(self.batch_size, -1) # (batch_size, hidden_dim * 2)
        return output, hidden

    def init_hidden(self):
        return torch.zeros((2, self.batch_size, self.hidden_dim))

class BahdanauAttention(nn.Module):
    def __init__(self, hidden_dim):
        super().__init__()
        self.W1 = nn.Linear(hidden_dim * 2, hidden_dim)
        self.W2 = nn.Linear(hidden_dim * 2, hidden_dim)
        self.V = nn.Linear(hidden_dim, 1)

    def forward(self, query, values):
        # query为上次的GRU隐藏层
        # values为编码器的编码结果enc_output
        # 在seq2seq模型中，St是后面的query向量，而编码过程的隐藏状态hi是values。

        # hidden shape == (batch_size, hidden size)
        # hidden_with_time_axis shape == (batch_size, 1, hidden size)
        # we are doing this to perform addition to calculate the score
        hidden_with_time_axis = torch.unsqueeze(query, 1)
        # print(hidden_with_time_axis.size())

        # score shape == (batch_size, max_length, 1)
        # we get 1 at the last axis because we are applying score to self.V
        # the shape of the tensor before applying self.V is (batch_size, max_length, units)
        # 计算注意力权重值
        score = self.V(torch.tanh(
            self.W1(values) + self.W2(hidden_with_time_axis)
        ))

        # attention_weights sha== (batch_size, max_length, 1)
        attention_weights = F.softmax(score, dim=1)

        # 使用注意力权重*编码器输出作为返回值，将来会作为解码器的输入
        # context_vector shape after sum == (batch_size, hidden_size)
        context_vector = attention_weights * values
        context_vector = torch.sum(context_vector, dim=1)

        return context_vector, attention_weights
        # a, b = self.W1(values), self.W2(hidden_with_time_axis)
        # print(a.size(), b.size())

class Decoder(nn.Module):
    # def __init__(self, embedding_matrix, batch_size, seq_len, hidden_dim, dropout=0.):
    def __init__(self, embedding_matrix, batch_size, hidden_dim, dropout=0.):
        super().__init__()
        self.batch_size = batch_size
        # self.seq_len = seq_len
        self.hidden_dim = hidden_dim
        self.vocab_size, self.embed_dim = embedding_matrix.size()
        self.embed = nn.Embedding.from_pretrained(embedding_matrix)
        self.gru = nn.GRU(self.embed_dim, hidden_dim, batch_first=True, bidirectional=True, dropout=dropout)
        self.fc = nn.Linear(hidden_dim * 2, self.vocab_size)

        # used for attention
        self.attention = BahdanauAttention(hidden_dim)

    def forward(self, x, hidden, enc_output):
        # 使用上次的隐藏层（第一次使用编码器隐藏层）、编码器输出计算注意力权重
        # enc_output shape == (batch_size, seq_len, hidden_size * 2)
        context_vector, attention_weights = self.attention(hidden, enc_output)
        # print('atten passed')
        # x shape after passing through embedding == (batch_size, 1, embedding_dim)
        x = self.embed(x)
        # print('embed passed', x.size())
        # 将上一循环的预测结果跟注意力权重值结合在一起作为本次的GRU网络输入
        # x shape after concatenation == (batch_size, 1, embedding_dim + hidden_size)
        x = torch.cat([torch.unsqueeze(context_vector, 1), x], dim=-1)
        proj = nn.Linear(x.size(-1), self.embed_dim)
        x = proj(x)
        # print('concat passed', x.size())
        # passing the concatenated vector to the GRU
        output, state = self.gru(x, hidden.reshape(2, self.batch_size, -1))
        # print('gru passed', output.size())
        # output shape == (batch_size * 1, hidden_size)
        output = output.reshape(-1, output.size(2))
        # print('reshape passed', output.size())
        # output shape == (batch_size, vocab)
        prediction = self.fc(output)
        return prediction, state, attention_weights

if __name__ == '__main__':
    seq_len = 250
    batch_size = 64
    embedding_dim = 500
    hidden_dim = 1024

    sample_embed_matrix = torch.randn((256, 512))
    sample_input = torch.ones((batch_size, seq_len)).long()

    encoder = Encoder(embedding_matrix=sample_embed_matrix, batch_size=batch_size, hidden_dim=hidden_dim)
    sample_hidden = encoder.init_hidden()

    sample_encoder_output, sample_hidden = encoder(sample_input, sample_hidden)
    print('output size:', sample_encoder_output.size())
    print('hidden size:', sample_hidden.size())

    attention = BahdanauAttention(hidden_dim=hidden_dim)
    # attention(sample_hidden, sample_encoder_output)
    context_vector, attention_weights = attention(sample_hidden, sample_encoder_output)
    print('context vector size:', context_vector.size())
    print('attention weight size:', attention_weights.size())

    decoder = Decoder(embedding_matrix=sample_embed_matrix, batch_size=batch_size, hidden_dim=hidden_dim)
    prediction, state, attention_weights = decoder(torch.randint(sample_embed_matrix.size(0), (batch_size, 1)), sample_hidden, sample_encoder_output)
    print('prediction size:', prediction.size())
    # print('state size:', state.size())
    # print('attention_weight size:', attention_weights.size())