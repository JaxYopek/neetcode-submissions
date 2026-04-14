class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_freq = dict()

        for c in s1:
            if c in s1_freq:
                s1_freq[c] += 1
            else:
                s1_freq[c] = 1
        for i in range(len(s2) - len(s1)):
            s2_freq = dict()
            for j in range(len(s1)):
                if s2[i - j] in s2_freq:
                    s2_freq[s2[i - j]] += 1
                else:
                    s2_freq[s2[i - j]] = 1
            if s2_freq == s1_freq:
                return True
        return False
                
