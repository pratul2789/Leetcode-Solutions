class MinStack {
     Stack<Integer> mainStack;
     Stack<Integer> minStack;
    public MinStack() {
        mainStack = new Stack<>();
        minStack = new Stack<>();
        
    }
    
    public void push(int val) {
        if(mainStack.size() == 0){
            //mainStack.push(val);
            minStack.push(val);
        } else{
            int top = minStack.peek();
            if(val < top){
            minStack.push(val);
        } else{
            minStack.push(top);
        }    
        }
        
        mainStack.push(val);
        return;
    }
    
    public void pop() {
        // underflow 
        if(mainStack.size() == 0) return;
        mainStack.pop();
        minStack.pop();
        return;
    }
    
    public int top() {
        //underflow erro check 
        if(mainStack.size() == 0) return -1;
        return mainStack.peek();
    }
    
    public int getMin() {
        if(minStack.size() == 0) return -1;
        return minStack.peek();
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