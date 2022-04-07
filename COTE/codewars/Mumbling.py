def accum(s):
    # your code
    result=[]
    for i,v in enumerate(s):
        result.append(s[i].upper()+s[i].lower()*i)
    return ('-').join(result)


# improved - use for i,v in enumerate(str)
def accums(s):
  return '-'.join(c.upper()+c.lower()*i for i,c in enumerate(s))