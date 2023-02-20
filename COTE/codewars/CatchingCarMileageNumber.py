# 🤔

# solution1
# str in str2, str[::-1], arr.-__contains__
# tests = ()
# for a, b in zip(as, bs):
# any(test(num) for test in tests)
def is_round(number): return set(str(number)[1:])==set('0')
def is_incre(number): return str(number) in '1234567890'
def is_decre(number): return str(number) in '9876543210'
def is_palindrome(number): return str(number)== str(number)[::-1]

def is_interesting(number, awesome_phrases):
    tests = (is_round, is_incre, is_decre, is_palindrome, awesome_phrases.__contains__)
    
    for num, color in zip(range(number, number+3), (2,1,1)):
        if num >=100 and any(test(num) for test in tests):
            return color
    return 0


# solution2
# str(number) in '1234567890 9876543210'

def is_good(number, awesome_phrases):
    return str(number) in '1234567890 9876543210' or number in awesome_phrases or int(str(number)[1:])==0 or str(number)==str(number)[::-1]

def is_interesting(number, awesome_phrases):
    if number>99 and is_good(number,awesome_phrases):
        return 2
    elif (number>98 and is_good(number+1,awesome_phrases)) or (number>97 and is_good(number+2,awesome_phrases)):
        return 1
    return 0
