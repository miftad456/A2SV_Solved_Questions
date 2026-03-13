class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in s:
            if i=='*':
                if stack:
                    stack.pop()
            
            elif i.isalnum():
                stack.append(i)
        return ''.join(stack)
        
        