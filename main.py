import json 
import random 
import string 
from pathlib import Path 

class Bank :
    database = 'data.json'
    data = []

    try:
        if Path (database).exists():
            with open(database) as fs :
                data = json.loads (fs.read())
        else:
            print("no such file exist")
    except Exception as err:
        print(f"an exception occured as {err}")

    @staticmethod
    def __update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))


    @classmethod
    def __accountgenerate (cls):
        alpha = random.choices(string.ascii_letters , k = 3)
        num = random.choices(string.digits , k = 3)
        spchar = random.choices("!@#$%^&*" , k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)




    def createAccount(self):
        info = {
            "name" : input("tell your name "),
            "age" : int(input("please tell your age ")),
            "email" : input("tell your email : "),
            "pin" : int(input("tell your 4 number pin : ")),
            "accountNo" : Bank.__accountgenerate(),
            "balance" : 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4 :
            print("sorry you cannot create your account")
        else :
            print("account has been successfully ")
            for i in info :
                print(f"{i}:{info[i]}")
            print("please note down your account number ")


            Bank.data.append(info)

            Bank.__update()


    def depositMoney(self):
        acc = input("please tell your account number : ")
        pin = int(input("please tell your pin :"))







user = Bank()


print("press 1 for creating an account")
print("press 2 for depositing the money ")
print("press 3 for withdrawing the money ")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting account")

check = int(input("tell your response :- "))

if check ==1 :
    user.createAccount()
elif check ==2 :
    user.depositeMoney ()
# elif check == 3:
#     def withdrawAmount()
# elif check == 4 :
#     def details() 
  