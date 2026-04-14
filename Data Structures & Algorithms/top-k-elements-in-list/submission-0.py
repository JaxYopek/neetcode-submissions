class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        for n in nums:
            if nums.count(n) == k:
                return n