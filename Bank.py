x = 1
while x != 0:
    print("Welcome to RxJ Banking")
    print("Press 1 to Login \nPress 2 to Signin\nPress 3 to Exit")
    choice = input()  # Read input as string

    try:
        choice = int(choice)  # Convert input to integer
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    print("Choice entered:", choice)  # Debug print

    from LOGIN import Log_in, Sign_in
    from BANKING import banking

    if choice == 1:
        flag,id_track = Log_in(False)
        if flag:
            print("Login Successful!")
            banking(id_track)
        else:
            print("Login Failed, Try Later")

    elif choice == 2:
        Sign_in()

    elif choice == 3:
        x = 0
    else:
        print("Wrong Choice!")
