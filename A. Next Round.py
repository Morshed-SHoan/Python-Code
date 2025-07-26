# n = int(input())
# k = int(input())
n, k = map(int, input().split())
#n, k = int(input().split())
count = 0
a=[]
#a = int(input())
#print(type(a))
a = list(map(int, input().split()))
#print(type(a))

for i in range(n) :
    if a[i] >= a[k-1] and a[i] != 0 :
        count+=1


print(count)

