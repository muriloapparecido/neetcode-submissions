class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        pot_area = 0
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                height, idx = stack.pop()
                pot_area = height * (i-idx)
                max_area = max(max_area, pot_area)
                start = idx
            stack.append((h, start))
        for height, idx in stack:
            pot_area = height * (len(heights) - idx)
            max_area = max(max_area, pot_area)
        return max_area