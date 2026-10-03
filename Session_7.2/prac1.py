#Write a program to reverse a string without using built-in methods.
str=input("Enter a string:")

rev_str=""
for i in str:
    rev_str=i+rev_str
print("The reversed string is:",rev_str)