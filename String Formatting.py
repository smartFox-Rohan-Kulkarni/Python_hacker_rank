def print_formatted(number):
    # your code goes here
    w = len(str(bin(number))[2:])+1
    for i in range(1,n+1):

        o = str(oct(i))[2:]
        h = str(hex(i))[2:]
        h = h.upper()
        b = str(bin(i))[2:]
        d = str(i)

        print("",end=" " * int((w-1)-len(d)))
        print(d,end=" " * int(w-len(o)))
        print(o, end=" " * int(w-len(h)))
        print(h,end=" " * int(w-len(b)))
        print(b)

if __name__ == '__main__':
