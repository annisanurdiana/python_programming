package com.assignment.week5;

public class triangular_pyramid extends triangle implements volume{

    private double height_py;

    triangular_pyramid(double base_t, double height_t) {
        super(base_t, height_t);
    }

    // ----Call or return the value of an attribute to the caller
    public double getHeight_py(){
        return height_py;
    }

    /* ---Setter modifies the value of an attribute based on the value sent by
        the caller using the input parameter */
    public void setHeight_py(double height_py){
        this.height_py = height_py;
    }

    // --- Implement from "Volume" interface class ---
    @Override
    public double getVolume() {
        return (0.33*base_t*height_t*0.5)*getHeight_py();
    }
    // --- Implement from "Volume" interface class ---
    @Override
    public void Volume() {
        System.out.println("The volume of triangular prism is = "+getVolume());
    }
}
