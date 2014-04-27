
import nltk, json, cPickle, itertools

p = cPickle.load(open('freqdist_2.pkl'))
pickled = jsonpickle.encode(p)
print p