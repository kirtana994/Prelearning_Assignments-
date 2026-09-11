/*Task 6: Write a program to find the factorial of a number using a recursive function*/

function factorial(num){
    let fact=1;
    if(num==0 || num==1){
        return fact;
    }
    else{
        return num*factorial(num-1);
    }
}
console.log("Factorial of 5 is: " + factorial(5));
console.log("Factorial of 0 is: " + factorial(0));