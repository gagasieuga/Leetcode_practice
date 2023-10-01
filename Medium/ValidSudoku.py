from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        #need 3 dicts for 3 types: rows, cols, 3x3 boxes
        #with 3x3 boxes, convert it into likes element into array from 0-2 by divide r and c by 3
        rows = defaultdict(list)
        cols = defaultdict(list)
        subBoxes = defaultdict(list)
        #rows[r] and cols[r] and subBoxs[r][c] is a list 
        for r in range(9):
            for c in range(9):
                if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in subBoxes[(r//3,c//3)]):
                    return False
                if board[r][c] != '.':
                    rows[r].append(board[r][c])
                    cols[c].append(board[r][c])
                    subBoxes[(r//3, c//3)].append(board[r][c])
        return True
        