def valid_parentheses(string):
    cnt=0
    for i in string:
        if i=='(':
            cnt+=1
        elif i==")":
            cnt-=1
        if cnt<0:
            return False
    return cnt==0