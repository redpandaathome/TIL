str = 'i love coding'
skips = [0,0,3,2,3,4]
word = 'mask'

strArr = list(str)
wordArr = list(word)
skipArr = list(skips)

wordIndex = 0
jump = 0
copyStr = ['' for i in range(len(strArr))]
print(copyStr)
for i in skipArr:
    jump += i
    jump = jump%len(strArr)
    print("i:",i, ', skipArr:', skipArr[i], ', jump:', jump)
    temp = wordArr[wordIndex%len(wordArr)]
    print('temp:', temp, ", strArr[",jump,']:', strArr[jump])
    copyStr[jump] = copyStr[jump] + temp
    wordIndex += 1
    
print("COPYSTR:", copyStr)
print('-STRARR:', strArr)
ans = ''
for i in range(len(copyStr)):
    ans += copyStr[i]
    ans += strArr[i]

print(ans)


#원하는 결과: 'mai lsovke cmodinag'