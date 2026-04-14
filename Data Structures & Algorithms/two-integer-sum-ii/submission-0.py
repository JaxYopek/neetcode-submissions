class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0 
        j = len(numbers) - 1
        while True:
            k = numbers[j] + numbers[i]
            if target < k:
                j -= 1
            elif target > k:
                i += 1
            else:
                return[numbers[i],numbers[j]]