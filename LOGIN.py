
import random
def Sign_in():
    name = input("Enter your name : ")
    age = input("Enter your age : ")
    address = input("Enter your Address : ")
    Phn = input("Enter your Phn no. : ")
    email = input("Enter your E-mail address : ")
    PASS = input("Enter your new passward : ") 
    while(True):
        rePASS = input("Re-enter your new passward : ") 
        if(PASS!=rePASS):
            print("Password didn't matched with the first one \nRetry Again\n")
        else:
            print("\nAccount Successfylly Created!")
            break
    ID = random.randint(100000,999999)
    with open("DataBase.txt", "a+") as file:
        file.write(f"{ID} {PASS} {name} {age} {Phn} {address} {email}\n")

    print("\nAccount Details Review\n")
    print("Your user ID : ",ID," Your Password : ",PASS)
    print("Your name : ",name," Your Age : ",age)
    print("Your phn no. : ",Phn," Your Address : ",address)
    print("Your E-mail : ",email)

def Log_in(flag):
    i=1
    print("Chances : 3")
    while(i<=3):
        print("Tryal no. ",i)
        UID = input("Enter your user ID : ")
        PASS = input("Enter your passward : ")
        with open("DataBase.txt","r+") as file:
            word=file.read().split()
            for a in range(0,len(word),1):
                if(word[a]==UID and word[a+1]==PASS):
                    flag=True
                    break
        if(flag!=True):
            i=i+1
            print("Wrong UID or Password")
            print("Try Again\n")
        else:
            break
    return flag,UID

