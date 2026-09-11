/*Task 2: Need to create a JavaScript function for the sum of a string (Example like "1.5, 
2.3, 3.1, 4, 5.5, 6, 7, 8, 9, 10.9") */

function sumOfaString(str){
    let sum=0;
    let num=str.split(",");
    for(let i=0;i<num.length;i++){
        sum+=parseFloat(num[i]);
    }
    return sum;
}

console.log("The sum of the string is: " + sumOfaString("1.5,2.3,3.1,4,5.5,6,7,8,9,10.9"));
console.log("The sum of the string is: " + sumOfaString("10.5, 2.5, 4, 6.75, 3.25"));