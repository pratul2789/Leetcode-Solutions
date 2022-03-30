class Solution {
    public int maxProfit(int[] prices) {
        int tot = 0;
        
        for(int i = 1; i < prices.length; i++){
            if(prices[i] > prices[i-1]){
                tot = tot + prices[i] - prices[i-1];
            }
        }
        
        return tot;
    }
}