from collections import defaultdict,deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        q = deque()
        d = defaultdict(list)
        ind = defaultdict(int)
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                d[ingredients[i][j]].append(recipes[i])
                ind[recipes[i]] += 1
                
        for i in supplies:
            q.append(i)
            
        #vis = set(recipes)
        
        
        ans = []
        
        while q:
            item = q.popleft()
            
            # if item in vis:
            #     ans.append(item)
                
            for i in d[item]:
                ind[i] -= 1
                if ind[i] == 0:
                    ans.append(i)
                    q.append(i)
                    
        return ans