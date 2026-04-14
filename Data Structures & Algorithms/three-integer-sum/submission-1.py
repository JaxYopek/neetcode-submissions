class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        groups = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if target < (nums[j] + nums[k]):
                    k -= 1
                elif target > (nums[j] + nums[k]):
                    j += 1
                else:
                    groups.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
        return groups
