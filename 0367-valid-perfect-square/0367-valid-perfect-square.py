class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = num**0.5
        return x%1 ==0
        