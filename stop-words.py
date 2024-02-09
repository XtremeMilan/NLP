import spacy
#loading the english language small model of spacy

spacy_nlp = spacy.load('en_core_web_sm')    


##getting default stopwords in spacy
stopwords = spacy_nlp.Defaults.stop_words
print('Stopwords in Spacy are:')
print()
print(len(stopwords))
print(stopwords)

##in case you want to add your own stopword
#spacy_nlp.Defaults.stop_words.add("spacy")

##in case you want to remove a stopword
#spacy_nlp.Defaults.stop_words.remove("using")

article = spacy_nlp("we will show how to remove stopwords using spacy library ")
##geting tokens

doc = spacy_nlp(article)
tokens = [token.text for token in doc]
print('Original Article: %s' % (article))
print()
print('Tokens:',tokens)

##The lst will keep only those words that are not in stopwords
lst=[]
for token in tokens:
    if token.lower() not in stopwords:    #checking whether the word is not 
        lst.append(token)                    #present in the stopword list.
print()        

#Join items in the list
print("Article after removing stopwords  :   ",  ' '.join(lst))
