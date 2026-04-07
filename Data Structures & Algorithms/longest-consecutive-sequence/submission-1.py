class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        s = 0
        sequences = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i + 1] == nums[i] + 1:
                s += 1
            else:
                sequences.append(s)
                s = 0
        if s not in sequences:
            sequences.append(s)
        return max(sequences) + 1
            
            
            