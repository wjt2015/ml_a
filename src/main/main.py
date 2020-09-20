
"""
机器学习;

dataset:
/Users/jintao9/linux2014/test
"""

import numpy
import pymysql
import sys
import os
import gensim_core.core_func

import pandas as pd
from gensim import corpora

data_file="Users/jintao9/linux2014/test/Dodgers.data"

texts = [['human', 'interface', 'computer'],
         ['survey', 'user', 'computer', 'system', 'response', 'time'],
         ['eps', 'user', 'interface', 'system'],
         ['system', 'human', 'system', 'eps'],
         ['user', 'response', 'time'],
         ['trees'],
         ['graph', 'trees'],
         ['graph', 'minors', 'trees'],
         ['graph', 'minors', 'survey']]


def read_data():
    data=pd.read_csv(data_file,None)
    print(data)

def word2vec():

    corpus=corpora.Dictionary(texts)

    print(corpus)

if __name__=="__main__":
    print("a={0};b={1}".format(1,"ABCD"));

    gensim_core.core_func.word_statistic(texts)

    word2vec()



