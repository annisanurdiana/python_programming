package com.assignment.week1;

// -- Public Class --
/* The class is accessible by any other class. */
public class IT4_001202000067_TaxFormula {

    // -- Static Class -&- Default Class --
    /* Static : The method belongs to the Main class and not an object of the Main class. */
    /* Default: The class is only accessible by classes in the same package. */
    static class Tax_TI{

        // -- Private --
        /* Only has access restrictions from within the class.*/
        private double nti;  // --Non-taxable Income
        private double agi;  // --Annual Gross Income
        private double ti;   // --Taxable Income
        private String name; // --Customer's name

        // -- Final --
        /* it means that we cannot change the data fields, but if not, we can change the fields*/
        private final int minTI; // --50M
        private final int medTI; // --250M
        private final int maxTI; // --500M

        // -- Private --
        private double percent_1/*_5%_*/, percent_2/*_15%_*/, percent_3/*_25%_*/, percent_4/*_30%_*/;

        // -- Constructor --
        /* The method that will call the first time the Object was created.*/
        Tax_TI(int min_TI, int med_TI, int max_TI){
            this.minTI = min_TI;
            this.medTI = med_TI;
            this.maxTI = max_TI;
        }



        //---------------------Getter Setter---------------------//


        // -- Public Modifier --
        /* To controls the access level and the code is accessible for all classes.*/
        public String getName(){
            return name;
        }
        public void setName(String name) {
            this.name = name;
        }
        public double getNti(){
            return nti;
        }
        // -- Public Modifier --
        public void setNti(double nti) {
            this.nti = nti;
        }
        public double getAgi(){
            return agi;
        }
        // -- Public Modifier --
        public void setAgi(double agi) {
            this.agi = agi;
        }
        public double setTi(){
            ti = this.agi - this.nti;
            return ti;
        }



        //---------------------Percent Method---------------------//


        // -- Public Modifier (Global Modifier) --
        public void Percent_1(double percent_1) {
            this.percent_1 = percent_1;
        }
        public void Percent_2(double percent_2) {
            this.percent_2 = percent_2;
        }
        public void Percent_3(double percent_3) {
            this.percent_3 = percent_3;
        }
        public void Percent_4(double percent_4) {
            this.percent_4 = percent_4;
        }



        //------------------Tax Formula - Method------------------//


        /* Declaring the tax calculation formula according to the range */
        private double range_1, range_2, range_3, range_4;

        // -- Private Modifier --
        private double Formula(){
            range_1 = ti * this.percent_1;
            return range_1;
        }
        // -- Private Modifier --
        private double Formula2(){
            range_2 = this.percent_1 * this.minTI + (ti - this.minTI) * this.percent_2;
            return range_2;
        }
        // -- Private Modifier --
        private double Formula3(){
            range_3 = this.percent_1 * this.minTI +this.percent_2 * (this.medTI - this.minTI) + (ti - this.medTI) *this.percent_3;
            return range_3;
        }
        // -- Private Modifier --
        private double Formula4(){
            range_4 = this.percent_1 * this.minTI + this.percent_2 * (this.medTI - this.minTI) + this.percent_3 * (this.maxTI - this.medTI) + (ti - this.maxTI) * this.percent_4;
            return range_4;
        }



        //---------------------Display Method---------------------//


        // --Call Method---
        /* To displays the amount of tax costs according to the TI amount range.*/
        public void Display(){
            // -- If Tax Income equal to zero
            if (ti == 0){
                System.out.println("\nHello "+getName()+"! This is your tax: \n>> NO TAX <<");
            }
            // -- If Tax Income less than or equal to 50000000
            else if (ti <= this.minTI){
                System.out.println("\nHello "+getName()+"! Your Tax is "+Formula());
            }
            // -- If Tax Income more than 50000000 or less than or equal 250000000
            else if (this.minTI < ti || ti <= this.medTI){
                System.out.println("\nHello "+getName()+"! Your Tax is "+Formula2());
            }
            // -- If Tax Income more than 250000000 or less than or equal 500000000
            else if (this.medTI < ti || ti <= this.maxTI){
                System.out.println("\nHello "+getName()+"! Your Tax is "+Formula3());
            }
            // -- If Tax Income more than 500000000
            else if (ti > this.maxTI){
                System.out.println("\nHello "+getName()+"! Your Tax is "+Formula4());
            }
            else {
                System.out.println("\nINVALID!");
            }
        } /* Display Method End */
    }/* Tax_TI - Static Class End */
}/* IT4_001202000067_TaxFormula - Class End */
