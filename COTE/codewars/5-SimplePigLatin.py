def pig_it(text):
    arr = text.split()
    sums=''
    for i,c in enumerate(arr):
        tail=''
        temp=''
        for j,w in enumerate(c):
            if w in '!?#@$-_':
                temp+=w
            elif j==0:
                tail=w+'ay'
            else:
                temp+=w
        sums+=temp+tail+' '
    return sums[0:-1]


#1
# ' '.join([])
# x if blah else blahblah for x in arr
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


#2
# isalpha()...
def pig_it(text):
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)
            
    return ' '.join(res)