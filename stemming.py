#nltk
import nltk
from nltk.tokenize import word_tokenize  
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import *

article="In computer science, lexical analysis, lexing or tokenization is the process of converting a sequence of characters"

nltk_tokenList = word_tokenize(article)

p_stemmer = PorterStemmer()
nltk_stemedList = []
for word in nltk_tokenList:
    nltk_stemedList.append(p_stemmer.stem(word))
        
print(nltk_stemedList)