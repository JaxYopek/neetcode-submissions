class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequent = []
        freq = Counter(nums)
        nums = sorted(nums, key = lambda x: -freq[x])
        for n in nums:
            if n not in most_frequent:
                most_frequent.append(n)
            if len(most_frequent) == k:
                return most_frequent