class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None: # wrong modify 
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        [2nd bit, 1st bit] = [next state, current state]

        - 00  dead (next) <- dead (current)
        - 01  dead (next) <- live (current)  
        - 10  live (next) <- dead (current)  
        - 11  live (next) <- live (current) 
        
        board == 1, lives == 2 or 3: 01 -> 11 
        board == 0, lives == 3: 00 -> 10 
        cur board[i][j] & 1 
        nex board[i][j] >> 1
        '''
        # n <= 1 live -> dead 01 
        # n == 2 or 3 live -> live 11
        # n >= 4 live -> dead 01
        # n == 3 dead -> live 10
        # dead 00 
        # 8 neibor: vert, hori, diag 
        if len(board) == 0 return; 
        m, n = len(board), len(board[0]) 
        
        def liveN(i, j): 
            lives = 0 
            for x in range(max(i - 1, 0), min(i + 2, m)): # nine gram
                for y in range(max(j - 1, 0), min(j + 2, n)): 
                    lives += board[x][y]&1 
            lives -= board[i][j]&1 
            return lives

        for i in range(0, m): 
            for j in range(0, n): 
                lives = liveN(i, j)
                # init 2nd bit is 0 
                # only change l2l and d2l 
                if board[i][j] == 1 and (lives == 2 or lives == 3): 
                    board[i][j] = 3 #11 
                elif board[i][j] == 0 and lives == 3: 
                    board[i][j] == 2 #10 
        
        for i in range(0, m): 
            for j in range(0, n): 
                board[i][j] >>= 1 
                

        
'''
public void gameOfLife(int[][] board) {
    if (board == null || board.length == 0) return;
    int m = board.length, n = board[0].length;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int lives = liveNeighbors(board, m, n, i, j);

            // In the beginning, every 2nd bit is 0;
            // So we only need to care about when will the 2nd bit become 1.
            if (board[i][j] == 1 && lives >= 2 && lives <= 3) {  
                board[i][j] = 3; // Make the 2nd bit 1: 01 ---> 11
            }
            if (board[i][j] == 0 && lives == 3) {
                board[i][j] = 2; // Make the 2nd bit 1: 00 ---> 10
            }
        }
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            board[i][j] >>= 1;  // Get the 2nd state.
        }
    }
}

public int liveNeighbors(int[][] board, int m, int n, int i, int j) {
    int lives = 0;
    for (int x = Math.max(i - 1, 0); x <= Math.min(i + 1, m - 1); x++) {
        for (int y = Math.max(j - 1, 0); y <= Math.min(j + 1, n - 1); y++) {
            lives += board[x][y] & 1;
        }
    }
    lives -= board[i][j] & 1;
    return lives;
}
'''