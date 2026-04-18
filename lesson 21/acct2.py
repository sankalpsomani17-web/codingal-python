def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word)>1 and word [0] ==word[-1]:
            ctr+= 1
            lst.append(word)
    count= match_words(['abc','cfc','xyz','aba','aba','1221'])
    print("list of words with first and last character same:", count)