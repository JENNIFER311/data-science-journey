import re

class register:
    def password_check(self):
        print("Your password must be atleast 8 characters")
        print("Must have a small letter, a captial letter, a special character")  
        self.password = input("Create password : ")
        self.check_password = True

        while self.check_password:
            self.digits = re.findall(r"\d",self.password)
            self.alphabets_small = re.findall(r"[a-z]",self.password)
            self.alphabets_caps = re.findall(r"[A-Z]",self.password)
            self.special_char = re.findall(r"[^a-zA-Z0-9]",self.password)
            if self.digits != [] and self.alphabets_small != [] and self.alphabets_caps != [] and self.special_char != [] and len(self.password) >= 8 :
                    self.check_password = False
            else:
                    print("Re-enter the password :")
                    self.password = input("Create Password : ")

    def collection(self):
        self.name = input("Create User Name : ")
        self.email = input("Enter email : ")
        self.password_check()
    
        

class login:
    def logging_in(self):
        self.log_name = input("Enter User name : ")
        self.log_pass = input("Enter Password : ")

class verify(register,login):
    def verification(self):
        self.check = 1
        
        while self.check <= 3:
            if self.name == self.log_name and self.password == self.log_pass:
                print ("Entry verified")
                break
            else:
                print("Invalid username and password! ")
                self.logging_in()
                self.check += 1
        else:
            retry = int(input("Press 1 if you forget your user name or password or press 0 for stop process : "))
            if retry == 1:
                self.collection()
                self.logging_in()
                self.verification()
            elif retry == 0:
                print("Sorry no entry! ")
        
        

obj = verify()
obj.collection()
obj.logging_in()
obj.verification()