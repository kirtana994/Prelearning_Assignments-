#Create a program to read a CSV file and print its content
with open('./Session_7.2/scholarships.csv','r') as file:
    content=file.read()
print("The content of the CSV file is:", content)