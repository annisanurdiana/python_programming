package com.assignment.week5;

public class rectangle extends shape{

    double Side;

    rectangle(double Side) {
        this.Side = Side;
    }

    // --- Inherit from "Shape" class ---
    @Override
    public double getArea() {
        // The Area of Rectangle = s^2
        return Math.pow(Side,2);
    }

    // --- Inherit from "Shape" class ---
    @Override
    public double getPerimeter() {
        // The Perimeter of Rectangle = 4*s
        return 4 * Side;
    }

    // --- Inherit from "Shape" class ---
    @Override
    public void area() {
        System.out.println("The area of rectangle is = "+getArea());
    }

    // --- Inherit from "Shape" class ---
    @Override
    public void perimeter() {
        System.out.println("The perimeter of rectangle is = "+getPerimeter());
    }

    // ---Declare Public Modifier to Display side diagonal of rectangle---
    public void side_diagonal(){
        // Diagonal side of the rectangle
        System.out.println("The Side Diagonal of the rectangle is = "+Side+"√2");
    }
}
