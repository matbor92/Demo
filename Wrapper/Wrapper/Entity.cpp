#include "Entity.h"
namespace CLI
{
    //Creating a native object Calculater, via wrapper, in C++/ClI code
    Calculator::Calculator(float a, float b)
        : ManagedObject(new Core::Calculator(a, b))
    {
        Console::WriteLine("Creating a new Calculator-wrapper object!");
    }
    //running native method "calculate", and saving output to finalArray
    array<float>^ Calculator::calculate()
    {
        Console::WriteLine("The calculate method from the Wrapper was called!");
        float* w_results = m_Instance->calculate();

        array < float > ^ finalArray = gcnew array<float>(4);
        finalArray = ConvertFloatArray(w_results, 4);
        return finalArray;
    }
}