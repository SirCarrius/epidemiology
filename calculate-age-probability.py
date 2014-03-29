import nltk, json, cPickle

import numpy as np

from nltk.tokenize import word_tokenize

t_given_a = json.load(open('conditional_probability.json','rb'))
a_unconditional = json.load(open('age.json','rb'))

t_unconditional = cPickle.load(open('freqdist.pkl','rb'))['distribution']
denominator = sum(t_unconditional.values())
test_sentence = "i like frogs nubs hit bob"
tokens = word_tokenize(test_sentence)

p = {}
for token in tokens:
	if all([token in [t_given_a,t_unconditional]]):
		for age in a_unconditional:
			p [age]= t_given_a[age][token]*float(a_unconditional[age])/(denominator*t_unconditional[word])

#Doesn't account for bigrams
#Need larger sample of unconditional token distribution