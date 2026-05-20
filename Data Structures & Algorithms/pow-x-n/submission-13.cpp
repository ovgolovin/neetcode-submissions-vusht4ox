class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;

        double res = 1;
        long power = abs((long)n);

        while (power) {
            ldiv_t division = std::div(power, 2L);
            res *= 1 + (x - 1) * division.rem;
            x *= x;
            power = division.quot;
        }

        return n >= 0 ? res : 1 / res;
    }
};