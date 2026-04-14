class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(nums[l],nums[mid],nums[r])
            if nums[l] == target:
                return l
            if nums[mid] <= target and target < nums[r]:
                r = mid
            else:
                l = mid + 1
            
        return -1