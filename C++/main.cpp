#include <cmath>
#include <vector>
#include "platform_time"
#include <tuple>
#include <iostream>

class PID
{
public:
    double kp, ki, kd, i, last_t = NAN, last_e = NAN;

    double process(double setpoint, double process)
    {
        double
            error = setpoint - process,
            t = pgm_time_s(),
            p = kp * error,
            i = ki * (i + (error * (last_t == NAN ? 0 : t - last_t))),
            d = kd * (last_t == NAN || last_e == NAN ? 0 : (error - last_e) / (t - last_t));
        last_e = error;
        last_t = t;
        return p + i + d;
    }
};

double f(double x)
{
    return -1 * x * (x - 4);
}

void test()
{
    using std::cout;
    using std::vector;
    using coordinate = std::pair<double, double>;
    constexpr double x_0 = 0;

    vector<coordinate> coordinates;

    for (double x = x_0, y = f(x_0); x < 5; x += 0.1, y = f(x_0))
    {
        coordinates.emplace_back(x, y);
        cout << '(' << x << ", " << y << ")\n";
    }
}

int main()
{
    using std::cout;
    cout.precision(10);
    while (true)
    {
        double t = time(NULL);
        cout << t << '\n';
    }
    return 0;
}