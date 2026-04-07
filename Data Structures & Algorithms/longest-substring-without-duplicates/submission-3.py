class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # go until you have substring then find repeat (take length) -> move left until no more repeat 
        # -> start again -> take max
        ans, l = 0,0 
        substring = set()
        for r in range(len(s)):
            while s[r] in substring:
                substring.discard(s[l])
                l += 1
            substring.add(s[r])
            ans = max(len(substring),ans)


            
        
        return ans



