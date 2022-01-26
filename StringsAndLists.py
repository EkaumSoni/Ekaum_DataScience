# -*- coding: utf-8 -*-

#Ekaum Soni
#1/13/2022
#We will learn about strings and lists

# import os, sys, random 

# StringVar1 = "Hello there"
# StringVar2 = "General Kenobi"
# num1 = 8
# num2 = 4.5
# char = "t"
# flag = False





#String concatanation Adding two strings
# print(StringVar1 + " " + StringVar2)
# print(StringVar1 + " " + str(2) + StringVar2)

# print(type(char))

# print("Hello \t Peter \n I am here \\ or not \"Goodbye\"")
 
height = input("What size do you want ur tower to be? ") 
height = int(height)
while height != -1: 
    while height > 25:
        height = input("Not a valid Number. What size do you want ur tower to be? ") 
        height = int(height)
    for i in range(height):
        print(" "*(height-i) + "x"*(i+1) + "  "+ "x"*(i+1) + " "*(height-i));
    height = input("What size do you want ur tower to be? ") 
    height = int(height)
else:
    print("Thank you for leaving. We didnt want you here.")