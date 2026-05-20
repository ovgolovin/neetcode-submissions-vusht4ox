class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;

        double res = 1;
        long power = abs((long)n);

        while (power) {
            res *= 1 + (x - 1) * (power % 2);
            x *= x;
            power /= 2;
        }

        return n >= 0 ? res : 1 / res;
    }
};