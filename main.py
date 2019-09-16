#!/usr/bin/env python
# encoding: utf-8
'''
@author: 10858
@license: (C) Copyright
@contact: xxx@qq.com
@software: PyCharm
@file: main.py
@time: 2019-04-10 17:46
@desc:
'''


from music21 import *
from ACCO_PARSER.ACC_PARSER_SongWeight import SongParser_weight
from ACCO_PARSER.ACCO_PARSER_Song import SongParser
from ACCO_GLOBALDATA.ACCO_GLOBALDATA_CNotes import CNotes
from ACCO_GLOBALDATA.ACCO_GLOBALDATA_Chord import CChord
from ACCO_MODEL.ACCO_MODEL_SVMModel import SVCModel
from ACCO_MODEL.ACCO_MODEL_DescionTree import DecisionTreeModel
from ACCO_MODEL.ACCO_MODEL_RandomForestModel import randomForstModel
from pandas.api.types import CategoricalDtype
from ACCO_MODEL.ACCO_MODEL_MLPClassifierModel import MLPModel
from sklearn import linear_model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


training_root = './ACCO_DATASET/training'
X = np.empty(shape=[0, 7])
y = np.empty(shape=[0, 1])
parser = SongParser()
filelist = os.listdir(training_root)
for file in filelist:
        #print(file)
        melody, acco = parser.parser_midi_training(os.path.join(training_root, file))
        acco = parser.remove_header(acco)
        X_one, y_one = parser.parseSong(melody, acco)
        X, y = parser.training_join(X, X_one, y, y_one)

model = randomForstModel()

df = pd.DataFrame(X)
df.columns = ['head', 'tail', 'chord_inside', 'beat', 'longest', 'fre', 'first']
for col in df.columns:
        df[col] = df[col].astype(int)
        df[col] = df[col].astype(str)

train_x = pd.get_dummies(df)
X = train_x.values

loss = model.train(X, y)
print(loss)