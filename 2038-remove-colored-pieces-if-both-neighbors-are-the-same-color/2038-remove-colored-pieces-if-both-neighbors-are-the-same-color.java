class Solution {
    public boolean winnerOfGame(String colors) {
        int w = 0;
    int b = 0;

    for(int i = 0; i < colors.length(); i++){
      Character c = colors.charAt(i);
      if(i > 0 && i < colors.length() - 1){
        if(c.equals('A')){
          Character bc = colors.charAt(i-1);
          Character fc = colors.charAt(i+1);
          if((bc.equals(c)) && (fc.equals(c))){
            w += 1;
          }
          // if(ws.contains(i-1)){
          //   w += 1;
          // }
          // ws.add(i);
        } else{
          Character bc = colors.charAt(i-1);
          Character fc = colors.charAt(i+1);
          if((bc.equals(c)) && (fc.equals(c))){
            b += 1;
          }
          // if(bs.contains(i-1)){
          //   b += 1;
          // }
          // bs.add(i);
        }
      }
    }
    // System.out.println("WENDY: " + w);
    // System.out.println("BOB: " + b);
    return w > b;
}
}