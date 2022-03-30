class Solution {
    public int maxProfit(int[] prices) {
        int minprice = Integer.MAX_VALUE;
	       // A variable to hold the max profit so far
        int maxprofit = 0;
        for (int i = 0; i < prices.length; i++) {
	// If the stock it as at a lower price, we buy it greedily. Just set the variable value
            if (prices[i] < minprice) {
                minprice = prices[i];
	}
	
            else {
	// We know that the current price is greater than the minimum price. 
// We check if we sell at the current day, i.e calculate the difference and see if we get a better profit, we just update the answer. Otherwise Do nothing

		int currentProfit = prices[i] - minprice;
if ( currentProfit > maxprofit){
	// This means that we are getting a better profit, so we just update it
maxprofit = prices[i] - minprice;
			}
		}
        }
        return maxprofit;
	}

        
}
