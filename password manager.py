import sys
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
            file.write(f"{data} |")
        

    




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
#File_rw.create_file("sample.db")

File_rw.write_on_file("sample.db", "Miro 123")