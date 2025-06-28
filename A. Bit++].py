a = int(input())
count = 0
n = 0

for x in range(a):
    b = input()
    if b == 'X++' or b == '++X':
        count+=1
    elif b == 'X--' or b == '--X':
        count-=1

print(count)