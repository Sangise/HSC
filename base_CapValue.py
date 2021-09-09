#!/usr/bin/env python
# coding: utf-8

# In[6]:


#要numpy
import numpy as np

def hyprawread(name,hor,ver,SpectDim, en_percent):
    with open(name,'rb') as f:
        img = np.fromfile(f,np.uint16,-1)
    img = np.reshape(img,(ver,SpectDim,hor))
    img = np.transpose(img, (0,2,1))
    if en_percent == True:
        img = img / 40 #パーセンテージ表記に変換
    else:
        pass
    return img

#読み込みたいファイル名を指定
FILENAME = 'C:/Users/FRNLC310Y-11/tomita/demo.nir'

#横400,縦320,バンド数81を引数に指定
result = hyprawread(FILENAME,400,320,81,False) #パーセント表記ならTrueに。

print(result)


# In[ ]:




