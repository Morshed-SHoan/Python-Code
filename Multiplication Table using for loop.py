while True:
    num = int(input("Enter a number : "))
    mul = 1
    for i in range(1, 11):
        mul = num * i
        if (i == 10):
            print(f"{num} * {i} : {mul}\n")
            break
        print(f"{num} * {i}  : {mul}")