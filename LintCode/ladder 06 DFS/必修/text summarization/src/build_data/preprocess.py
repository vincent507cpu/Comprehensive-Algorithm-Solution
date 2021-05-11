import pandas as pd

from src.build_data.utils import sentences_proc
from src.utils import config
from src.utils.multi_proc_utils import parallelize


def preprocess(train_data_path, test_data_path):
    # 1.加载数据
    train_df = pd.read_csv(train_data_path)
    test_df = pd.read_csv(test_data_path)
    print('train data size {},test data size {}'.format(len(train_df), len(test_df)))
    # 2. 空值剔除
    train_df.dropna(subset=['Report'], inplace=True)
    # test_df.dropna(subset=['Report'], inplace=True)
    train_df.fillna('', inplace=True)
    test_df.fillna('', inplace=True)
    # 3.多线程, 批量数据处理
    train_df = parallelize(train_df, sentences_proc)
    test_df = parallelize(test_df, sentences_proc)
    # 4. 合并训练测试集合
    train_df['merged'] = train_df[['Question', 'Dialogue', 'Report']].apply(lambda x: ' '.join(x), axis=1)
    # test_df['merged'] = test_df[['Question', 'Dialogue', 'Report']].apply(lambda x: ' '.join(x), axis=1)
    test_df['merged'] = test_df[['Question', 'Dialogue']].apply(lambda x: ' '.join(x), axis=1)
    merged_df = pd.concat([train_df[['merged']], test_df[['merged']]], axis=0)
    print('train data size {},test data size {},merged_df data size {}'.format(len(train_df),
                                                                               len(test_df),
                                                                               len(merged_df)))
    # 5.保存处理好的 训练 测试集合
    train_df = train_df.drop(['merged'], axis=1)
    test_df = test_df.drop(['merged'], axis=1)
    train_df.to_csv(config.train_seg_path, index=False, header=False)
    test_df.to_csv(config.test_seg_path, index=False, header=False)
    # 6. 保存合并数据
    merged_df.to_csv(config.merger_seg_path, index=False, header=False)
    return test_df, train_df