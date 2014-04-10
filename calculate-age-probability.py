import nltk, json, cPickle, itertools

import numpy as np

from nltk.tokenize import word_tokenize
from pprint import pprint

t_given_a = json.load(open('conditional_probability.json','rb'))
a_unconditional = json.load(open('age.json','rb'))

t_unconditional = json.load(open('t_unconditional.json','rb'))['distribution'] #t_unconditional is a list of tuples
#print t_unconditional
key, value = zip(*t_unconditional)
#print value
denominator = sum(value)
print denominator
test_sentence = "i in the library"
tokens = word_tokenize(test_sentence)

ngram = 3
p = {age:np.nan for age in t_given_a} #initial value of probability; {age, probability}; p is a dictionary
#np.nan: constant; not a number; undefined number

for n in range(1,ngram+1):
	for token in itertools.combinations(tokens,n): #combo from 1 word to 4l itertools.combo creates a list. token is an element of the list
	#for bigram, token is a list of two words - nested list
		token = ' '.join(token)#look it up in string
		print token
		print 1
		for age in t_given_a:
			print 2
			if token in t_given_a[age]: #shorter data -> more efficient
				#Is all of token in the string?
				print 3
				if token in t_unconditional:
					p[age]= t_given_a[age][token]*float(a_unconditional[age])/(denominator*t_unconditional[token])
					print 4
				if n>1 and all([word in t_unconditional for word in token.split()]):
					print 5
					for word in token.split():
						print 6
						print word in t_unconditional, word,'kkk'
						probs = [t_unconditional[word] for word in token.split()] #probs is a list because it has the 2 brackets on the right side
					#this gives us a list of all the t_unconditional value for each word in the token, which is a list after we did token.split()
						t_unconditional[token] = reduce(lambda x,y: x*y, probs) #lambda function: anoynomous functino; function without a name;
					#multiply (x*y) each successive element in the list (probs)
						p[age]= t_given_a[age][token]*float(a_unconditional[age])/(denominator*t_unconditional[token])
					#print token


pprint(p)
#Doesn't account for bigrams
#Need larger sample of unconditional token distribution