from __future__ import print_function
import numpy as np
import re
import itertools
import codecs
from collections import Counter
import jieba
import nltk
from nltk import word_tokenize

PAD = "<PAD>"
EOS = "<EOS>"
UNK = "<UNK>"
GO = "<GO>"


def build_vocab(sentences, vocab_size=80):
    """
    Builds a vocabulary mapping from word to index based on the sentences.
    Returns vocabulary mapping and inverse vocabulary mapping.
    """
    # Build vocabulary
    word_counts = Counter(itertools.chain(*sentences))
    # Mapping from index to word
    vocabulary_inv = [PAD] + [EOS] + [GO] + [UNK] + [x[0] for x in word_counts.most_common(vocab_size-4)]
    # Mapping from word to index
    vocabulary = {x: i for i, x in enumerate(vocabulary_inv)}
    return [vocabulary, vocabulary_inv]



def load_data():
    texts = []

    with codecs.open("train_.txt", "r", "utf-8") as f:
        for line in f:
            texts.append(list(line.strip()))
    return texts
a = load_data()
vocabulary, vocabulary_inv = build_vocab(a)
with open('vocab.json', 'w') as f:
    st = str(vocabulary).replace("'", '"')
    f.write(st)