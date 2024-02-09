##Tokenization - To convert given texts into words or sentences.

text = "It was a very pleasant day, the weather was cool and there were light showers. I went to the market to buy some flowers."

##files required to use tokenizers.

import nltk
nltk.download('punkt')

##Punkt is made to learn parameters from a corpus in an unsupervised way that is related to the target domain, such as a list of abbreviations, acronyms, etc.
from nltk.tokenize import sent_tokenize,word_tokenize

##tokenize every sentence.
sents = sent_tokenize(text)
print(sents)

##tokenze every word.
new_sents = word_tokenize(text.lower())
print(new_sents)