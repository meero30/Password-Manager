import sys
import os
class Person:
    num_of_people = 0
    def __init__(self):
        self.first_init = True
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        Person.num_of_people += 1
        

    def get_token(self):
        #return (self.email, self.password)
        print(self.email, self.password)

    def create_new_acc(self):
        if self.first_init == True:
            
            print("Hello new user, to create an account please enter the following details")
            self.first_name = input("Enter your first name: ")
            self.last_name = input("Enter your last name: ")
            self.email = input("Enter your email: ")
            self.password = input("Create your new password: ")

            self.first_init = False

class File_rw:

    @staticmethod
    def create_file(file_name):
        try:

            file = open(file_name, mode="x")
            file.close()
        except FileExistsError:
            print(f"FileExistsError: {file_name} already exists!")
    
    @staticmethod
    def write_on_file(file_name,data):

        with open(file_name, mode = "a") as file:
            file.write(f"{data}\n")
        
    @staticmethod
    def read_file(file_name):
        
        with open(file_name, mode = "r") as file:
            database = file.readlines()
            return(database)

    @staticmethod
    def clear_file(file_name):
        if os.path.exists(file_name) == True:
            file = open(file_name, mode="w")
            file.close()
        else: 
            print(f"Error: {file_name} does not exist")
    

class Crypt:
    @staticmethod
    # Caesar cipher with Ascii from 33 to 126
    def encrypt(data, key):
        
        alist = []
        for c in data:
            sum_key = ord(c) + key
            if sum_key > 126: #upper bound
                num = (ord(c) - 126) + (32 + key)
                alist.append(chr(num))
            elif sum_key < 33: #lower bound
                num = (ord(c) - 33) + (127 + key)
                alist.append(chr(num))
            else:
                num = sum_key
                alist.append(chr(num))
        #print("".join(alist))
        return("".join(alist))

    @staticmethod
    def decrypt(data, key):
        alist = []
        for c in data:
            diff_key = ord(c) - key
            if diff_key > 126: #upper bound
                num = (ord(c) - 126) + (32 - key)
                alist.append(chr(num))
            elif diff_key < 33: #lower bound
                num = (ord(c) - 33) + (127 - key)
                alist.append(chr(num))
            else:
                num = diff_key
                alist.append(chr(num))
        #print("".join(alist))
        return("".join(alist))

#I: 124 key:4
#num = ord(c) - 126 + (33 + key) Equation

# class Vault:
#     def __init__(self):
#         self.store = []

#     def get_info(self,info = None):
#         if type(info) == type(""):
#             self.store.append(info)
#         else:
#             print("Invalid data type")

    
# person1 = Person()
# person1.create_new_acc()
# person1.get_token()

# File_rw.create_file("Database.db")
# File_rw.write_on_file("Database.db", "samplemail@fake.com")
# File_rw.write_on_file("Database.db", "samplemail2@fake.com")

# File_rw.read_file("Database.db")
# File_rw.clear_file("Datafase.db")
Crypt.encrypt("Miro", 93)
Crypt.decrypt("Lhqn", 93)
