import nltk, os, json, csv, string, cPickle, sys, unicodedata

t_given_a = json.load(open('conditional_probability.json','rb'))
stopwords = open('stopwords','rb').read().splitlines()

'''
find('a1318')

def find(age):
	list = t_given_a(age).keys()
	for item in list:
		if item not in stopwords:
			print item
'''

#list of words and numbers
list = [t_given_a['a1922'].keys()]

#print stopwords

for stop in stopwords:
	for word in list:
		if stop == word:
			print word

'''
for n in len(list)
	if n%2 == 0
		list.pop(n)
'''