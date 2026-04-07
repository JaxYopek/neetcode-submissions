class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for i in range(0, len(nums)):
            remainder = target - nums[i]
            if remainder in nums_dict:
                return [nums_dict[remainder], i]
            else:
                nums_dict[nums[i]] = i
            