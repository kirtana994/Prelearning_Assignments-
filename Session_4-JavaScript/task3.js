/*Task 3: Write a JavaScript program that creates a class called 'Shape' with a method to 
calculate the area. Create two subclasses, 'Circle' and 'Triangle', that inherit from the 
'Shape' class and override the area calculation method. Create an instance of the 'Circle' 
class and calculate its area. Similarly, do the same for the 'Triangle' class. */

class Shape {
    area(){
        console.log("Area calculation");
    }
}
class Circle extends Shape {
    constructor(radius){
        super();
        this.radius=radius;
    }
    area(){
        return Math.PI * this.radius * this.radius;
    }
}
class Triangle extends Shape {
    constructor(base, height){
        super();
        this.base=base;
        this.height=height;
    } 
    area(){
        return 0.5 * this.base * this.height;
    }
}
let circle = new Circle(3);
console.log("Area of Circle: " + circle.area());
let triangle = new Triangle(4, 5);
console.log("Area of Triangle: " + triangle.area());
