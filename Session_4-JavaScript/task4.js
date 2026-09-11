/*Task 4: Write a JavaScript program that creates a class called University with properties 
for university names and departments. Include methods to add a department, remove a 
department, and display all departments. Create an instance of the University class and 
add and remove departments. */

class University{
    constructor(name){
        this.name=name;
        this.departments=[];
    }
    addDepartment(department){
        this.departments.push(department);
    }
    removeDepartment(department){
        this.departments=this.departments.filter(dep=>dep!==department);
    }
    displayDepartments(){
        console.log("Departments in " + this.name +" are:");
        for(let i=0;i<this.departments.length;i++){
            console.log(this.departments[i]);
        }
    }
}

let university = new University("CVM University");
university.addDepartment("Computer Science");
university.addDepartment("Cyber Security");
university.addDepartment("Electronics and Communication");
university.displayDepartments();
console.log("\nAfter removing Cyber Security department");
university.removeDepartment("Cyber Security");
university.displayDepartments();