##NLP text preprocessing pipeline in nltk
#   Tokenization → Stemming → Lemmatization → Remove stopwords → Remove punctuation
import nltk
from nltk.tokenize import word_tokenize  
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import *
p_stemmer = PorterStemmer()

text="In computer science, lexical analysis, lexing or tokenization is the process of converting a sequence of characters"


#Tokenization
nltk_tokenList = word_tokenize(text)

#Stemming
nltk_stemedList = []
for word in nltk_tokenList:
    nltk_stemedList.append(p_stemmer.stem(word))

#Lemmatization
wordnet_lemmatizer = WordNetLemmatizer()
nltk_lemmaList = []
for word in nltk_stemedList:
    nltk_lemmaList.append(wordnet_lemmatizer.lemmatize(word))

print("Stemming + Lemmatization")
print(nltk_lemmaList)

#Filter stopword
filtered_sentence = []  
nltk_stop_words = set(stopwords.words("english"))
for w in nltk_lemmaList:  
    if w not in nltk_stop_words:  
        filtered_sentence.append(w)
        
#Removing Punctuation
punctuations="?:!.,;"
for word in filtered_sentence:
    if word in punctuations:
        filtered_sentence.remove(word)
print(" ")
print("Remove stopword & Punctuation")
print(filtered_sentence)