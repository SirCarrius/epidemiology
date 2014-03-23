import nltk, json, cPickle

import numpy as np

from nltk.tokenize import word_tokenize

t_given_a = json.load(open('conditional_probability.json','rb'))
a_unconditional = json.load(open('age.json','rb'))

t_unconditional = cPickle.load(open('freqdist.pkl','rb'))['distribution']

test_sentence = "i like frogs"
tokens = word_tokenize(test_sentence)

for token in tokens:
	if all([token in [t_given_a,a_unconditional,t_unconditional]]):
		pass
