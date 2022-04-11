def anagrams(word, words):
    #your code here
    return [w for w in words if ''.join(sorted(list(w)))==''.join(sorted(list(word)))]

#improved
# python can sort string...!
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]


#lambda! & filter(lambda key: ,list)
#~in Python 3 where filter returns an iterator
def anagrams(word, words):
    return list(filter(lambda x: sorted(word.lower())==sorted(x.lower()),words))