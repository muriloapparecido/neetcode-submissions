class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenInCol = defaultdict(set)
        seenInBox = defaultdict(set)
        for r, row in enumerate(board):
            seenInRow = set()
            for c, col in enumerate(row):
                if col == ".":
                    continue
                if col in seenInRow or col in seenInCol[c]:
                    return False
                seenInRow.add(col)
                seenInCol[c].add(col)
                box = (r // 3) * 3 + (c // 3) 
                if col in seenInBox[box]:
                    return False
                seenInBox[box].add(col)
        return True
        