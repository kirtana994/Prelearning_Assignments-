/*Task 1: Need to create JavaScript functions for a sum of numbers in the string (Example 
like “foo8bar8cat2tc2”) */

function sumofNumbersInString(str) {
    let sum=0;
    let pattern=/\d/g;
    let num=str.match(pattern);
    for(let i=0;i<num.length;i++){
        sum+=Number(num[i]);
    }
    return sum;
}

let inputString = "foo8bar8cat2tc2";
let result = sumofNumbersInString(inputString);
console.log("The sum of numbers in the string is: " + result);
console.log("The sum of numbers in the string is: " + sumofNumbersInString("abc5xyz3hello7world2"));