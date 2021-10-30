package com.assignment.week5;

// ---Everything in the interface uses abstract methods.

public interface volume {

    double getVolume();
    void Volume();

}

/*

Because not all classes use "volume", so I apply
the interface instead of abstract.

I understand that the interface is implemented not with
the concept of inheritance, but using the concept of realization.

Instead of writing the "volume" method manually,
I decided to use an Interface to manage the code so it is reusable :)

*/