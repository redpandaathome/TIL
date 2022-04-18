def make_readable(seconds):
    # Do something
    hour=int(seconds/(60*60))
    seconds= int(seconds-hour*60*60)
    min=int((seconds)/60)
    second=int(seconds%60)
    return pad(hour)+":"+pad(min)+":"+pad(second)

def pad(n):
    return '0'+str(n) if n<10 else str(n)


#s1 >>> no
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

#trial1 >>> ok
# '{:02}:~'.format()
# int()
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(int(s/(60*60)), int(s/60%60), int(s%60))

#s2
def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)