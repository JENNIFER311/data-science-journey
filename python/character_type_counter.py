str_1 = input("Enter a string : ")
digit = 0
alpha = 0
space = 0
special = 0
for i in str_1:
    check_0 = i.isalnum() 
    check_1 = i.isdigit()
    check_2 = i.isalpha()
    check_3 = i.isspace()
    if check_0 == 0:
        if check_3:
            space += 1
        else:
            special += 1
    elif check_1:
        digit += 1
    elif check_2:
        alpha += 1
    
print(f"There are {digit} digit, {alpha} alphabets, {special} special character and {space} spaces in the given string")