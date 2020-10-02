# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 16:31:37 2020

@author: 91973
"""

import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords

import re

essay = """Looking back on a childhood filled with events and memories, 
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

text= re.sub(r'\[[0-9]*\]',' ',essay) # Remove unnecessary numbeers and special characters
text = re.sub(r'\s+',' ',text) # Remove space
text = text.lower() # make all the words lower case
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

sentences = nltk.sent_tokenize(text)
sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

# Remove the stopwords
for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]
    
#Modelling
model = Word2Vec(sentences, min_count=1) # min_count is used to consider a word which occurs min how many times

words = model.wv.vocab






