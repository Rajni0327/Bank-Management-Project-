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
        accnumber = input("please tell your account number : ")
        pin = int(input("please tell your pin :"))

        userdata = [i for i in Bank.data if i ['accountNo'] == accnumber and i['pin'] == pin ]

        if userdata == False :
            print("sorry no data found")

        else:
            amount = int(input("enter the amount you want to deposit : "))
            if amount >10000 or amount <0 :
                print("sorry the amount is too much , you can deposit below 10000")
            else :
                userdata[0]['balance'] += amount
                Bank.__update()
                print("AMOUNT DEPOSITED SUCCESSFULLY")
    

    def withdrawMoney(self):
        accnumber = input("please tell your account number : ")
        pin = int(input("please tell your pin :"))

        userdata = [i for i in Bank.data if i ['accountNo'] == accnumber and i['pin'] == pin ]

        if userdata == False :
            print("sorry no data found")

        else:
            amount = int(input("enter the amount you want to withdraw : "))
            if userdata[0]['balance'] < amount  :
                print("sorry you dont have that much money")
            else :
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("AMOUNT WITHDREW SUCCESSFULLY")

    def showDetails (self):
        accnumber = input("please tell your account number : ")
        pin = int(input("please tell your pin :"))

        userdata = [i for i in Bank.data if i ['accountNo'] == accnumber and i['pin'] == pin ]

        print("your informations are : \n")
        for i in userdata [0]:
            print(f"{i} :{userdata[0][i]}")



    def updateDetails (self):
        accnumber = input("please tell your account number : ")
        pin = int(input("please tell your pin :"))

        userdata = [i for i in Bank.data if i ['accountNo'] == accnumber and i['pin'] == pin ]

        if userdata == False :
            print("no such user found")
        else :
            print("you cannot change the age , account number and balance ")
            print("fill the details for change or leave it empty if no change")

            newdata = {
                "name" : input("enter your new name or press enter to skip :"),
                "email" :input("enter your new email address or press enter to skip"),
                "pin" : input("enter your new pin or press enter to skip : ")
            } 

            if newdata ["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata ["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata ["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
                
            newdata['age'] = userdata[0]['age']
            newdata['accountNo'] = userdata[0]['accountNo']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])


            for i in newdata :
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] =  newdata[i]


            Bank.__update()
            print("DETAILS UPDATED SUCCESSFULLY ")


    def deleteAccount(self) : 
        accnumber = input("please tell your account number : ")
        pin = int(input("please tell your pin :"))

        userdata = [i for i in Bank.data if i ['accountNo'] == accnumber and i['pin'] == pin ]

        if userdata ==False:
            print("sorry no such data found")

        else :
            check = input("press y if you actually want to delete your account  ")
            if check == 'n' or check =='N' :
                print("bypassed")
            else :
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully")

                Bank.__update()


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
    user.depositMoney()
elif check == 3:
    user.withdrawMoney()
elif check == 4 :
    user.showDetails()
elif check == 5:
    user.updateDetails()
elif check == 6 :
    user.deleteAccount()
  