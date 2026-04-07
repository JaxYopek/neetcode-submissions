class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashmap = {}
        for string in strs:
            s_string = ''.join(sorted(string))
            if s_string in hashmap:
                hashmap[s_string].append(string)
            else:
                hashmap[s_string] = []
                hashmap[s_string].append(string)
        for anagrams in hashmap.values():
            ans.append(anagrams)
        return ans

