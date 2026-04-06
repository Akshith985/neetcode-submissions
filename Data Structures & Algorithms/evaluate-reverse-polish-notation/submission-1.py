class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       l=[]
       k=['+','-','*','/']
       for i in tokens:
        if i in k:
            right=l.pop()
            left=l.pop()
            if i=='/':
                l.append(int(left/right))
            elif i=='-':
                l.append(left-right)
            elif i=="+":
                l.append(left+right)
            elif i=="*":
                l.append(right*left)
        else: 
            l.append(int(i))
       return l[-1]