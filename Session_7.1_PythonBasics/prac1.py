#Write a python program to find the sum of first N prime numbers. 
n=int(input("Enter a range:"))
sum=0
count=0
num=2
while count<n:
    isPrime=True

    for i in range(2,num):
         if(num%i==0):
            isPrime=False
            break
    if isPrime:
        sum+=num;
        count+=1
    num+=1
print(f"Sum of first {n} prime numbers is: {sum}")