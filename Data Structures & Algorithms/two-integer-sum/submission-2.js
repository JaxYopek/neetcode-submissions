class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map();
        let difference = 0;
        for (let i = 0; i < nums.length; i++){
            difference = target - nums[i];
            if (map.has(difference)){
                return [map.get(difference), i];
            }
            else {
                map.set(nums[i],i);
            }
        }
    }
}
