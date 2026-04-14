class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s) - 1
        left = 0
        while left <= right:
            if  not s[left].isalnum():
                left += 1
            if not s[right].isalnum():
                right -= 1
            print(f"{s[left]}, {s[right]}")
            if s[left].lower() != s[right].lower():
                return False
            right -= 1
            left += 1
        return True