impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        if x == 0.0 {
            return 0.0;
        }
        if n == 0 {
            return 1.0;
        }

        let mut res = 1.0;
        let mut base = x;
        let mut power = (n as i64).abs();

        while power > 0 {
            if power & 1 == 1 {
                res *= base;
            }
            base *= base;
            power >>= 1;
        }

        if n >= 0 { res } else { 1.0 / res }
    }
}