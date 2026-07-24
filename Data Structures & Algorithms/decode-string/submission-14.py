class Solution:
    def decodeString(self, s: str) -> str:
        prefixes = []
        multipliers = []

        cur_pref = []
        cur_mult = 0
        for char in s:
            if char.isdigit():
                cur_mult = cur_mult * 10 + int(char)
            elif char == '[':
                prefixes.append(''.join(cur_pref))
                multipliers.append(cur_mult)
                cur_pref = []
                cur_mult = 0
            elif char == ']':
                cur_pref = [prefixes.pop() + ''.join(cur_pref) * multipliers.pop()]
                cur_mult = 0 
            else:
                cur_pref.append(char)
        return ''.join(cur_pref)