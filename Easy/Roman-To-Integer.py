class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # creating dictionary to hold value translations

        total = 0       # sum / decimal conversion of roman numerals
        prev = 0        # previous roman numeral value (to determine operation)
        for char in s:                 # for each roman numeral
            curr = roman["%s" % char]  # current roman numeral value
            if prev < curr:
                total = total + (curr - 2*prev)  
            else:
                total += curr  
            prev = curr
        
        return total
        
