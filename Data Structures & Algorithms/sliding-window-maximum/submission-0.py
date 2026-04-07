class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxNums = []
        for i in range(len(nums) - k + 1):
            maxNum = max(nums[i:i + k])
            maxNums.append(maxNum)
        return maxNums