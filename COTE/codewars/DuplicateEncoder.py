#[ ]
# count & lower
#  
def duplicate_encode(word):
    #your code here
    word = word.lower()
    new= []
    for el in word:
        if word.count(el)==1:
            new.append("(")
        else:
            new.append(")")
    return ''.join(new)
