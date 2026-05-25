class Solution:
    def countSubstrings(self, s: str) -> int:
        n = 2 * len(s) + 1
        rads = [0] * n
        right = center = 0
        count = 0
        for i in range(n):
            rad = min(max(0, right - i), rads[2 * center - i])
            while (
                (i + rad + 1) < n 
                and (i - rad - 1) > -1 
                and (
                    (i + rad + 1) % 2 == 0
                    or s[(i - rad - 1) // 2] == s[(i + rad + 1) // 2]     
                )):
                
                rad += 1
            
            if i + rad > right:
                right = i + rad
                center = i

            rads[i] = rad

            length = rad
            count += (length + 1) // 2

        return count

