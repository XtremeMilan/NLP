#spaCy lemmatizing

import spacy
#loading the english language small model of spacy

spacy_nlp = spacy.load('en_core_web_sm')    

article = spacy_nlp("we will show how to remove stopwords using spacy library ")
##geting tokens

doc = spacy_nlp(article)
tokens = [token.text for token in doc]
print('Original Article: %s' % (article))
print()
print('Tokens:',tokens)


lemma_list = []
for token in doc:
    lemma_list.append(token.lemma_)
print("Tokenize+Lemmatize:")
print(lemma_list)