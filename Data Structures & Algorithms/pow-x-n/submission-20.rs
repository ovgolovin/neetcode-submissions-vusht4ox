impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        if n == 0 {
            return 1.0;
        }

        let mut res = 1.0;
        let mut base = x;
        let mut power = (n as i64).abs();

        while power > 0 {
            res *= 1.0 + (base - 1.0) * (power & 1) as f64;
            base *= base;
            power >>= 1;
        }

        if n >= 0 { res } else { 1.0 / res }
    }
}