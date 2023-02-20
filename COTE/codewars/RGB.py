def rgb(r, g, b):
    #your code here :)
    return hex16(r)+hex16(g)+hex16(b)

def hex16(n):
    if n<0:
        return '00'
    elif n>255:
        return 'FF'
    else:
        temp = '0'+hex(n)[2:]
        return temp.upper()[-2:]


# improved - lambda x: min(bigRange, max(x, smallRange))
# formatting 0xFF -> FF
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))