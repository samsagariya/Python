def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

for idx,item in enumerate(df.title):
    if not(isEnglish(item)) == True:

        df.drop(idx, inplace=True)
print(df)
