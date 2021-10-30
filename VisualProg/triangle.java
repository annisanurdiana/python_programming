package com.assignment.week5;

public class triangle extends shape {
    double base_t;
    double height_t;
    private double side_1;
    private double side_2;
    private double side_3;
    // ----Call or return the value of an attribute to the caller
    public double getSide_1(){
        return side_1;
    }

    /* ---Setter modifies the value of an attribute based on the value sent by
        the caller using the input parameter */
    public void setSide_1(double side_1){
        this.side_1 = side_1;
    }
    // ----Call or return the value of an attribute to the caller
    public double getSide_2(){
        return side_2;
    }

    /* ---Setter modifies the value of an attribute based on the value sent by
        the caller using the input parameter */
    public void setSide_2(double side_2){
        this.side_2 = side_2;
    }
    // ----Call or return the value of an attribute to the caller
    public double getSide_3(){
        return side_1;
    }

    /* ---Setter modifies the value of an attribute based on the value sent by
        the caller using the input parameter */
    public void setSide_3(double side_3){
        this.side_3 = side_3;
    }

    triangle(double base_t, double height_t) {
        this.base_t = base_t;
        this.height_t = height_t;
    }

    @Override
    public void area() {
        System.out.println("The area of triangle is = "+getArea());
    }

    @Override
    public void perimeter() {
        System.out.println("The perimeter of triangle is = "+getPerimeter());
    }

    @Override
    public double getArea() {
        return base_t*height_t*0.5;
    }

    @Override
    public double getPerimeter() {
        return getSide_1()+getSide_2()+getSide_3();
    }
}
