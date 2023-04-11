#pragma once
namespace Core
{
    class Calculator
    {
    public:
    private:
        float m_a, m_b;
        float results_[4] = { 0.0f };
    public:
        Calculator(float a, float b);

        float* calculate();
        void sum();
        void diff();
        void prod();
        void quot();
    };
}