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
    print("Hey, welcome to the math helper.")
    validation = True

    while validation == True:
        print("What would you like to do?")
        print("1. Basic Operations (like +, -, x, and ÷)\n2. Complex Operations (like square root)\n3. Statistical Operations (like finding the mean)\n0. Exit the program")
        userTask = input("Enter menu option: ")

        if userTask == "1":
            print("What operation would you like to carry out?\n1. +\n2. -\n3. x\n4. ÷")
            userChoice1 = input("Enter choice: ")

            if userChoice1 == "1":
                a = float(input("Enter a number: "))
                b = float(input("Enter another number: "))
                c = a+b
                print(f"{a} + {b} = {c}")

            elif userChoice1 == "2":
                a = float(input("Enter a number: "))
                b = float(input("Enter another number: "))
                c = a-b
                print(f"{a} - {b} = {c}")

            elif userChoice1 == "3":
                a = float(input("Enter a number: "))
                b = float(input("Enter another number: "))
                c = a*b
                print(f"{a} x {b} = {c}")
            
            elif userChoice1 == "4":
                a = float(input("Enter a number: "))
                b = float(input("Enter another number: "))
                c = a/b
                print(f"{a} ÷ {b} = {c}")
            
            else:
                print("Invalid choice.")
            

            askUser = input("Would you like to continue? (y/n): ")
            if askUser == "y":
                validation = True
            else:
                print("Alright, exiting program.")
                validation = False



        elif userTask == "2":
            print("What would you like to do?\n1. Square Root\n2. Cube Root\n3. Power")
            userChoice2 = input("Enter choice: ")

            if userChoice2 == "1":
                a = float(input("Enter the number you want to square root: "))
                c = math.sqrt(a)
                print(f"√ {a} = {c}")
            
            elif userChoice2 == "2":
                numInput = float(input("Enter the number you want to cube root: "))
                cube_root(numInput)

            elif userChoice2 == "3":
                numInput = float(input("Enter a number: "))
                powerInput = float(input("Enter the power: "))
                answer = numInput**powerInput
                print(f"{numInput}^{powerInput} = {answer}")

            else:
                print("Invalid choice.")
            

            askUser2 = input("Would you like to continue? (y/n): ")
            if askUser2 == "y":
                validation = True
            else:
                print("Alright, exiting program.")
                validation = False



        elif userTask == "3":
            print("What would you like to do?\n1. Mean\n2. Median\n3. Mode\n4. Standard Deviation")
            userChoice3 = input("Enter choice: ")

            if userChoice3 == "1":
                a = input("Enter your values, separated by a comma and space, e.g., ', ': ")

                b = a.split(", ")

                i = 0
                for i in range(len(b)):
                    b[i] = float(b[i])
                    i = i+1
  
                print("Your list of values are:")
                print(b)

                meanValue = statistics.mean(b)
                print(f"The mean is: {meanValue}")

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
            
            elif userChoice3 == "2":
                a = input("Enter your values, separated by a comma and space, e.g., ', ': ")

                b = a.split(", ")

                i = 0
                for i in range(len(b)):
                    b[i] = float(b[i])
                    i = i+1
  
                print("Your list of values are:")
                print(b)

                medianValue = statistics.median(b)
                print(f"The median is: {medianValue}")
            
            elif userChoice3 == "3":
                a = input("Enter your values, separated by a comma and space, e.g., ', ': ")

                b = a.split(", ")

                i = 0
                for i in range(len(b)):
                    b[i] = float(b[i])
                    i = i+1
  
                print("Your list of values are:")
                print(b)

                modalValue = statistics.mode(b)
                print(f"The mode is: {modalValue}")
            
            elif userChoice3 == "4":
                a = input("Enter your values, separated by a comma and space, e.g., ', ': ")

                b = a.split(", ")

                i = 0
                for i in range(len(b)):
                    b[i] = float(b[i])
                    i = i+1
  
                print("Your list of values are:")
                print(b)

                stdDevValue = statistics.stdev(b)
                print(f"The standard deviation is: {stdDevValue}")
            
            else:
                print("Invalid option.")

            askUser3 = input("Would you like to continue? (y/n): ")
            if askUser3 == "y":
                validation = True
            else:
                print("Alright, exiting program.")
                validation = False
        
        elif userTask == "0":
            print("Alright, exiting program.")
            validation = False

        else:
            print("Invalid task.")
            askUser4 = input("Would you like to continue? (y/n): ")
            if askUser4 == "y":
                validation = True
            else:
                print("Alright, exiting program.")
                validation = False

menu()