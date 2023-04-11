#pragma once
#pragma once
#include "Wrapper.h"
#include "../Native/Core.h"
using namespace System;
namespace CLI
{
    public ref class Calculator : public ManagedObject<Core::Calculator>
    {
    public:

        Calculator(float a, float b);
        array<float>^ calculate();
    };
}