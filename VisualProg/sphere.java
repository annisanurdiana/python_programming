package com.assignment.week5;

public class sphere extends circle implements volume{

    private final double phi = 3.14;

    sphere(double Radius) {
        super(Radius);
    }

    // --- Inherit from "Circle" class ---
    @Override
    public void area() {
        System.out.println("The area of sphere is = "+getArea());
    }

    // --- Inherit from "Circle" class ---
    @Override
    public double getArea() {
        // Formula the area of sphere is 4 π.r²
        return 4*phi*Math.pow(Radius,2);
    }

    // --- Implement from "Volume" interface class ---
    @Override
    public double getVolume() {
        // Formula volume of sphere is 4/3 π.r²
        return 1.33 * phi * Math.pow(Radius,2);
    }

    // --- Implement from "Volume" interface class ---
    @Override
    public void Volume() {
        System.out.println("The volume of sphere is = "+getVolume());
    }
}
