# str.isnumeric()
# for i,c in enumerate(str):
# str repeat s*10
def increment_string(s):
    start= -1
    for i,c in enumerate(s):
        if c.isnumeric() and s[i:].isnumeric():
            start=i
            break
    if start<0:
        return s+'1'
    numStr=s[start:]
    newNumStr=str(int(numStr)+1)

    if len(numStr)==len(newNumStr):
        return s[:start]+newNumStr
    else:
        return s[:start]+ '0'*(len(numStr)-len(newNumStr)) +newNumStr
            


#s1
#✨str.rstrip() for 'hello     '
#✨str.rstrip('0123456789') will cut numbers away at the very right side
#✨str.zfill(totalDigitNum) '1'.zfill(2) => '01'
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))