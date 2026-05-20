func myPow(x float64, n int) float64 {
    if n == 0 {
        return 1
    }

    res := 1.0
    power := int(math.Abs(float64(n)))

    for power > 0 {
        res *= 1.0 + (x - 1.0) * float64(power & 1);
        x *= x
        power >>= 1
    }

    if n >= 0 {
        return res
    }
    return 1 / res
}