class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search starting from which side?
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[l] < nums[r]:
                #search right half
                r = mid
            else:
                l = mid + 1
        return nums[l]