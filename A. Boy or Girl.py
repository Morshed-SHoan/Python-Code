s = input()
length = len(s)
count = 0
sort = sorted(s)

for i in range(length):

    if sort[i-1] == sort[i]:
        continue
    else:
        count+=1


if count%2==0:
    print("CHAT WITH HER!")
else :
    print("IGNORE HIM!")

# Shortcut

#items = input()
## Convert list to a set to eliminate duplicates
#unique_items = set(items)
#length = len(unique_items)
#if length%2==0:
#    print("CHAT WITH HER!")
#else :
#    print("IGNORE HIM!")