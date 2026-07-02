class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5 = 0
        count_10 = 0

        for bill in bills:
            if bill == 5:
                count_5 += 1
            elif bill == 10:
                if count_5 == 0:
                    return False
                count_10 += 1
                count_5 -= 1
            elif bill == 20:
                if count_5 == 0:
                    return False
                elif count_10 > 0:
                    count_5 -= 1
                    count_10 -= 1
                elif count_10 == 0:
                    if count_5 < 3:
                        return False
                    else:
                        count_5 -= 3
        
        return True
        