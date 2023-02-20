#https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

#binary 2base? bin(number)[2:]
#count specific character from a string? str.count('val)
def count_bits(n):
    return bin(n)[2:].count('1')


#imporved?
def countBits(n):
    return bin(n).count("1")