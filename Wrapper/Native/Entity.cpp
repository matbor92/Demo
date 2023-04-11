#include "Entity.h"
#include <iostream>
#include <thread>

namespace Core
{
    //constructor
    Calculator::Calculator(float a, float b)
        : m_a(a), m_b(b)
    {
        std::cout << "received numbers" << a << ", " << b << std::endl;
    }

    /*
 * Calculates the sum, difference, product, and quotient of the two numbers using separate threads.
 * Returns an array containing the results of the arithmetic operations.
 *
 * @return A pointer to the results array.
 */

    float* Calculator::calculate()
    {
        std::thread sumThread(&Calculator::sum, this);
        std::thread diffThread(&Calculator::diff, this);
        std::thread prodThread(&Calculator::prod, this);
        std::thread quotThread(&Calculator::quot, this);

        sumThread.join();
        diffThread.join();
        prodThread.join();
        quotThread.join();

        return results_;
    }
    
    void Calculator::sum()
    {
        results_[0] = static_cast<float>(m_a) + static_cast<float>(m_b);
    }
    void Calculator::diff()
    {
        results_[1] = static_cast<float>(m_a) - static_cast<float>(m_b);
    }

    void Calculator::prod()
    {
        results_[2] = static_cast<float>(m_a) * static_cast<float>(m_b);
    }

    void Calculator::quot()
    {
        if (m_b == 0)
        {
            std::cout << " can't divide by 0!!" << std::endl;
            results_[3] = -1;
        }
        else
        {
            results_[3] = static_cast<float>(m_a) / static_cast<float>(m_b);
        }
    }
}

