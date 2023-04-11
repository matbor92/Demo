using System;
using CLI;
namespace Sandbox
{
    class Program
    {

        static void Main(string[] args)
        {
            //Creating a native class object
            Calculator e = new Calculator(20, 35);
            //receving table of floats, created in Native project,
            //and corverted to C# table, by wrapper
            float[] myArray = new float[4];
            myArray = e.calculate();
            //Displaying the results
            Console.WriteLine(string.Join(", ", myArray));
            Console.Read();
        }
    }
}