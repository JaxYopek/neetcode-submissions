class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search starting from which side?
        l = 0
        r = len(nums) - 1
        minNum = 1001
        while l < r:
            mid = (l + r) // 2
            if nums[l] < nums[r] and nums[mid] < nums[r]:
                #search right half
                r = mid - 1
            else:
                l = mid + 1
            minNum = min(nums[mid], minNum)
        return minNum