#python... to get index in for enumerate
#python replace
#can't replace string element like js txt[1]="h"

def to_camel_case(text):
    #your code here
    nextUp = False
    newStr=''
    for i, v in enumerate(text):
        if v=="-" or v=="_":
            nextUp=True
            v=''
        elif nextUp:
            v=text[i].upper();
            nextUp=False
            
        newStr+=v
            
    return newStr

# improved 👀
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

# title(), replace()
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')