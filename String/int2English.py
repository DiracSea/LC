class Solution:
    def numberToWords(self, num: int) -> str: 
        # brute force 
        if num == 0: 
            return "Zero" 
        ten = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
               "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
               "Eighteen", "Nineteen"] 
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"] 
        thousand = ["", "Thousand", "Million", "Billion"]     
        
        def word(n): 
            if n == 0: 
                return "" 
            elif n < 20: 
                return ten[n] + " " 
            elif n < 100: 
                return tens[n//10] + " " + word(num%10) 
            else: 
                return ten[n//100] + " Hundred " + word(num%100)
            
        s = ""
        i = 0 
        while num > 0: 
            if num%1000 != 0: 
                s = word(num%1000) + thousand[i] + " " + s 
            num //= 1000 
            i += 1 
        return s.strip()  

        
    def numberToWords1(self, num: int) -> str: 
        # recursive 
        if num == 0: 
            return "Zero" 
        ten = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
               "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
               "Eighteen", "Nineteen"] 
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"] 
        thousand = ["Thousand", "Million", "Billion"]     
        
        def word(n): 
            if n < 20: 
                return [ten[n]] 
            elif n < 100: 
                return [tens[n//10]] +  word(n%10) 
            elif n < 1000: 
                return [ten[n//100]] + ["Hundred"] + word(n%100) 
            for p, w in enumerate(thousand, 1): 
                if n < 1000**(p+1): 
                    return word(n//1000**p) + [w] + word(n%1000**p)
            
        return ' '.join(x for x in word(num) if x is not '').strip() 

        
                
            