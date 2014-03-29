import nltk, json, cPickle, itertools

import numpy as np

from nltk.tokenize import word_tokenize
from pprint import pprint

t_given_a = json.load(open('conditional_probability.json','rb'))
a_unconditional = json.load(open('age.json','rb'))

t_unconditional = cPickle.load(open('freqdist.pkl','rb'))['distribution']
denominator = sum(t_unconditional.values())
test_sentence = "i in the library"
tokens = word_tokenize(test_sentence)

ngram = 3
p = {age:np.nan for age in t_given_a}

for n in range(1,ngram+1):
	for token in itertools.combinations(tokens,n):
		token = ' '.join(token)
		for age in t_given_a:
			if token in t_given_a[age]:
				#Is all of token in the string?
				if token in t_unconditional:
					p[age]= t_given_a[age][token]*float(a_unconditional[age])/(denominator*t_unconditional[token])
				if n>1:
					for word in token.split():
						print word in t_unconditional, word,'kkk'
				elif n>1 and all([word in t_unconditional for word in token.split()]):
					print token

pprint(p)
#Doesn't account for bigrams
#Need larger sample of unconditional token distribution