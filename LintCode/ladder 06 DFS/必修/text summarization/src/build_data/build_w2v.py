from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

from src.utils import config
from src.utils.multi_proc_utils import cores


def build_w2v():
    # 7. 训练词向量
    print('start build w2v model')
    wv_model = Word2Vec(LineSentence(config.merger_seg_path),
                        size=config.embedding_dim,
                        sg=1,
                        workers=cores,
                        iter=config.wv_train_epochs,
                        window=5,
                        min_count=5)
    return wv_model