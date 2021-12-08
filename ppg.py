import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['#','$','%','&','*','_']

coder = "Ravi"
version = "0.0.1"

print(f"""
██████╗░██████╗░░█████╗░███████╗░░░  ██████╗░░█████╗░░██████╗░██████╗░██████╗░███████╗███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝░░░  ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝░██╔════╝████╗░██║
██████╔╝██████╔╝██║░░██║█████╗░░░░░  ██████╔╝███████║╚█████╗░╚█████╗░██║░░██╗░█████╗░░██╔██╗██║
██╔═══╝░██╔══██╗██║░░██║██╔══╝░░░░░  ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗██║░░╚██╗██╔══╝░░██║╚████║
██║░░░░░██║░░██║╚█████╔╝██║░░░░░██╗  ██║░░░░░██║░░██║██████╔╝██████╔╝╚██████╔╝███████╗██║░╚███║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚══╝
            
   Coded by {coder}                                                   version. {version}   """)

print()

print("                  ##############################################")
print("                  #  Welcome to the Prof. Password Generator!  #")
print("                  ##############################################")
print("\n")


user_choice  = "y"

while(user_choice.lower() == 'y'):

    ui_letters = int(input("How many letters would you like in your password?\n>> "))

    ui_symbols = int(input("How many symbols would you like?\n>> "))

    ui_numbers = int(input("How many numbers would you like?\n>> "))

    password = ""

    for char in range(0,ui_letters):
        random_char = random.choice(letters)
        password += random_char

    for char in range(0,ui_symbols):
        random_sym = random.choice(symbols)
        password += random_sym

    for char in range(0,ui_numbers):
        random_num = random.choice(numbers)
        password += random_num
    
    print("----------------------------------------------------------------")
    print("Your final Password is here --> ",password)
    print("----------------------------------------------------------------")
    print()

    user_choice = input("Wanna create again? (Y/y = yes or N/n = no)\n>> ")

print("Bye....")