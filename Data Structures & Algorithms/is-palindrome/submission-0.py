import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.translate(str.maketrans("", "", string.punctuation))
        s = "".join(s.split())
        return s[::-1] == s