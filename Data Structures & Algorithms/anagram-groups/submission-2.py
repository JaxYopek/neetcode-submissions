class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        my_dict = dict()
        for string in strs:
            counts = [0] * 26
            for i in range(0,len(string)):
                counts[ord(string[i]) - ord('a')] += 1
            if tuple(counts) in my_dict:
                my_dict[tuple(counts)].append(string)
            else:
                my_dict[tuple(counts)] = [string]
        
        return list(my_dict.values())


