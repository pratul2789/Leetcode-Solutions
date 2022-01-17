class MinStack {
     Stack<Integer> mainStack;
     //Stack<Integer> minStack;
     int min;
    public MinStack() {
        mainStack = new Stack<>();
        //minStack = new Stack<>();
        min = Integer.MAX_VALUE;
    }
    
    public void push(int val) {
        // Check if the curr min is changing
        if(val <= min){
            mainStack.push(min);
            min = val;
        }
        mainStack.push(val);
    }
    
    public void pop() {
        int x = mainStack.pop();
        if(x == min){
            min = mainStack.pop();
        }
    }
    
    public int top() {
        //underflow erro check 
        return mainStack.peek();
    }
    
    public int getMin() {
        return min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */