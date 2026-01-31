class Solution:
    def isPalindrome(self, s: str) -> bool:
        x= s.lower().replace(" ", "")
        y=""
        for i in x :
            if i.isalnum():
                y += i
        if y == y[::-1]:
            return True
        else:
            return False
        