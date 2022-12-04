import time
import os

menu_options = ('l', 'x')
option1 = "1) Delete Temp Files"
option2 = "2) Delete Log Files"

while True:
    print()
    print("** MENU **")
    print("l = login")
    print("x = exit")


    print()
    user_input = input("Enter an option: ")

    if user_input in menu_options:
        break

    else:
        print()
        print("Option not available")

if user_input == 'l':
    print("Processing....")
    time.sleep(3)
    print()
    user_name = input('Name: ')
    password = input('Password: ')

elif user_input == 'x':
    print()
    print('See you soon')
    exit()

if user_name == ("Mac") and password == ("4dd74dc2"):
    print()
    print('Processing....')
    time.sleep(2)
    print("VICIOUS FPS BOOST")
    print()
    print()
    print(option1)
    print()
    print(option2)
    print()
    print("3) Disable Memory Compression")
    print()
    user_option = input("Enter an option: ")
if user_option == (option1):
    os.system('cmd /k "Delete Temp Files"')