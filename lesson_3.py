#! /usr/bin/env python
# -*- coding: utf-8 -*-
import string
import sys, codecs
file = codecs.open('text.txt', encoding = 'utf-8')
with file as f:
    s = f.read()

import re

#wordfreq = {}
#with file as f:
#    for line in f:
#        for word in re.findall(r'[\w]+', line.lower()):
#            wordfreq[word] = wordfreq.setdefault(word, 0) + 1

#print wordfreq

for p in string.punctuation:
    if p in s:
        s = s.replace(p, '')
        s.strip()

lst = s.split()
lst = repr(lst).decode("unicode_escape")
lst = lst.lower()
wordfreg = {}
#repr(word).decode("unicode_escape")
for word in lst.replace(',', ' ').split():
    wordfreg[word] = wordfreg.setdefault(word, 0) + 1
    #if word not in d:
    #    d[word] = 0
    #d[word] += 1

print(wordfreg)

#for i in range(5):
#    word, wordfreg = items[i]
#    print ("{0:<10}{1:>5}".format(word, count))
#for raw_word in words:
#    word = raw_word.strip(unwanted_chars)
#    if word not in wordfreq:
#        wordfreq[word] = 0
#    wordfreq[word] += 1

file.close
