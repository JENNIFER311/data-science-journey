num = int(input("Enter a number: "))
result = 0
while num > 0:
    num_1 = num % 10
    result += num_1
    num = num//10
print(result)
