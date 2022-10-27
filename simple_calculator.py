from logging import exception
from re import X
from statistics import multimode

"""
First project :)
"""

'''
calculator is going to be a function that holds helper functions that are going to perform the
operations.
'''



def calculator():
    user = input("Hi This is a Calculator Press m for Menu or q to quit: ")
    try:
        if user == "Q" or user == "q":
            return print("Goodbye!")
        if user == "m" or user == "M":
            print("Addition (a)")
            print("Subtraction? (s)")                                 
            print("Multiplication? (x)")                              
            print("Division? (d)")
            print("Exponents? (e)")
            second2 = input("What operation would you like to do: ")
            if second2 == 'a' or second2 == "A":
                add() 
            elif second2 == 's' or second2 =='S':
                subtract() 
            elif second2 == 'x' or second2 =='X':
                multiply()
            elif second2 == 'd' or second2 == 'D':
                division()  
            elif second2 == 'e' or second2 == 'E':
                return exponentt()            
    except:
        print("invalid input")
        return calculator()


def add():
    try:
        ad1 = float(input("enter a number to add: "))
        ad2 = float(input("enter another numebr to add: "))
        print("your answer is ",ad1+ad2)
        user = input("would you like to add again (a) or go to the menu (m): ")
        if user == 'm' or user == 'M':
            return calculator()
        elif user == 'a' or user == 'A':
            return add()
    except:
        print("invalid input")
        return add()
   

def subtract():
    try:
        sub1 = float(input("enter a number to subtract from: "))
        sub2 = float(input("enter a number to subtract: "))
        print("your answer is ",sub1-sub2)
        user = input("would you like to subtract again (s) or go to the menu (m): ")
        if user == 'm' or user ==  'M':
            return calculator()
        elif user == 's' or user == 'S':
            return subtract()
    except:
        print("invalid input")
        return subtract()

def multiply():
    try:
        prod1 = float(input("enter a number to multiply: "))
        prod2 = float(input("enter another number to multiply: "))
        print("your answer is ",prod1*prod2)
        user = input("press (x) to multiply again or (m) to go to the menu: ")
        if user == 'X' or user =='x':
            return multiply()
        elif user == 'm' or user == 'M':
            return calculator()
    except:
        print("invalid input")
        return multiply()

def division():
    try:
        div1 = float(input("enter a Dividend: "))
        div2 = float(input("enter a divisor: "))
        print("your answer is ",div1/div2)
        user = input("press (d) to divide again or (m) for the menu: ")
        if user == 'd' or user == 'D':
            return division()
        elif user == 'm' or user == 'M':
            return calculator()
    except:
        print("invalid input")
        return division()

def exponentt():
    try:
        base = float(input(("enter a number that is the base of the exponent: ")))
        exponent = float(input("enter a exponent"))
        print("your answer is ",base**exponent)
        user = input("press (e) for exponentiation or (m) for the menu: ")
        if user == 'e' or user == 'E':
            return exponent()
        elif user == 'm' or user == 'M':
            return calculator()
    except:
        print("invalid input")
        return exponentt() 
    

def main():
    calculator()

main()