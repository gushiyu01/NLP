#!/usr/bin/Python
# -*- coding: utf-8 -*-
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS

# 当前文件路径 pwd
d = path.dirname(__file__)
print(d)
# Read the whole text.
file = open('alice.txt', 'r', encoding='UTF-8').read()
# 进行分词
# 刚开始是分完词放进txt再打开却总是显示不出中文很奇怪
default_mode = jieba.cut(file)
print("111", default_mode)
text = " ".join(default_mode)
print(text)
alice_mask = np.array(Image.open(path.join(d, "1.png")))
stopwords = set(STOPWORDS)
stopwords.add("这个")
wc = WordCloud(
    font_path='C:\Windows\Fonts\STZHONGS.TTF',
    # 设置字体，不指定就会出现乱码,这个字体文件需要下载
    # background_color="white",
    max_words=200,
    mask=alice_mask,
    stopwords=stopwords)
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "qq_result.jpg"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
# plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
# plt.imshow(wc)
plt.axis("off")
plt.show()
