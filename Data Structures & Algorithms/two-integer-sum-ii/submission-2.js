class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let left = 0;
        let right = numbers.length - 1;
        while (left < right){
            let sum = numbers[left] + numbers[right]
            if (sum === target){
                return [numbers[left], numbers[right]];
            }
            else if (sum < target){
                left++;
            
            }
            else {
                right--;
            }
        }
    }
}
