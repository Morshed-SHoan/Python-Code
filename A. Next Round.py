# n = int(input())
# k = int(input())
n, k = map(int, input().split())
count = 0
#a=[]
#a = int(input())
a = list(map(int, input().split()))
for i in range(n) :
    if a[i] >= a[k-1] and a[i] != 0 :
        count+=1


print(count)

