
#Program to Calculate Area and Circumference of a circle
import os
from pickle import FALSE, TRUE
from xmlrpc.client import TRANSPORT_ERROR

welcome = "***** Welcome to circles.py! *****\nThis program will let you calculate the area and circumference of a circle\n"
menu = "*** Menu ***\n1)Calculate Circumference\n2)Calculate Area\n3)Exit"
prompt = "\nPlease Enter a Value :"
option = 0
pi = 3.141529
radius = 0
circumference = 0
area =0

 ## Function to Calculate Area
def calc_area(radius):
    return pi * (radius ** 2)

## Function to Calculate Circumference
def calc_circumference(radius):
    return 2* pi * radius


## Main Menu Loop
while option != "3":
    
    os.system("Clear")

    ## Printing Welcome and Menu
    print(welcome)
    print(menu)    
    option = input(prompt)
    valid_input = False
    
    if option == "1":
        print("Option 1 Selected")

        while(valid_input == False):
            try:
                radius = float(input("Please Enter Radius"))
                valid_input = True
            except:
                print("Invalid Value, Please Try Again: ")
                valid_input = False

        circumference = calc_circumference(radius)
        print("The Circumference is :")
        print(circumference)
        anykey = input("Press any key to continue")

    elif option == "2":
        print("Option 2 is Selected")

        while(valid_input == False):
            try:
                radius = float(input("Please Enter Radius"))
                valid_input = True
            except:
                print("Invalid Value, Please Try Again: ")
                valid_input = False        

        area = calc_area(radius)
        print("The Area is :")
        print(area)
        anykey = input("Press any key to continue")

    elif option == "3":
        print("Have a Nice Day!!")        
    else:
        print("Invalid Option, Please Try again")
        anykey = input("Press any key to continue")        
        

   



