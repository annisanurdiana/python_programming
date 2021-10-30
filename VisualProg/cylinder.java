package com.assignment.week5;

public class cylinder extends circle implements volume{

    private double Height;
    private final double phi = 3.14;

    cylinder(double Radius) {
        super(Radius);
    }

    // ----Call or return the value of an attribute to the caller
    public double getHeight(){
        return Height;
    }

    /* ---Setter modifies the value of an attribute based on the value sent by
            the caller using the input parameter */
    public void setHeight(double Height){
        this.Height = Height;
    }

    // --- Inherit from "Circle" class ---
    @Override
    public void area() {
        System.out.println("The area of cylinder is = "+getArea());
    }

    // --- Inherit from "Circle" class ---
    @Override
    public void perimeter() {
        System.out.println("The perimeter of cylinder is = "+getPerimeter());
    }

    // --- Inherit from "Circle" class ---
    @Override
    public double getArea() {
        // Formula surface area of cylinder = 2πr(r+t)
        return 2*phi*Radius*(Radius+getHeight());
    }

    // --- Inherit from "Circle" class ---
    @Override
    public double getPerimeter() {
        // Formula perimeter of cylinder = 2(height + length)
        // length = perimeter the two bases of the tube >> 2.π.r²
        // height = cylinder height
        return 2*(getHeight()+2*phi*Math.pow(Radius,2));
    }

    // --- Implement from "Volume" interface class ---
    @Override
    public double getVolume() {
        // Formula volume of cylinder  = h.π.r²
        return getHeight()*phi*Math.pow(Radius,2);
    }

    // --- Implement from "Volume" interface class ---
    @Override
    public void Volume() {
        System.out.println("The volume of cylinder is = "+getVolume());
    }
}
