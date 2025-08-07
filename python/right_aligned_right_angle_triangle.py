num = 5
space = 3
for i in range(0,num):
    for j in range(0,num):
        if j <= space:
            print(" ", end = "")
        else:
            print("*", end = "")
    space -= 1
    print()