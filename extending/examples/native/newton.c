#include "Python.h"
#include <math.h>


static PyObject *
newton(PyObject * self, PyObject *args)
{
    float guess;
    float x;

    if (!PyArg_ParseTuple(args, "ff", &guess, &x))
        return NULL;

    while(fabsf(powf(guess, 2) - x) > 0.01)
        {
            guess = (guess + (x / guess)) / 2;
        }

    return Py_BuildValue("f", guess);
}


static PyMethodDef
module_functions[] = {
    {"newton", newton, METH_VARARGS, "Newton Docstring"},
    {NULL}
};

PyMODINIT_FUNC
initnewton(void){
    Py_InitModule3("newton", module_functions, "Module docstring");
}
