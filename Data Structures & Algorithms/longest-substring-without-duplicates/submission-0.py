class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        substring = ""
        for i in range(len(s)):
            print(substring)
            if s[i] not in substring:
                substring += s[i]
            else:
                max_length = max(len(substring), max_length)
                substring = ""
                substring += s[i]
        return max_length
