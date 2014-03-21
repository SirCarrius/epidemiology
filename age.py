import nltk, os, json, csv, string, cPickle
from scipy.stats import scoreatpercentile

from pprint import pprint
from progress.bar import Bar
READ = 'rb'
WRITE = 'wb'
stopwords = set(open('stopwords',READ).read().splitlines())
exclude = set(string.punctuation)

#lemmatizer
lmtzr = nltk.stem.wordnet.WordNetLemmatizer()
base = '/Volumes/My Book/carrie-controls/'
#get the names of the files in a list
json_list = [os.path.join(base,datafile) 
			 for datafile in 
			 filter(lambda string: string.endswith('json'),os.listdir(base))]

def sanitize(wordList):
	#Lemmatize
	answer = [lmtzr.lemmatize(word.lower()) for word in list(set(wordList)-exclude)]
	
	#Remove stopwords
	answer = list(set(answer)-stopwords)

	#Remove non-english words
	answer = [word for word in answer if all([ord(letter)<128 for letter in word])]

	#Remove links
	answer = [word for word in answer if 'http://' not in word]
	return answer

words = []
bar = Bar('Converting JSON files to proper text',max=len(json_list))
for filename in json_list:
	words.extend([sanitize(' '.join([tweet['text'] 
			for tweet in json.load(open(filename,READ))]).split())] )
	bar.next()
bar.finish()

words = [item for sublist in words for item in sublist]
freq = nltk.FreqDist(words)
cutoff = scoreatpercentile(freq.values(),15)
vocab = [word for word,f in freq.items() if f > cutoff] 
cPickle.dump({'distribution':freq,'cutoff':cutoff},open('freqdist.pkl',WRITE))
#pprint(vocab)