# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:34:34 2020

@author: 91973
"""

import nltk

paragraph =  """Looking back on a childhood filled with events and memories, 
I find it rather difficult to pick one that leaves me with the fabled "warm and fuzzy feelings.
" As the daughter of an Air Force major, I had the pleasure of traveling across America in many moving trips. 
I have visited the monstrous trees of the Sequoia National Forest, stood on the edge of the Grand Canyon and have jumped on the beds at Caesar's Palace in Lake Tahoe."
"The day I picked my dog up from the pound was one of the happiest days of both of our lives. I had gone to the pound just a week earlier with the idea that I would just "look" at a puppy. 
Of course, you can no more just look at those squiggling little faces so filled with hope and joy than you can stop the sun from setting in the evening.
I knew within minutes of walking in the door that I would get a puppy… but it wasn't until I saw him that I knew I had found my puppy."
"Looking for houses was supposed to be a fun and exciting process. 
Unfortunately, none of the ones that we saw seemed to match the specifications that we had established. 
They were too small, too impersonal, too close to the neighbors.
After days of finding nothing even close, we began to wonder: was there really a perfect house out there for us?"""
               
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
wordnet = WordNetLemmatizer()
ps = PorterStemmer()
wordnet=WordNetLemmatizer()
sentences = nltk.sent_tokenize(paragraph)
corpus = []
for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])
    review = review.lower()
    review = review.split()
## Using Stemming
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()

## Using Lemmitization
corpus_1 = []
for i in range(len(sentences)):
    review_1 = re.sub('[^a-zA-Z]', ' ', sentences[i])
    review_1 = review_1.lower()
    review_1 = review_1.split()
    review_1 = [wordnet.lemmatize(word) for word in review_1 if not word in set(stopwords.words('english'))]
    review_1 = ' '.join(review_1)
    corpus_1.append(review_1)
    
# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X_lem = cv.fit_transform(corpus_1).toarray()
