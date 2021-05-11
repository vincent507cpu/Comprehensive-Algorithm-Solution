# -*- coding:utf-8 -*-
# Created by Wenjia Zhai on 05/04/2021 inspired by LuoJie's script

import sys
sys.path.append('/Users/wenjiazhai/Documents/GitHub/nlp_projects/text summarization')

from src.utils.data_loader import load_dataset
from torch.utils.data import TensorDataset, DataLoader
import torch
from src.utils import config

def train_batch_generator(batch_size, max_enc_len=200, max_dec_len=50, sample_sum=None):
    # 加载数据集
    train_X, train_y = load_dataset(config.train_x_path, config.train_y_path,
                                    max_enc_len, max_dec_len)
    val_X, val_y = load_dataset(config.test_x_path, config.test_y_path,
                                max_enc_len, max_dec_len)
    print(f'total {len(train_Y)} examples ...')
    if sample_sum:
        train_X = train_X[:sample_sum]
        train_y = train_y[:sample_sum]
    # train_dataset = tf.data.Dataset.from_tensor_slices((train_X, train_Y)).shuffle(len(train_X),
    #                                                                                reshuffle_each_iteration=True)
    # val_dataset = tf.data.Dataset.from_tensor_slices((val_X, val_Y)).shuffle(len(val_X),
    #                                                                          reshuffle_each_iteration=True)
    # train_dataset = train_dataset.batch(batch_size, drop_remainder=True)
    # val_dataset = val_dataset.batch(batch_size, drop_remainder=True)
    train_dataset = TensorDataset((train_X, train_y))
    val_dataset = TensorDataset((val_X, val_y))
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, drop_last=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=True, drop_last=True)
    train_steps_per_epoch = len(train_X) // batch_size
    val_steps_per_epoch = len(val_X) // batch_size
    return train_loader, val_loader, train_steps_per_epoch, val_steps_per_epoch


def beam_test_batch_generator(beam_size, max_enc_len=200, max_dec_len=50):
    # 加载数据集
    test_X, test_y = load_dataset(config.test_x_path, config.test_y_path,
                                  max_enc_len, max_dec_len)
    for row in test_X:
        beam_search_data = torch.tensor([row for i in range(beam_size)])
        yield beam_search_data


if __name__ == '__main__':
    beam_test_batch_generator(4)