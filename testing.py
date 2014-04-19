# -*- coding: utf-8 -*-

import nltk, os, json, csv, string, cPickle
from scipy.stats import scoreatpercentile

#print string.punctuation
# ! " # $ & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ {| } ~

exclude = set(string.punctuation)

lmtzr = nltk.stem.wordnet.WordNetLemmatizer()
#true positive - dictionary with key: 1
#true negative - empty dictionary
#false positive - dictionary with key: 1
#false negative: empty dictionary


#testing case 1: yes
#testing case 2: #the
wordList= ['\'the', 'the', '"the']
print wordList
wordList2 = [word.translate(None, string.punctuation) for word in wordList]
#wordList2 = [filter(lambda char: char in exclude,word) for word in wordList]
print wordList2
#answer = [lmtzr.lemmatize(word.lower()) for word in wordList word.translate(None, string.punctuation)]
answer = [lmtzr.lemmatize(word.lower()) for word in wordList2]
print answer

#word = ''.join(wordList)
#print word
freq = nltk.FreqDist(wordList2)
print freq


