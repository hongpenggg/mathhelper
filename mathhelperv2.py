# This is the math helper programme for personal and other uses. Acts as a calculator and more.

import math
import statistics

def cube_root(x):
    if x < 0:
        x = abs(x)
        cube_rooted = x**(1/3)*(-1)
    else:
        cube_rooted = x**(1/3)
    print(f"3√ {x} = {cube_rooted}")


def menu():
    """
    This is the main menu function, with many other functions nested inside. 
    """

    print("Hey, welcome to the math helper.")
    validation = True

    while validation == True:
        print("\nWhat would you like to do?")
        print("1. Basic Operations (like +, -, x, and ÷)\n2. Complex Operations (like square root)\n3. Statistical Operations (like finding the mean)\n4. Display Math Constants (like pi)\n5. Read the Developer Docs\n0. Exit the program")
        userTask = input("Enter menu option: ")



        if userTask == "1":
            print("\nWhat operation would you like to carry out?\n1. +\n2. -\n3. x\n4. ÷")
            userChoice1 = input("Enter choice: ")

            a = float(input("\nEnter first number: "))
            b = float(input("Enter second number: "))

            if userChoice1 == "1":
                c = a+b
                print(f"{a} + {b} = {c}")

            elif userChoice1 == "2":
                c = a-b
                print(f"{a} - {b} = {c}")

            elif userChoice1 == "3":
                c = a*b
                print(f"{a} x {b} = {c}")
            
            elif userChoice1 == "4":
                c = a/b
                print(f"{a} ÷ {b} = {c}")
            
            else:
                print("Invalid choice.")
            

            askUser = input("\nWould you like to continue? (y/n): ")
            if askUser == "y":
                print("\n")
                validation = True
            else:
                print("\nAlright, exiting program.")
                validation = False



        elif userTask == "2":
            print("\nWhat would you like to do?\n1. Square Root\n2. Cube Root\n3. Power\n4. Trigonometric Functions\n5. Angle Functions\n6. Logarithmic Functions")
            userChoice2 = input("Enter choice: ")

            if userChoice2 == "1":
                a = float(input("\nEnter the number you want to square root: "))
                c = math.sqrt(a)
                print(f"√ {a} = {c}")
            
            elif userChoice2 == "2":
                numInput = float(input("\nEnter the number you want to cube root: "))
                cube_root(numInput)

            elif userChoice2 == "3":
                numInput = float(input("\nEnter a number: "))
                powerInput = float(input("Enter the power: "))
                answer = numInput**powerInput
                print(f"{numInput}^{powerInput} = {answer}")

            elif userChoice2 == "4":
                print("\nWhat would you like to do?\n1. Sin(x)\n2. Cos(x)\n3. Tan(x)\n4. Arcsin(x)\n5. Arccos(x)\n6. Arctan(x)")
                print("Note that the operations are done in radians.")
                userTaskk = input("Choice: ")
                a = float(input("\nEnter a number: "))

                if userTaskk == "1":
                    b = math.sin(a)
                    print(f"sin({a}) = {b}")
                elif userTaskk == "2":
                    b = math.cos(a)
                    print(f"cos({a}) = {b}")
                elif userTaskk == "3":
                    b = math.tan(a)
                    print(f"tan({a}) = {b}")
                elif userTaskk == "4":
                    b = math.asin(a)
                    print(f"asin({a}) = {b}")
                elif userTaskk == "5":
                    b = math.acos(a)
                    print(f"acos({a}) = {b}")
                elif userTaskk == "6":
                    b = math.atan(a)
                    print(f"atan({a}) = {b}")
                else:
                    print("Invalid operation.")
            
            elif userChoice2 == "5":
                print("\nWhat would you like to do?\n1. Deg -> Rad\n2. Rad -> Deg")
                userTaskk2 = input("Choice: ")

                a = float(input("\nEnter a value you would like to convert: "))

                if userTaskk2 == "1":
                    radVal = math.radians(a)
                    print(f"{a} is {radVal} radians.")
                elif userTaskk2 == "2":
                    degVal = math.degrees(a)
                    print(f"{a} is {degVal} degrees.")
                else:
                    print("Invalid operation.")

            elif userChoice2 == "6":
                print("\nWhat would you like to do?\n1. Natural Log / ln(x)\n2. Base-10 Log / lg(x)")
                userTaskk3 = input("Choice: ")

                a = float(input("\nEnter a value you would like to log: "))

                if userTaskk3 == "1":
                    logVal = math.log(a)
                    print(f"ln({a}) = {logVal}")
                elif userTaskk3 == "2":
                    logVal = math.log10(a)
                    print(f"lg({a}) = {logVal}")
                else:
                    print("Invalid operation.")

            else:
                print("Invalid choice.")
            

            askUser2 = input("\nWould you like to continue? (y/n): ")
            if askUser2 == "y":
                print("\n")
                validation = True
            else:
                print("\nAlright, exiting program.")
                validation = False



        elif userTask == "3":
            print("\nWhat would you like to do?\n1. Mean\n2. Median\n3. Mode\n4. Standard Deviation")
            userChoice3 = input("Enter choice: ")

            a = input("\nEnter your values, separated by a comma and space, i.e., ', ' : ")

            b = a.split(", ")

            i = 0
            for i in range(len(b)):
                b[i] = float(b[i])
                i = i+1
            
            # Other Method
                # userValidation = True
                # dataList = []
                #
                # While userValidation == True:
                #  userValue = float(input("Enter a value: "))
                #  dataList.append(userValue)
                #  anotherVal = input("Would you like to enter another value? (y/n): ")
                #
                #  if anotherVal == "y":
                #    userValidation = True
                #  elif anotherVal == "n":
                #    userValidation = False
                #  else:
                #    print("Invalid choice.")
            
            print("\nYour list of values are:")
            print(b)
            print("")

            if userChoice3 == "1":
                meanValue = statistics.mean(b)
                print(f"The mean is: {meanValue}")
            
            elif userChoice3 == "2":
                medianValue = statistics.median(b)
                print(f"The median is: {medianValue}")
            
            elif userChoice3 == "3":
                modalValue = statistics.mode(b)
                print(f"The mode is: {modalValue}")
            
            elif userChoice3 == "4":
                stdDevValue = statistics.stdev(b)
                print(f"The standard deviation is: {stdDevValue}")
            
            else:
                print("Invalid option.")


            askUser3 = input("\nWould you like to continue? (y/n): ")
            if askUser3 == "y":
                print("\n")
                validation = True
            else:
                print("\nAlright, exiting program.")
                validation = False
        


        elif userTask == "4":
            print("\nWhat constants would you like me to show?\n1. π\n2. e\n3. tau")
            userChoice4 = input("Choice: ")
            print("")

            if userChoice4 == "1":
                a = math.pi
                print(f"π has a value of {a}")
            elif userChoice4 == "2":
                a = math.e
                print(f"e has a value of {a}")
            elif userChoice4 == "3":
                a = math.tau
                print(f"tau has a value of {a}")
            else:
                print("Invalid choice.")
            
            askUser6 = input("\nWould you like to continue? (y/n): ")
            if askUser6 == "y":
                print("\n")
                validation = True
            else:
                print("\nAlright, exiting program.")
                validation = False



        elif userTask == "5":
            print("\nWhat would you like to see?\n1. Author & Contributors\n2. About Hongpeng\n3. Changelog & Versions\n4. GitHub Link\n5. Apply to Contribute\n6. Contact Information")
            userSelection = input("Choice: ")

            if userSelection == "1":
                print("\n\n********************************")
                print("\nAuthors & Contributors:")
                print("Author: Hongpeng Wei")
                print("\n********************************\n")

            elif userSelection == "2":
                print("\n\n********************************")
                print("""
Hey!

This program was written by Hongpeng Wei, as a simple math tool for lazy people like himself. 🤷‍♂️
He mainly wanted to save himself the time spent finding his calculator, but he's probably spent more time doing this! 🤦‍♂️

Hongpeng is based in Singapore, and is studying computing at VJC. He is part of the third batch of computing students at VJC.

In his free time, Hongpeng codes useless projects like these, writes articles on Medium and Quora and reads about psychology.

You can find out more about Hongpeng at https://hongpeng.webflow.io, or at https://github.com/hongpenggg.

Thanks for reading! 🍻
            """)
                print("********************************\n")
                
            elif userSelection == "3":
                print("\n********************************")
                print("Changelog:\n1. V1.0,22/3/23 -> Basic Code was written\n2. V1.1,22/3/23 -> Added whitespace and options 4 and 5")
                print("*If you'd like to add new functionality, contact the developer. See contact information.*\n")
                print("********************************")
                print("Versions:\nV1.0, 22/03/23\nV1.1, 22/03/23 (Current)")
                print("*New versions will be added as convenient for the developer.*\n")
                print("********************************\n")

            elif userSelection == "4":
                print("\n********************************\nGithub Link: https://github.com/hongpenggg/mathhelper \n********************************")

            elif userSelection == "5":
                print("\n********************************\n")
                print("Apply to contribute:\nEmail whpwhp2018@gmail.com or\nVisit https://hongpeng.webflow.io")
                print("\n********************************\n")

            elif userSelection == "6":
                print("\n********************************\n")
                print("Contact Information:\nEmail: whpwhp2018@gmail.com\nWebsite: https://hongpeng.webflow.io \nLink-in Bio: https://beacons.ai/hongpeng")
                print("\n********************************\n")

            else:
                print("Please select a valid option.")
            
            askUser5 = input("\nWould you like to continue? (y/n): ")
            if askUser5 == "y":
                print("\n")
                validation = True
            else:
                print("\nAlright, exiting program.")
                validation = False
            


        elif userTask == "0":
            print("\nAlright, exiting program.\n")
            validation = False



        else:
            print("Invalid task.")

            askUser4 = input("\nWould you like to continue? (y/n): ")
            if askUser4 == "y":
                print("\n")
                validation = True
            else:
                print("\nAlright, exiting program.")
                validation = False

menu()
# To see what menu() does, hit "help(menu)"
