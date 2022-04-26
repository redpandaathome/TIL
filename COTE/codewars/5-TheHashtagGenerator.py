
# str.title() -> capitalize first character
# str.split() -> separated chunks through all the spaces unlike js
# >>> list("foobar")
# ['f', 'o', 'o', 'b', 'a', 'r']
def generate_hashtag(s):
    arr=s.split()
    result="#"
    for el in arr:
        result+=el.title()
    return result if len(result)<=140 and len(result)>1 else False