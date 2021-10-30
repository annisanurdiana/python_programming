package com.assignment.week1;
import com.assignment.week1.IT4_001202000067_TaxFormula.Tax_TI;
import java.util.Scanner;
/*

Name    : ANNISA NURDIANA
Class   : INFORMATION TECHNOLOGY - 4 / 2020

>>>PROBLEM,
    "How to Calculate The Tax in Indonesia with Java Program?"

>>>DISPLAY,
    ============== INDONESIAN TAX CALCULATION ==============
    Please Enter Your Full name          : <String input>
    Enter Your Annual Gross Income       : <double input>
    Enter Your Non-Taxable Annual Income : <double input>

    =============== TABLE OF TAX CALCULATION ===============
    +-------+----------------------------------+-----------+
    | RANGE |       TI AMOUNT (IDR)            |   TAX (%) |
    |_______|__________________________________|___________|
    |   1.  | <= 50 Million                    |     5%    |
    |   2.  | 50 Million < TI <= 250 Million   |    15%    |
    |   3.  | 250 Million < TI <= 500 Million  |    25%    |
    |   4.  | >500 Million                     |    30%    |
    |_______|__________________________________|___________|

    You have input Annual Gross Income : <double output>
    You have input Non-Taxable Income  : <double output>
    This is your Taxable Income:  <double output>

    Hello <String name output>! Your Tax is <the tax result>

>>>PROGRAM,
    Input Name of Customer >> Scanner(System.in)
    Input Annual Gross Income >> Scanner(System.in)
    Input Non-Taxable Income >> Scanner(System.in)
    Display Tax Income from method >> different class
    Display the Tax consider of range from TI-Amount

>>>SOLUTION,
    ...
*/

public class IT4_001202000067 {

    public static void main(String[]args){
        // -- Instantiation scanner object --
        Scanner in = new Scanner(System.in);

        // -- String input and double input --
        System.out.println("\n============== INDONESIAN TAX CALCULATION ==============\n");
        System.out.print("Please Enter Your Full Name  \t\t : "); String Name = in.nextLine();
        System.out.print("Enter Your Annual Gross Income\t\t : "); double AGI = in.nextDouble();
        System.out.print("Enter Your Non-Taxable Annual Income : "); double NTI = in.nextDouble();

        // -- Show Table of TI Amount and Tax Percent plus Range --
        System.out.println("\n=============== TABLE OF TAX CALCULATION ===============\n");
        System.out.println("+-------+----------------------------------+-----------+");
        System.out.println("| RANGE |       TI AMOUNT (IDR)            |   TAX (%) |");
        System.out.println("|_______|__________________________________|___________|");
        System.out.println("|   1.  | <= 50 Million                    |     5%    |");
        System.out.println("|   2.  | 50 Million < TI <= 250 Million   |    15%    |");
        System.out.println("|   3.  | 250 Million < TI <= 500 Million  |    25%    |");
        System.out.println("|   4.  | >500 Million                     |    30%    |");
        System.out.println("|_______|__________________________________|___________|");

        // -- Using Constructor and Declare min,med,max of TI Amount from IT4_001202000067_TaxFormula --
        var main_tax = new Tax_TI(50000000,250000000,500000000);

        // -- Create Object from Class 1 --
        main_tax.setName(Name);main_tax.setNti(NTI);main_tax.setAgi(AGI);

        // -- Input percent with decimal value into object --
        main_tax.Percent_1(0.05);main_tax.Percent_2(0.15);
        main_tax.Percent_3(0.25);main_tax.Percent_4(0.30);

        // -- Display Input --
        System.out.println("You have input Annual Gross Income : "+ main_tax.getAgi());
        System.out.println("You have input Non-Taxable Income  : "+ main_tax.getNti());

        // -- Display TI Result --
        System.out.println("This is your Taxable Income: " + main_tax.setTi());

        // -- Display Tax Result --
        main_tax.Display();
    }
}