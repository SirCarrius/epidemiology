import nltk, os, json, csv, string, cPickle, sys, unicodedata
from scipy.stats import scoreatpercentile

from pprint import pprint

print (sys.version)
#from progress.bar import Bar
READ = 'rb'
WRITE = 'wb'
stopwords = set(open('stopwords',READ).read().splitlines())
exclude = set(string.punctuation)

tbl = dict.fromkeys(i for i in xrange(sys.maxunicode)
                      if unicodedata.category(unichr(i)).startswith('P'))

#lemmatizer
lmtzr = nltk.stem.wordnet.WordNetLemmatizer()
base = 'C:\Users\Carrie0731\Desktop\JSON FILES\json'
#get the names of the files in a list
json_list = [os.path.join(base,datafile)
			 for datafile in 
			 filter(lambda string: string.endswith('json'),os.listdir(base))]
			 
#wordList: each tweet
def sanitize(wordList): 
	#Lemmatize
	#remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    #word_list = [s.translate(remove_punctuation_map) for s in value_list]
	#for word in wordList:
	#	for item in word:
	#		answer = [item.translate(exclude)]
	#answer = [word.translate(None, exclude) for word in wordList] #testing membership is faster in set
	#answer = [word.translate(remove_punctuation_map) for word in wordList]
	
	answer = [word.translate(tbl) for word in wordList]
	
	#Remove stopwords
	answer = list(set(answer)-stopwords)

	#Remove everything that's not spacing, numbers, punctuations, and roman characters (includes pin yin)
	answer = [word for word in answer if all([ord(letter)<128 for letter in word])]

	#Remove links
	answer = [word for word in answer if 'http://' not in word]
	answer = [lmtzr.lemmatize(word.lower()) for word in answer]
	return answer

	
words = []
#bar = Bar('Converting JSON files to proper text',max=len(json_list))

for filename in json_list:
	words.extend([sanitize(nltk.word_tokenize(' '.join([tweet['text'] 
                       for tweet in json.load(open(filename,READ))])))])

'''

for filename in json_list:
	print filename
	for tweet in json.load(open(filename,READ)):
		print sanitize(nltk.word_tokenize(' '.join([tweet['text']])))
		
'''		
#bar.next()
#bar.finish()


#line graph: freq.plot(10) -> 10 most common words
#test if Mike's code works
#open cPickle file
words = [item for sublist in words for item in sublist]
freq = nltk.FreqDist(words)
cutoff = scoreatpercentile(freq.values(),15)
print cutoff
vocab = [word for word,f in freq.items() if f > cutoff] 
#make it freqdist_2 -> different file
cPickle.dump({'distribution':freq,'cutoff':cutoff},open('freqdist_2.pkl',WRITE))
#pprint(vocab)