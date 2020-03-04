# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import os

path = 'brain/1/'
files = []
for filename in os.listdir(path):
    if os.path.isfile(os.path.join(path,filename)):
        if (".csv" in filename) is True:
            files.append(filename)
#print("使用するbrainファイルは次の通りです"+str(files))
for i,file in enumerate(files):
    #print(str(file)+"を削除します")
    os.remove(path+file)

path = 'brain/2/'
files = []
for filename in os.listdir(path):
    if os.path.isfile(os.path.join(path,filename)):
        if (".csv" in filename) is True:
            files.append(filename)
#print("使用するbrainファイルは次の通りです"+str(files))
for i,file in enumerate(files):
    #print(str(file)+"を削除します")
    os.remove(path+file)

path = 'log'
files = []
for filename in os.listdir(path):
    if os.path.isfile(os.path.join(path,filename)):
        if (".csv" in filename) is True:
            files.append(filename)
#print("使用するbrainファイルは次の通りです"+str(files))
for i,file in enumerate(files):
    #print(str(file)+"を削除します")
    os.remove(path+file)
