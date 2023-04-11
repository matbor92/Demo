## Description

This project is a C++ library that contains a calculator class capable of performing basic mathematical operations.
The C++ code is compiled into a static library, which is then utilized in a C# project through a C++/CLI wrapper.
Solution consists of 3 project
-Native, which is a native C++ class
-Wrapper, which a C++/CLI wrapper
-Sandbox, which is a C# project from where you input a data to a Native class, and where the output of Native class is being received by a wrapper.

Operations in C++ are being executed in threads, only for demonstration purposes.


## Requirements

- support for C++/CLI installed in visual studio [link](https://learn.microsoft.com/en-us/cpp/dotnet/dotnet-programming-with-cpp-cli-visual-cpp?view=msvc-170)

## Usage

To run the project, download the repository and ensure that all projects (native, wrapper and sandbox) are in the same directory. 

Remember to ensure that you have the necessary dependencies installed before running the program.


## Output

Output of the project is a sum, difference, product and quotient, of 2 given numbers. Output is displayed in console


## Author

Mateusz Boruch
mateuszboruch1992@gmail.com