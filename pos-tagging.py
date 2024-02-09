import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("The sky is Blue")
for token in doc:
    print(token,"\t", token.pos_, "\t", token.tag_)
print()
print()
print(f"{'text':{8}} {'POS':{6}} {'TAG':{6}} {'Dep':{6}} {'POS explained':{20}} {'tag explained'} ")
print("-----------------------------------------------------------------------------------------")
for token in doc:
    print(f'{token.text:{8}} {token.pos_:{6}} {token.tag_:{6}} {token.dep_:{6}} {spacy.explain(token.pos_):{20}} {spacy.explain(token.tag_)}')



from spacy import displacy
displacy.render(doc, style = "dep")