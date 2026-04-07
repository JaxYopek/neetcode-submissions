class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        char_set = set(s)
        for c in char_set:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                while (r - l + 1) - count > k:
                    #shrink the window
                    if s[l] == c:
                        count -= 1
                    l += 1
                ans = max(r - l + 1,ans)
        return ans
                
