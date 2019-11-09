class Solution:


    '''
           1 3 3 1 0 
        +  0 1 3 3 1
        =  1 4 6 4 1
    '''
    def getRow(self, rowIndex: int) -> List[int]: 
        row = [1] 
        for i in range(0, rowIndex): 
            row = list(map(lambda x, y: x + y, row + [0], [0] + row)) 
        return row  



