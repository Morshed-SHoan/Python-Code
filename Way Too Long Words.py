a = int(input())

for i in range(a):
    b = input()
    length = len(b)
    if length > 10  :
        print(b[0],end='')
        print(length-2,end='')
        print(b[-1])
    else:
        print(b)