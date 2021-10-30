package com.assignment.week5;

public class cube extends rectangle implements volume{


    cube(double Side) {
        super(Side);
    }

    // --- Inherit from "rectangle" class ---
    @Override
    public void area() {
        System.out.println("The area of cube is = "+getArea());
    }

    // --- Inherit from "rectangle" class ---
    @Override
    public void perimeter() {
        System.out.println("The perimeter of cube is = "+getPerimeter());
    }

    // --- Inherit from "rectangle" class ---
    @Override
    public double getArea() {
        // Formula = 6 * side
        return 6 * Side;
    }

    // --- Inherit from "rectangle" class ---
    @Override
    public double getPerimeter() {
        // Formula = 12 * Side
        return 12 * Side;
    }

    // --- Implement from "Volume" interface class ---
    @Override
    public double getVolume() {
        // Formula = s^3
        return Math.pow(Side,3);
    }

    // --- Implement from "Volume" interface class ---
    @Override
    public void Volume() {
        System.out.println("The volume of cube is = "+getVolume());
    }

    // ---Declare Public Modifier to Display side diagonal of cube---
    public void side_diagonal(){
        // Side Diagonal of the cube
        System.out.println("The Side Diagonal of the cube is = "+Side+"√2");
    }

    // ---Declare Public Modifier to Display space diagonal of cube---
    public void space_diagonal(){
        // Space Diagonal of the cube
        System.out.println("The Space Diagonal of the cube is = "+Side+"√3");
    }
}
