package com.assignment.week5;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

/*

Name        : ANNISA NURDIANA
Class       : INFORMATION TECHNOLOGY - 4 / 2020
Student ID  : 001202000067

>>>PROBLEM,
    "Calculate Area and Perimeter and More of Shapes - Geometry Program"

>>>DISPLAY,
    ========================== GEOMETRY CALCULATION  ==========================
    1. Shape 2D
    2. Shape 3D
    Please choose one according to the numbers above. Enter Number: <input int>

    ***

    If the numbers chosen are not 1 and 2 then,
    >>> "Exception Error Handle" <<<

    ***

    if choose number 1 then,
    Here is a selection from number 1:
    1. Circle
    2. Rectangle
    3. Triangle
    What do you want to calculate? choose one: <input int>

    if choose "1" then,
    1. Find the Radius
    2. Calculate the perimeter
    3. Calculate Area
    What do you want to calculate? choose one: <input int>

    if choose "1" then,
    1. Find the Radius if the perimeter is known
    2. Find the Radius if area is known
    What do you want to calculate? choose one: <input int>

    ***

    if choose "2" then,
    1. Find the Side Diagonals
    2. Calculate the perimeter
    3. Calculate Area
    What do you want to calculate? choose one: <input int>

    ---
    if choose number 2 then,
    1. Cube
    2. Cylinder
    3. Rectangular Pyramid
    4. Sphere
    What do you want to calculate? choose one: <input int>
    ---
    If choose '1' then,
    1. Find the Side Diagonals
    2. Find the Space Diagonal
    3. Calculate the perimeter
    4. Calculate Area
    5. Calculate the Volume
    What do you want to calculate? choose one: <input int>
    ---
    If choose '2' then,
    1. Calculate the perimeter
    2. Calculate Area
    3. Calculate the Volume
    What do you want to calculate? choose one: <input int>
    ---
    If choose '3' then,
    1. Find the diagonal of the side of the base
    2. Find the perpendicular diagonals on the perpendicular side
    3. Calculate the Perimeter
    4. Calculate Area
    5. Calculate Volume
    What do you want to calculate? choose one: <input int>
    ---
    If choose '3' then,
    1. Calculate Area
    2. Calculate the Volume
    What do you want to calculate? choose one: <input int>

    ***

    if choose number 3 then,
    1. Triangle Area
    2. Triangle Perimeter
    What do you want to calculate? choose one: <input int>
    ---
    if choose number 3 then,
    1. Triangular pyramid.
    2. Triangular prism.
    What do you want to calculate? choose one: <input int>
    ---
    If choose '1' then,
    Calculate Volume of Triangular pyramid.
    What do you want to calculate? choose one: <input int>

    If choose '2' then,
    Calculate Volume of Triangular prism.
    What do you want to calculate? choose one: <input int>

>>>PROGRAM,
    1. Display the geometry calculation statement
    2. Displays a command to select a statement
    2. Receive user input according to the input command
    4. Runs and displays the output according to what the user has selected
    5. Displays the second part specific geometry calculation options
    6. The program starts according to the input
    7. The results of the input are displayed

>>>SOLUTION,
    ...

*/

public class Main {
    public static void main(String[]args){
        // ---BufferedReader which is assisted by InputStreamReader---
        InputStreamReader streamReader = new InputStreamReader(System.in);
        // ---InputStreamReader so that it can read Input from the Keyboard---
        BufferedReader write = new BufferedReader((streamReader));

        // ---Exception Handle---
        try {
            System.out.print("\n========================== GEOMETRY CALCULATION  ==========================\n");
            System.out.println("1. Shape 2D");
            System.out.println("2. Shape 3D");
            System.out.print("\nPlease choose one according to the numbers above. Enter Number: ");
            int value = Integer.parseInt(write.readLine());

            switch (value) {
                case 1:
                    // Create a Scanner object
                    Scanner input = new Scanner(System.in);
                    // ---Calculate_Shape2D--
                    System.out.println("Here is a selection from number 1:");
                    System.out.println("1. Circle");
                    System.out.println("2. Rectangle");
                    System.out.println("3. Triangle");
                    System.out.print("What do you want to calculate? choose one: ");
                    int choose = input.nextInt();

                    if (choose == 1){
                        // Create a Scanner object
                        Scanner in = new Scanner(System.in);
                        System.out.println("\nHere is a selection from '1':");
                        System.out.println("1. Find the Radius");
                        System.out.println("2. Calculate the perimeter");
                        System.out.println("3. Calculate Area");
                        System.out.print("What do you want to calculate? choose one: ");
                        int choose2 = in.nextInt();

                        if (choose2 == 1){
                            // --A. Find the Radius--
                            System.out.println("\nif choose number 1 then,");
                            System.out.println("A. Find the Radius if the perimeter is known");
                            System.out.println("B. Find the Radius if area is known");
                            System.out.print("What do you want to calculate? choose one: ");
                            String value2A = in.nextLine();

                            circle Circle_ = new circle(0);

                            switch (value2A){
                                case "A":
                                    System.out.print("\nPlease enter the value of circle perimeter: ");
                                    double num_perimeter_c = Double.parseDouble(write.readLine());
                                    Circle_.setArea_P(num_perimeter_c);

                                    System.out.println("\n");
                                    Circle_.FindR_P();
                                    break;

                                case "B":
                                    System.out.print("\nPlease enter the value of circle area: ");
                                    double num_area_c = Double.parseDouble(write.readLine());
                                    Circle_.setArea_A(num_area_c);

                                    System.out.println("\n");
                                    Circle_.FindR_A();
                                    break;

                                default:
                                    System.out.println("\n ===INVALID===");

                            } // --- switch case value2_end ---
                        } // --- if else choose2_end ---

                        else if (choose2 == 2){
                            // --B. Calculate the perimeter of circle--
                            System.out.print("\nPlease enter the value of circle radius: ");
                            double num_radius = Double.parseDouble(write.readLine());
                            shape Circle = new circle(num_radius);

                            System.out.println("\n");
                            Circle.perimeter();
                        }

                        else if (choose2 == 3){
                            // --C. Calculate the area of circle--
                            System.out.print("\nPlease enter the value of circle radius: ");
                            double num_radius = Double.parseDouble(write.readLine());
                            shape Circle = new circle(num_radius);

                            System.out.println("\n");
                            Circle.area();
                        }
                    }// --- if else choose_end ---

                    else if (choose == 2){
                        // ---Shape_Rectangle---
                        // Create a Scanner object
                        Scanner in = new Scanner(System.in);
                        System.out.println("\nHere is a selection from '2':");
                        System.out.println("1. Find the Side Diagonals");
                        System.out.println("2. Calculate the perimeter");
                        System.out.println("3. Calculate Area");
                        System.out.print("What do you want to calculate? choose one: ");
                        int choose2 = in.nextInt();

                        if (choose2 == 1){
                            // ---Find the Side Diagonals---
                            System.out.print("\nPlease enter the value of rectangle side: ");
                            double num_side = Double.parseDouble(write.readLine());
                            rectangle Rectangle_ = new rectangle(num_side);

                            System.out.println("\n");
                            Rectangle_.side_diagonal();
                        }
                        else if (choose2 == 2 ){
                            // ---Calculate the perimeter---
                            System.out.print("\nPlease enter the value of rectangle side: ");
                            double num_side = Double.parseDouble(write.readLine());
                            shape Rectangle = new rectangle(num_side);

                            System.out.println("\n");
                            Rectangle.perimeter();
                        }
                        else if (choose2 == 3 ){
                            // ---Calculate Area---
                            System.out.print("\nPlease enter the value of rectangle side: ");
                            double num_side = Double.parseDouble(write.readLine());
                            shape Rectangle = new rectangle(num_side);

                            System.out.println("\n");
                            Rectangle.area();
                        }
                    }
                    else if (choose == 3){
                        // ---Shape_Triangle---
                        // Create a Scanner object
                        Scanner in = new Scanner(System.in);
                        System.out.println("\nHere is a selection from 3:");
                        System.out.println("1.Triangle Perimeter");
                        System.out.println("2.Triangle Area");
                        System.out.print("What do you want to calculate? choose one: ");
                        int choose2 = in.nextInt();

                        if (choose2 == 1){
                            // ---Calculate the perimeter---
                            System.out.print("\nPlease enter the value of triangle base-1: ");
                            double num_base1 = Double.parseDouble(write.readLine());
                            System.out.print("\nPlease enter the value of triangle base-2: ");
                            double num_base2 = Double.parseDouble(write.readLine());
                            System.out.print("\nPlease enter the value of triangle base-3: ");
                            double num_base3 = Double.parseDouble(write.readLine());

                            shape Triangle = new triangle(0,0);
                            triangle Triangle_ = new triangle(0,0);
                            Triangle_.setSide_1(num_base1);
                            Triangle_.setSide_2(num_base2);
                            Triangle_.setSide_3(num_base3);
                            System.out.println("\n");
                            Triangle.perimeter();
                        }
                        else if(choose2 == 2){
                            // ---Calculate the Area---
                            System.out.print("\nPlease enter the value of triangle base: ");
                            double num_base = Double.parseDouble(write.readLine());
                            System.out.print("\nPlease enter the value of triangle height: ");
                            double num_height = Double.parseDouble(write.readLine());

                            shape Triangle = new triangle(num_base,num_height);
                            System.out.println("\n");
                            Triangle.area();
                        }

                    }

                    break;

                case 2:
                    // Create a Scanner object
                    Scanner input_ = new Scanner(System.in);
                    // ---Calculate_Shape3D--
                    System.out.println("\nHere is a selection from number 1:");
                    System.out.println("1. Cube");
                    System.out.println("2. Cylinder");
                    System.out.println("3. Rectangular Pyramid");
                    System.out.println("4. Sphere");
                    System.out.println("5. Triangular pyramid.");
                    System.out.println("6. Triangular prism.");
                    System.out.print("What do you want to calculate? choose one: ");
                    int choose_2 = input_.nextInt();

                    if (choose_2 == 1){
                        // Create a Scanner object
                        Scanner in = new Scanner(System.in);
                        // ---Shape 3D >> Cube
                        System.out.println("\nHere is a selection from '1' :");
                        System.out.println("1. Find the Side Diagonals");
                        System.out.println("2. Find the Space Diagonal");
                        System.out.println("3. Calculate the perimeter");
                        System.out.println("4. Calculate Area");
                        System.out.println("5. Calculate the Volume");
                        System.out.print("What do you want to calculate? choose one: ");
                        int chooseValue = in.nextInt();

                        if (chooseValue == 1){
                            // ---Find the Side Diagonals---
                            System.out.print("\nPlease enter the value of rectangle side: ");
                            double num_side = Double.parseDouble(write.readLine());
                            rectangle Cube = new cube(num_side);

                            System.out.println("\n");
                            Cube.side_diagonal();

                        } else if (chooseValue == 2){
                            // ---Find the Space Diagonals---
                            System.out.print("\nPlease enter the value of rectangle side: ");
                            double num_side_ = Double.parseDouble(write.readLine());
                            cube Cube_d = new cube(num_side_);

                            System.out.println("\n");
                            Cube_d.space_diagonal();

                        } else if (chooseValue == 3){
                            // ---Calculate the perimeter---
                            System.out.print("\nPlease enter the value of rectangle side: ");
                            double num_side_p = Double.parseDouble(write.readLine());
                            rectangle Cube_p = new cube(num_side_p);

                            System.out.println("\n");
                            Cube_p.perimeter();

                        } else if (chooseValue == 4){
                            // ---Calculate Area---
                            System.out.print("\nPlease enter the value of rectangle side: ");
                            double num_side_a = Double.parseDouble(write.readLine());
                            rectangle Cube_a = new cube(num_side_a);

                            System.out.println("\n");
                            Cube_a.area();

                        } else if (chooseValue == 5){
                            // ---Calculate the volume---
                            System.out.print("\nPlease enter the value of rectangle side: ");
                            double num_side_v = Double.parseDouble(write.readLine());
                            cube Cube_v = new cube(num_side_v);

                            System.out.println("\n");
                            Cube_v.Volume();

                        } else{

                            System.out.println("\n ===INVALID===");
                        }
                    }

                    else if (choose_2 == 2){
                        // Create a Scanner object
                        Scanner in = new Scanner(System.in);
                        // ---Shape 3D >> Cylinder
                        System.out.println("\nHere is a selection from '2' :");
                        System.out.println("1. Calculate the perimeter");
                        System.out.println("2. Calculate Area");
                        System.out.println("3. Calculate the Volume");
                        System.out.print("What do you want to calculate? choose one: ");
                        int value_Shape3D = in.nextInt();

                        switch (value_Shape3D){
                            case 1:
                                // ---Calculate the perimeter
                                System.out.print("\nPlease enter the value of cylinder radius: ");
                                double num_r = Double.parseDouble(write.readLine());
                                System.out.print("\nPlease enter the value of cylinder height: ");
                                double num_h = Double.parseDouble(write.readLine());
                                circle Cylinder_P = new cylinder(num_r);
                                cylinder Cylinder_ = new cylinder(num_r);
                                Cylinder_.setHeight(num_h);

                                System.out.println("\n");
                                Cylinder_P.perimeter();
                                break;

                            case 2:
                                // ---Calculate Area
                                System.out.print("\nPlease enter the value of cylinder radius: ");
                                double num_r2 = Double.parseDouble(write.readLine());
                                System.out.print("\nPlease enter the value of cylinder height: ");
                                double num_h2 = Double.parseDouble(write.readLine());
                                circle Cylinder_A = new cylinder(num_r2);
                                Cylinder_A.area();
                                cylinder Cylinder_A_ = new cylinder(num_r2);

                                System.out.println("\n");
                                Cylinder_A_.setHeight(num_h2);
                                break;

                            case 3:
                                // ---Calculate the Volume
                                System.out.print("\nPlease enter the value of cylinder radius: ");
                                double num_r3 = Double.parseDouble(write.readLine());
                                System.out.print("\nPlease enter the value of cylinder height: ");
                                double num_h3 = Double.parseDouble(write.readLine());
                                cylinder Cylinder_V = new cylinder(num_r3);
                                Cylinder_V.setHeight(num_h3);

                                System.out.println("\n");
                                Cylinder_V.Volume();
                                break;

                            default:
                                System.out.println("\n ===INVALID===");

                        }// ---Switch_case_value_Cylinder_end---
                    }

                    else if (choose_2 == 3){
                        // Create a Scanner object
                        Scanner in = new Scanner(System.in);
                        // ---Shape 3D >> Rectangular Pyramid
                        System.out.println("\nHere is a selection from '3' :");
                        System.out.println("1. Find the diagonal of the side of the base");
                        System.out.println("2. Find the perpendicular diagonals on the perpendicular side");
                        System.out.println("3. Calculate the Perimeter");
                        System.out.println("4. Calculate Area");
                        System.out.println("5. Calculate Volume");
                        System.out.println("What do you want to calculate? choose one: ");
                        int value_Shape3D = in.nextInt();

                        switch (value_Shape3D){
                            case 1:
                                // ---Diagonal of the side of the base of pyramid
                                System.out.print("\nPlease enter the value of side of the base of pyramid: ");
                                double value_py = Double.parseDouble(write.readLine());
                                rectangle Pyramid_ = new pyramid(value_py);

                                System.out.println("\n");
                                Pyramid_.side_diagonal();
                                break;

                            case 2:
                                // ---Perpendicular diagonals on the perpendicular side
                                System.out.print("\nPlease enter the value of side of the base of pyramid: ");
                                double value_pyp = Double.parseDouble(write.readLine());
                                pyramid Pyramid_2 = new pyramid( value_pyp);

                                System.out.println("\n");
                                Pyramid_2.perpendicular_diagonal();
                                break;

                            case 3:
                                // ---Calculate the Perimeter
                                System.out.print("\nPlease enter the value of side of the base of pyramid: ");
                                double value_sp = Double.parseDouble(write.readLine());
                                System.out.print("\nPlease enter the value of the frame of pyramid: ");
                                double value_f = Double.parseDouble(write.readLine());
                                pyramid Pyramid_p = new pyramid(value_sp);
                                Pyramid_p.setFrame(value_f);
                                rectangle Pyramid_P = new pyramid(value_sp);

                                System.out.println("\n");
                                Pyramid_P.perimeter();
                                break;

                            case 4:
                                // ---Calculate Area
                                System.out.print("\nPlease enter the value of side of the base of pyramid: ");
                                double value_sa = Double.parseDouble(write.readLine());
                                System.out.print("\nPlease enter the value of triangle area: ");
                                double value_at = Double.parseDouble(write.readLine());
                                pyramid Pyramid_A = new pyramid(value_sa);
                                Pyramid_A.setAreaTriangle(value_at);
                                rectangle Pyramid = new pyramid(value_sa);

                                System.out.println("\n");
                                Pyramid.area();
                                break;

                            case 5:
                                // ---Calculate Volume
                                System.out.print("\nPlease enter the value of side of the base of pyramid: ");
                                double value_Vs = Double.parseDouble(write.readLine());
                                System.out.print("\nPlease enter the value of the height of pyramid: ");
                                double value_Vh = Double.parseDouble(write.readLine());
                                pyramid Pyramid_V = new pyramid(value_Vs);
                                Pyramid_V.setHeight(value_Vh);

                                System.out.println("\n");
                                Pyramid_V.Volume();
                                break;

                            default:
                                System.out.println("\n ===INVALID===");

                        }// ---Switch_case_value_RectangularPyramid_end---
                    }

                    else if (choose_2 == 4){
                        // Create a Scanner object
                        Scanner in = new Scanner(System.in);
                        // ---Shape 3D >> Sphere
                        System.out.println("\nHere is a selection from '4' :");
                        System.out.println("1. Calculate Area");
                        System.out.println("2. Calculate Volume");
                        System.out.print("What do you want to calculate? choose one: ");
                        int value_Shape3D = in.nextInt();

                        switch (value_Shape3D){
                            case 1:
                                // --- Calculate Area of Sphere
                                System.out.print("\nPlease enter the value of the radius of sphere: ");
                                double value_rs = Double.parseDouble(write.readLine());
                                circle Sphere = new sphere(value_rs);

                                System.out.println("\n");
                                Sphere.area();
                                break;

                            case 2:
                                // --- Calculate the Volume of Sphere
                                System.out.print("\nPlease enter the value of the radius of sphere: ");
                                double value_rs_ = Double.parseDouble(write.readLine());
                                sphere Sphere_v = new sphere(value_rs_);

                                System.out.println("\n");
                                Sphere_v.Volume();
                                break;

                            default:
                                System.out.println("\n ===INVALID===");

                        }// ---Switch_case_value_Sphere_end---
                    }

                    else if (choose_2 == 5){
                        // --- Calculate the Volume of Triangular pyramid
                        System.out.print("\nPlease enter the value of the height of base of Triangular pyramid: ");
                        double value_tp_h = Double.parseDouble(write.readLine());
                        System.out.print("\nPlease enter the value of the side of base of Triangular pyramid: ");
                        double value_tp_b = Double.parseDouble(write.readLine());
                        System.out.print("\nPlease enter the value of the height of Triangular pyramid: ");
                        double value_tph = Double.parseDouble(write.readLine());

                        triangular_pyramid Triangular_py = new triangular_pyramid(value_tp_b,value_tp_h);
                        Triangular_py.setHeight_py(value_tph);
                        System.out.println("\n");
                        Triangular_py.Volume();
                    }
                    else if (choose_2 == 6){

                        // --- Calculate the Volume of Triangular prism.
                        System.out.print("\nPlease enter the value of the height of base of Triangular prism.: ");
                        double value_tph = Double.parseDouble(write.readLine());
                        System.out.print("\nPlease enter the value of the side of base of Triangular prism.: ");
                        double value_tpb = Double.parseDouble(write.readLine());
                        System.out.print("\nPlease enter the value of the height of Triangular prism.: ");
                        double value_tph_p = Double.parseDouble(write.readLine());

                        triangular_prism Triangular_ps = new triangular_prism(value_tpb,value_tph);
                        Triangular_ps.setHeight_p(value_tph_p);
                        System.out.println("\n");
                        Triangular_ps.Volume();
                    }
                    break;
            } // ---Switch_case_MainMenu_end---
        }
        catch (Exception e) {
            System.out.println(" \n >>>Something went WRONG!<<< \n === Your Input INVALID ===");
        }

    }// ---main_program_end---

}// ---main_class_end---
