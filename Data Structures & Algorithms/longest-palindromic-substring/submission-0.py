class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = 2 * len(s) + 1
        rads = [0] * n
        right = center = 0
        best_center = 1
        best_rad = 0
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

            if rad > best_rad:
                best_center = i
                best_rad = rad

        return s[(best_center - best_rad) // 2 : (best_center + best_rad) // 2]



        