def create_a_list():
    while True:
        value = input()
        if value == "":
            break
        list_1.append(value)

def Pair_swap():
    if len(list_1) > 2:
        for i in range(1,len(list_1),3):
            if i + 1 < len(list_1):
                list_1[i], list_1[i+1] = list_1[i+1], list_1[i]
    else:
        pass

list_1 = []
value = 0
print("Enter a value or simply press enter to stop ")
create_a_list()
Pair_swap()
print(list_1)




