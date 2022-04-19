alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
cipher   = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM";

def rot13(message):
    result=''
    for el in message:
        if el in alphabet and alphabet.index(el)>=0:
            result+=cipher[alphabet.index(el)]
        else:
            result+=el
    return result

#s1 - translate(maketrans table)
#print(msg.translate(msg.maketrans("ABC", "abc")))
def rot13(message):
    return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))