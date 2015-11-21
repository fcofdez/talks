#include <math.h>


float
newton(float guess, float x)
{
    while(fabsf(powf(guess, 2) - x) > 0.01)
    {
        guess = (guess + (x / guess)) / 2;
    }

    return guess;
}
