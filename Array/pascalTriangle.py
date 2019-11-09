class Solution:
    def generate(self, numRows: int): 
        out = [] 
        for i in range(numRows): 
            out.append([1]*(i+1)) # initialize all lines
            if i>1: 
                for j in range(1,i): # eliminate 1st and last 1
                    out[i][j] = out[i-1][j-1] + out[i-1][j] # 
        return out 


    '''
           1 3 3 1 0 
        +  0 1 3 3 1
        =  1 4 6 4 1
    '''
    def generate1(self, numRows: int): 

        res = [[1]] 
        for i in range(1, numRows): 
            res.append(list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))) 
        return res if numRows else [] 
