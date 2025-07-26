a=5
b=0
for i in range(a):
   for k in range(b):
        print(" ",end=' ')
   for j in range(a):
       print('0',end=' ')
   for l in range(a-1):
       print('0',end=' ')
   #print()

   a-=1
   b+=1
   if a!=0:
       print()

# print(a+1)

for i in range(6):
    if(a!=1):
        for j in range(b):
            print(' ', end=' ')
        for k in range(a):
            print('0', end=' ')
        for l in range(a-1):
            print('0',end=' ')

    a+=1
    b-=1
    if a!=1:
        print()
    #print()