package com.assignment.week5;

public class triangular_prism extends triangle implements volume{

    private double height_p;

    triangular_prism(double base_t, double height_t) {
        super(base_t, height_t);
    }


    // ----Call or return the value of an attribute to the caller
    public double getHeight_p(){
        return height_p;
    }

    /* ---Setter modifies the value of an attribute based on the value sent by
        the caller using the input parameter */
    public void setHeight_p(double height_p){
        this.height_p = height_p;
    }

    // --- Implement from "Volume" interface class ---
    @Override
    public double getVolume() {
        return (base_t*height_t*0.5)*getHeight_p();
    }
    // --- Implement from "Volume" interface class ---
    @Override
    public void Volume() {
        System.out.println("The volume of triangular prism is = "+getVolume());
    }
}
