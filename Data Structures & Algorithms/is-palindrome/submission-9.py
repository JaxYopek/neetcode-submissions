class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        right = len(s) - 1
        left = 0
        while left <= right:
            print(f"1{s[left], s[right]}")
            while not s[left].isalnum():
                left += 1
            while not s[right].isalnum():
                right -= 1
            print(f"2{s[left], s[right]}")
            if s[left].lower() != s[right].lower():
                return False

            right -= 1
            left += 1
        return True