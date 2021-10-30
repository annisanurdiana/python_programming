package com.assignment.week5;

public class pyramid extends rectangle implements volume{

//-----------Rectangular Pyramid----------------//

    private double Height;
    private double Frame;
    private double areaTriangle;

    pyramid(double Side) {
        super(Side);
    }

    // ----Call or return the value of an attribute to the caller
    public double getAreaTriangle(){
        return areaTriangle;
    }

    /* ---Setter modifies the value of an attribute based on the value sent by
    the caller using the input parameter */
    public void setAreaTriangle(double areaTriangle){
        this.areaTriangle = areaTriangle;
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

    // ----Call or return the value of an attribute to the caller
    public double getFrame(){
        return Frame;
    }

    /* ---Setter modifies the value of an attribute based on the value sent by
    the caller using the input parameter */
    public void setFrame(double Frame){
        this.Frame = Frame;
    }

    // --- Inherit from "rectangle" class ---
    @Override
    public void area() {
        System.out.println("The area of rectangular pyramid is = "+getArea());
    }

    // --- Inherit from "rectangle" class ---
    @Override
    public void perimeter() {
        System.out.println("The perimeter of rectangular pyramid is = "+getPerimeter());
    }

    // --- Inherit from "rectangle" class ---
    @Override
    public double getArea() {
        // Formula of surface area = Area.rectangle + 4*Area.triangle
        return Math.pow(Side,2) + 4 * getAreaTriangle();
    }

    // --- Inherit from "rectangle" class ---
    @Override
    public double getPerimeter() {
        // Formula of Pyramid frame length total = perimeter of rectangle + 4*f
        return 4 * Side + 4 * getFrame();
    }

    // --- Implement from "Volume" interface class ---
    @Override
    public double getVolume() {
        // Formula of volume = 1/2 * area.rectangle * height
        return 0.5 * Math.pow(Side,2) * getHeight();
    }

    // --- Implement from "Volume" interface class ---
    @Override
    public void Volume() {
        System.out.println("The volume of rectangular pyramid is = "+getVolume());
    }

    // ---Declare Public Modifier to Display base_side_diagonal of pyramid---
    public void side_diagonal(){
        // Find the side of the base. Diagonal side of the triangle
        System.out.println("The Side Diagonal of the base of rectangular pyramid is = "+Side+"√2");
    }

    // ---Declare Public Modifier to Display base_side_diagonal of pyramid---
    public void perpendicular_diagonal(){
        // Find the perpendicular diagonals on the perpendicular side. Diagonal side of the square
        System.out.println("The perpendicular diagonals on the perpendicular side" +
                " of the rectangular pyramid is = "+0.5*Side+"√3");
    }
}
