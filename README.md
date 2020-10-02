## Tokenisation :

Tokenisation - a technique that’s used to split the text into smaller elements. These elements can be characters, words, sentences, or even paragraphs depending on the requirement
There are multiple types of tokenizer present in nltk library. These are:

 - Word Tokenizer
 - Sentence Tokenizer
 - Tweet Tokenizer
 - Regex Tokenizer
 
## Bag Of Words:
Bag Of Words is a document of matrix

## Stemming:
This technique cuts all the suffix of a word and get the root form of it which also known as Stem.
There are two types of stemmers.
       - Porter Stemmer 
       - Snowball Stemmer

## Lemmatization: 
It also does the same thing as Stemming and bring the word to its root word but here the process is more sofisticated and it converted the word into its meaningful root word.Whereas the root word from Stemming sometime might note have a meaningful word. Hence, This process take more time compare to the previous as it requires to check the dictionary. The most popular lemmatizer is  **WordNet lemmatizer. 

## TF - IDF ( Term Frequency & Inverse Document Frequency)

This technique takes into account the importance of each word. Where as the bag of words considers all the words in a sentence has equal importance which is not correct

### Term Frequency - Number of repetation of a word in a sentence / Number of total number of words in a sentence

#### Inverse Document Frequency - log ( Number of Sentences / Number of Sentences containing the word)
