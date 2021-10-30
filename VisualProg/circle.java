package com.assignment.week5;

public class circle extends shape{
    private final double phi = 3.14;
    private double Area_A;
    private double Area_P;
    double Radius;

    circle(double Radius) {
        this.Radius = Radius;
    }

    // ----Call or return the value of an attribute to the caller
    public double getArea_A(){
        return Area_A;
    }

    /* ---Setter modifies the value of an attribute based on the value sent by
        the caller using the input parameter */
    public void setArea_A(double Area_A){
        this.Area_A = Area_A;
    }

    // ----Call or return the value of an attribute to the caller
    public double getArea_P(){
        return Area_P;
    }

    /* ---Setter modifies the value of an attribute based on the value sent by
        the caller using the input parameter */
    public void setArea_P(double Area_P){
        this.Area_P =  Area_P;
    }

    // --- Inherit from "Shape" class ---
    @Override
    public double getArea() {
        // The Area of Circle = phi x r^2
        return phi * Math.pow(Radius,2);
    }

    // --- Inherit from "Shape" class ---
    @Override
    public double getPerimeter() {
        // The Formula of Perimeter = 2 x phi x r
        return 2*phi*Radius;
    }

    // --- Inherit from "Shape" class ---
    @Override
    public void area() {
        System.out.println("The area of circle is = "+getArea());
    }

    // --- Inherit from "Shape" class ---
    @Override
    public void perimeter() {
        System.out.println("The perimeter of circle is = "+getPerimeter());
    }

    // ----Call or return the value of an attribute to the caller
    public long getFindR_A(){
        return (long) (getArea_A()/(2 * phi));
    }

    // ----Call or return the value of an attribute to the caller
    public long getFindR_P(){
        // Math.sqrt(x) = root in java
        return (long) Math.sqrt(getArea_P()/phi);
    }

    // ---Declare Public Modifier to Display radius from Area and Perimeter---
    public void FindR_A() {
        System.out.println("So, the radius of circle is = "+ getFindR_A());
    }
    public void FindR_P() {
        System.out.println("So, the radius of circle is = "+getFindR_P());
    }
}
