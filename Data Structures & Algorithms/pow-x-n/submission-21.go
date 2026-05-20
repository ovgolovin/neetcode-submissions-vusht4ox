func myPow(x float64, n int) float64 {
    if x == 0 {
        return 0
    }
    if n == 0 {
        return 1
    }

    res := 1.0
    power := int(math.Abs(float64(n)))

    for power > 0 {
        if power&1 != 0 {
            res *= x
        }
        x *= x
        power >>= 1
    }

    if n >= 0 {
        return res
    }
    return 1 / res
}