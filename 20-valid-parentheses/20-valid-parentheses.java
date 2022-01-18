class Solution {
    public boolean isValid(String s) {
        if(s == null || s.length() == 0){
            return true;
        }
        
        Stack<Character> st = new Stack<>();
        
        HashMap<Character,Character> hm = new HashMap<>();
        
        hm.put(')','(');
        hm.put(']','[');
        hm.put('}','{');
        
        for(int i = 0; i < s.length();i++){
            char br = s.charAt(i);
            //System.out.println(hm.containsKey(br));
            if(!hm.containsKey(br)){
                //System.out.println("hmm");
                st.push(br);
            }else{
                if(st.isEmpty()){
                    return false;
                }
                char op = st.pop();
                //System.out.println(op);
                if(hm.get(br) != op){
                    return false;
                }
            }
        }
        return st.size() == 0;
    }
}