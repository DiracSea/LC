class Solution:
    def isNumber(self, s: str) -> bool:
        # trick 
        try:
            float(s)
            return True
        except :
            return False
    # iterate test case 
    def isNumber1(self, s: str) -> bool:
        # flag site 
        s = s.strip() 
        point = False 
        epow = False 
        num = False 
        numE = True 
        for i in range(len(s)): 
            if '0' <= s[i] and s[i] <= '9': 
                num = True 
                numE = True
            elif s[i] == '.': 
                if epow or point: 
                    return False 
                point = True
            elif s[i] == 'e': 
                if epow or not num: 
                    return False 
                numE = False 
                epow = True 
            elif s[i] == '-' or s[i] == '+': 
                if i != 0 and s[i-1] != 'e': 
                    return False 
            else: 
                return False 
        return num and numE 
    
    # remove wrong 

    # DFA 
    def isNumber2(self, s: str) -> bool:
        # DFA 
        state = 0 
        s = s.strip() 
        for i in s: 
            if i == '+' or i == '-': 
                if state == 0: state = 1 
                elif state == 4: state = 6 
                else: return False 
            elif i >= '0' and i <= '9': 
                if state <= 2: 
                    state = 2 
                elif state == 3: 
                    state = 3  
                elif state <= 6: 
                    state = 5  
                elif state == 7: 
                    state = 8 
                elif state == 8: 
                    state = 8 
                else: 
                    return False 
            elif i == '.': 
                if state <= 1: 
                    state = 7 
                elif state == 2: 
                    state = 3 
                else: 
                    return False 
            elif i == 'e': 
                if state == 2 or state == 3 or state == 8: 
                    state = 4 
                else: 
                    return False 
            else: 
                return False 
        return state == 2 or state == 3 or state == 5 or state == 8 