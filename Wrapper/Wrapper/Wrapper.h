#pragma once

using namespace System;
using namespace System::Runtime::InteropServices;

// Template class for managing native objects in managed code
namespace CLI
{

    template<class T>
    public ref class ManagedObject
    {
    protected:
        T* m_Instance;
    public:
        ManagedObject(T* instance)
            : m_Instance(instance)
        {
        }
        // Virtual destructor that deletes the native object when the managed object is destroyed
        virtual ~ManagedObject()
        {
            if (m_Instance != nullptr)
            {
                delete m_Instance;
            }
        }
        // Finalizer that deletes the native object when the garbage collector collects the managed object
        !ManagedObject()
        {
            if (m_Instance != nullptr)
            {
                delete m_Instance;
            }
        }
        // Getter method for the native object
        T* GetInstance()
        {
            return m_Instance;
        }
    };
}
static const char* string_to_char_array(String^ string)
{
    const char* str = (const char*)(Marshal::StringToHGlobalAnsi(string)).ToPointer();
    return str;
}

array<float>^ ConvertFloatArray(float* cppFloatArray, int length)
{
    array<float>^ csharpFloatArray = gcnew array<float>(length);

    for (int i = 0; i < length; i++)
    {
        csharpFloatArray[i] = cppFloatArray[i];
    }

    return csharpFloatArray;
}
