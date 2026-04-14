class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let maxProfit = 0;
        let left = 0;
        let right = 1;
        while (right <= prices.length - 1){
            let buy = prices[left];
            let sell = prices[right];
            let currentProfit = sell - buy;
            maxProfit = Math.max(maxProfit, currentProfit)
            if (buy > sell){
                right++;
                left++;
            }
            else {
                right++;
            }
        }
        return maxProfit;
    }
}
