from cryptography.fernet import Fernet

class passwordmanager:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dictionary = {}
    
    def create_key(self,path):
        self.key = Fernet.generate_key()
        print(self.key)
        with open(path,"wb") as f:
            f.write(self.key)
    
    def load_key(self,path):
        with open(path,"rb")as f:
            f.read(self.key)

    def create_password_file(self,path,initial_values = None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                pass
        
    def load_password_file(self, path):
        self.password_file = path

        with open(path,"r") as f:

            for line in  f:
                site, encrypted = line.split(":")
                self.password_dictionary[site] = Fernet(self.key).decrypt(encrypted.encode())
    
    def add_password(self,site,password):
        self.password_dictionary[site]= password

        if self.password_file is not None :
            with open(self.password_file,'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write ( site + ":" + encrypted.decode() + "\n")

    def get_password(self,site):
        return self.password_dict[site] 
    
def main():
password = {
        "email" : "abc123",
        "facebook" : "abc123",
        "youtube" : "abc123"
}

pm = passwordmanager()

print(" what do you want to do?")
print("(1) generate and create new key")
print("(2) load an existing new key")
print("(3) create a new password file")
print("(4) load an existing password file")
print("(5) add a new password ")
print("(6) get a new password")
print("(q) quit")

done = False

while not done:
    choice = input("press a number to decide what you wanna do")
    if choice == "1":
        path = input("enter path:")
        pm.create_key(path)
    elif choice == "2":
        path = input("enter path:")
        pm.load_key(path)
    elif choice == "3":
        path = input("enter path:")
        pm.create_password_file(path,password)
    elif choice == "4":
        path = input("enter path:")
        pm.load_password_file(path)
    elif choice == "5":
        path = input("enter path:")
        pm.create_password_file(path,password)
    elif choice == "6":
        path = input("enter path")
        pm.get_password (path,password)
    else:
        exit
         

