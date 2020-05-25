import pandas as pd
import re
df= pd.read_csv('1.csv', sep='|',error_bad_lines=False)
dfn.reset_index()
dfn.shape 

eng =[]

def isEnglish(s):

    try:

        s.encode(encoding='utf-8').decode('ascii')

    except UnicodeDecodeError:

        return False

    else:

        return True



for idx,item in enumerate(dfn.title):

    if isEnglish(item) == False:
        eng.append(idx)
               
print(eng)

def engprepo(line):
    line=line.lower()
    doc_spacy = en_nlp(line)
    a = [token.lemma_ for token in doc_spacy]
    my_stop=set(stopwords.words('english')+list(punctuation))
    words=[w for w in a if not w in my_stop if len(w)>2]
    return words

