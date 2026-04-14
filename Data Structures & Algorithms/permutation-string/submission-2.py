from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letter_freq = Counter(s1)
        print(letter_freq)
        if len(s1) > len(s2):
            return False
        for i in range(len(s2) - len(s1)):
            print(Counter(s2[i: i + len(s1)]))
            if Counter(s2[i: i + len(s1)]) == letter_freq:
                return True
        return False
            
