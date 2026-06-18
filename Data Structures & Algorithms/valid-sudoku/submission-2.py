class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenCol = defaultdict(set)
        seenBox = defaultdict(set)
        for r,row in enumerate(board):
            seenRow = set()
            for c,value in enumerate(row): 
                if value == ".":
                    continue
                if value in seenCol[c] or value in seenRow: 
                    return False
                seenCol[c].add(value)
                seenRow.add(value)
                box = (r // 3) * 3 + (c // 3)
                if value in seenBox[box]:
                    return False
                seenBox[box].add(value)

        return True
