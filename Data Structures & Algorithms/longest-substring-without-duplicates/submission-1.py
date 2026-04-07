class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letterSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in letterSet:
                letterSet.remove(s[l])
                l += 1
            letterSet.add(s[r])
            res = max(res, r - l + 1)
        return res
