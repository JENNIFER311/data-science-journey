length = int(input("Enter the total no of values in a list :"))
base = []
for i in range(0, length ):
    value = input("Enter the value : ")
    base.append(value)
list_a = base.copy()
print(list_a)

confrm = length % 2
k = 2

if confrm:
    for i in range(0, length):
        check = i % 2
        if check and i!=0:
            list_a.pop(length - k)
            list_a.insert(length - k, base[i])
            k += 2
        else:
            list_a.pop(i)
            list_a.insert(i,base[i])

else:
    for i in range(0, length):
        check = i % 2
        if check and i!=0:
            list_a.pop(length - i)
            list_a.insert(length - i, base[i])
            
        else:
            list_a.pop(i)
            list_a.insert(i,base[i])

print(list_a)
