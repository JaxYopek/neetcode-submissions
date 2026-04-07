class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        hashmap = dict()

        for i in range(0,len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            elif s[i] in hashmap:
                hashmap[s[i]]+= 1
            if t[i] not in hashmap:
                hashmap[t[i]] = -1
            elif t[i] in hashmap:
                hashmap[t[i]] -= 1
        
        for val in hashmap.values():
            print(val)
            if val != 0:
                return False
        return True
                

        

        