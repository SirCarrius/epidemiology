import nltk, os, json, csv, string, cPickle, sys
from scipy.stats import scoreatpercentile

#print string.punctuation
# ! " # $ & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ {| } ~
print (sys.version)
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
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
#wordList2 = [word.translate(remove_punctuation_map) for word in wordList]
wordList2 = [word.translate(None, string.punctuation) for word in wordList]
print wordList2
#answer = [lmtzr.lemmatize(word.lower()) for word in wordList word.translate(None, string.punctuation)]
answer = [lmtzr.lemmatize(word.lower()) for word in wordList2]
print answer


#word = ''.join(wordList)
#print word
freq = nltk.FreqDist(wordList2)
print freq


