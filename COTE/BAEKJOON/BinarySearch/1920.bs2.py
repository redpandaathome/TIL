#someone else's code!

ip = input
def main():
    ip()
    n = ip().strip().split(' ')
    ip()
    
    s = set(n)
    r = ''
    for k in input().strip().split(' '):
        r += '1\n' if k in s else '0\n'
    print(r)

if __name__ == "__main__":
    main()