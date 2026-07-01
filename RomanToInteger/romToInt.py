class Solution(object):
    def romanToInt(self, s):
        roman = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000
                }

        n = len(s)
        total = 0

        for i in range(n):
            value = roman.get(s[i])
            nextValue = roman.get(s[i + 1]) if i + 1 < n else 0

            if nextValue > value:
                total -= value
            else:
                total += value
                
        return total