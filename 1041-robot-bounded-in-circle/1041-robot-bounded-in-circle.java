class Solution {
    public boolean isRobotBounded(String instructions) {
        int [] d = new int[]{0,1};
    List<String> res = new ArrayList<>();
    int x = 0;
    int y = 0;
    for(char c : instructions.toCharArray()){
      if(c == 'G'){
        x = x + d[0];
        y = y + d[1];
      } else if (c == 'L'){
        int tx = d[1] * -1;
        int ty = d[0]; 
        d[0] = tx;
        d[1] = ty;
      } else{
        int tx = d[1];
        int ty = d[0] * -1; 
        d[0] = tx;
        d[1] = ty;
      }
    }

    if((x == 0 && y == 0) || (!Arrays.equals(d ,new int [] {0,1}))){
      return true;
    }
    return false;
    }
}