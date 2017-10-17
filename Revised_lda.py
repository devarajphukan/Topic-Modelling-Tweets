import re, nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from gensim import corpora, models
import gensim

stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
	stemmed = []
	for item in tokens:
		stemmed.append(stemmer.stem(item))
	return stemmed

def tokenize(text):

	text = re.sub("[^a-zA-Z]", " ", text) # Removing numbers and punctuation
	text = re.sub(" +"," ", text) # Removing extra white space
	text = re.sub("\\b[a-zA-Z0-9]{10,100}\\b"," ",text) # Removing very long words above 10 characters
	text = re.sub("\\b[a-zA-Z0-9]{0,1}\\b"," ",text) # Removing single characters (e.g k, K)
	tokens = nltk.word_tokenize(text.strip())
	tokens = nltk.pos_tag(tokens)
	# Uncomment next line to use stemmer
	# tokens = stem_tokens(tokens, stemmer)
	return tokens

stopset = stopwords.words('english')
freq_words = ['http','https','amp','com','co','th']
for i in freq_words :
    stopset.append(i)

def analyze(fileObj,Uname) :

	text_corpus = []
	for doc in fileObj :
		temp_doc = tokenize(doc.strip())
		current_doc = []
		for word in range(len(temp_doc)) :
			if temp_doc[word][0] not in stopset and temp_doc[word][1] == 'NN':
				current_doc.append(temp_doc[word][0])

		text_corpus.append(current_doc)


	dictionary = corpora.Dictionary(text_corpus)
	corpus = [dictionary.doc2bow(text) for text in text_corpus]
	ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary,passes=100)
	print 'Topics for ',Uname,'\n'
	for topics in ldamodel.print_topics(num_topics=3, num_words=7) :
		print topics,"\n"

narendraModi = open('narendramodi.txt')
analyze(narendraModi,'Narendra Modi')

andrewYNg = open('AndrewYNg.txt')
analyze(andrewYNg,'Andrew Y Ng')

donaldTrump = open('realDonaldTrump.txt')
analyze(donaldTrump,'Donald Trump')
