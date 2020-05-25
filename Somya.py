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
