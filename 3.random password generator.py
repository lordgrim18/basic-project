import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

#generation part
def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    
    random.shuffle(characters)
    
    password_list = []
    
    for x in range(password_length):
        password_list.append(random.choice(characters))
    
    random.shuffle(password_list)
    
    password_string = "" .join(password_list)
    print(password_string)

#calling part
while True:
    option = input("Do you want to generate a password? (Yes/No): ").lower()

    if option == "yes":
        generate_password()
    elif option == "no":
        print("Thank you")
        quit()
    else:
        print("Invalid input, please input Yes or No")
