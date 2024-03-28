class NotInRangeError(Exception): #Custom exception handling
    pass

def check(ch): #Checking for the exception
    if(ch<1 or ch>4):
        raise NotInRangeError("Choice must be in the range of 1 to 3")



def banking(id):
    x=0
    USER_file=id+".txt"
    while(x!=1):
        print("OPTIONS")
        try:
            choice=int(input("Press 1 to Deposit Money \nPress 2 to Withdraw Money\nPress 3 to Check Balance\nPress 4 to Logout\n"))
            check(choice)
        except ValueError: #Checks for integer value only to be entered as Choice
            print("Invalid input. Please enter an integer.")
            continue
        except NotInRangeError as e: #Checks that if the value entered is within the range of the options or not
            print(f"Invalid choice:{e}")
            continue
        
        if(choice==1):
            amt=input("Enter the amount to be Deposited : ")               
            Deposit(amt, USER_file)

        elif(choice==2):
            amt=input("Enter the amount to be Withdrawn : ")
            Withdraw(amt, USER_file)

        elif(choice==3):
            Display(USER_file)

        elif(choice==4):
            x=1
            

def Deposit(amt, file_name):
    with open(file_name, "a+") as file:
        # Check if the file is empty
        file.seek(0, 2)  # Move to the end of the file
        if file.tell() == 0:  # If the file is empty
            file.write("(0.0, 0.0, 0.0)\n")
        
        # Read the last line and extract the last element
        file.seek(0)  # Move to the beginning of the file
        lines = file.readlines()
        last_line = lines[-1].strip()  
        elements = last_line.strip("()").split(", ")  # Split into individual elements
        last_elements = float(elements[2])
        # Append the new tuple representing the deposit
        file.write(f"({float(amt):.2f}, 0.0, {float(last_elements) + float(amt):.2f})\n")
        print(f"Deposited {float(amt):.2f}$ Current Balance {float(last_elements) + float(amt):.2f}")

def Withdraw(amt, file_name):
    with open(file_name, "a+") as file:
        # Check if the file is empty
        file.seek(0, 2)  # Move to the end of the file
        if file.tell() == 0:  # If the file is empty
            file.write("(0.0, 0.0, 0.0)\n")
            print("Insufficient balance for withdrawl!")
            pass
        
        file.seek(0)  # Move to the beginning of the file
        lines = file.readlines()
        last_line = lines[-1].strip()  
        elements = last_line.strip("()").split(", ")  # Split into individual elements
        last_elements = float(elements[2])
        # Append the new tuple representing the withdrawl
        if float(last_elements) < float(amt): #Balance check
            print("Insufficient balance for withdrawl!")
        else:
            file.write(f"(0.0, {float(amt):.2f}, {float(last_elements) - float(amt):.2f})\n")
            print(f"Withdrawled {float(amt):.2f}$ Current Balance {float(last_elements) - float(amt):.2f}$")

def Display(file_name):
    with open(file_name, "a+") as file:
        file.seek(0, 2)  # Move to the end of the file
        if file.tell() == 0:  # If the file is empty
            file.write("(0.0, 0.0, 0.0)\n")
            print("Your Current Balance is 0.0$")
            return
        file.seek(0)  # Move to the beginning of the file
        lines = file.readlines()
        last_line = lines[-1].strip()  
        elements = last_line.strip("()").split(", ")  # Split into individual elements
        last_elements = float(elements[2])
        if(last_elements==0.0):
            print("Your Current Balance is 0.0$")
        else:
            print(f"Your current balance is {last_elements :.2f}$")

