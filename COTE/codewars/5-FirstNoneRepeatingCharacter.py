# for in string, str.lower(), enumerate(), str.rindex(char)
def first_non_repeating_letter(string):
    lower_string=string.lower()
    for i,c in enumerate(lower_string):
        if lower_string.index(c)==lower_string.rindex(c.lower()):
            return string[i]
    return ''


#1
# string.count(letter)
def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
            
    return ""