class Solution {
    public int rob(int[] choco) {
        int answer = 0;
    if(choco == null || choco.length == 0){
      return answer;
    }

    int [][] dp = new int [choco.length+1][2];

    for(int i = 1; i <= choco.length; i++){
      //if we choose the current chocolate
      dp[i][0] = choco[i-1] + dp[i-1][1];
      //if we dont choose, choose the max of previous step
      dp[i][1] = Math.max(dp[i-1][0],dp[i-1][1]);
    }

    return Math.max(dp[choco.length][0],dp[choco.length][1]);
    }
}