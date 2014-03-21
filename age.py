import nltk, os, json, csv
from scipy.stats import scoreatpercentile

#read the stopwrod file
#do stopwords have to be in the same file as the json files?
READ = 'rb'
stopwords = open('../data/stopwords',READ).readlines()

#lemmatizer
lmtzr = WordNetLemmatizer()

#get the names of the files in a list
json_list = os.listir('C:\Users\Carrie0731\Desktop\JSON FILES')#probably should modify this so everyone can open it on his/her computer

sanitize = lambda text: lmtzer.lemmatize(text) if text not in stopwords else ''
string = ' ' .join(map(sanitize,[tweet['text'] for tweet in json.load(open(filename,READ)) for filename in json_list]))

	
freq = FreqDist(string)
cutoff = scoreatpercentile(freq.values(),15)
vocab = [word for word,f in freq.items() if f > cutoff] #Items returns the tuple (key,value), in this case (word, frequency)