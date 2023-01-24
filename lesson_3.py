#! /usr/bin/env python
# -*- coding: utf-8 -*-
import string
import sys, codecs
file = codecs.open('text.txt', encoding = 'utf-8')
with file as f:
    s = f.read()

# 1
for p in string.punctuation:
    if p in s:
        s = s.replace(p, '')
        s.strip()

# 2, 3
lst = s.split()
lst = repr(lst).decode("unicode_escape")
lst = lst.lower()
#print(s)
#for i in lst:
#lst = list(map(lambda x:x.lower(), lst))
#print(lst)
wordfreg = {}

# 4
for word in lst.replace(',', ' ').split():
    wordfreg[word] = wordfreg.setdefault(word, 0) + 1
    if word not in wordfreg:
        wordfreg[word] = 0
    wordfreg[word] += 1

# 5
print(sorted(wordfreg.values(), reverse=True)[0:5])
print(len(set(wordfreg)))
#list= []
#for i in range(wordfreg)


file.close
