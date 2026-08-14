class Solution:
    def operate(self,l,r,o):
        if o == '+':
            return l+r
        elif o == '-':
            return l-r
        elif o == '*':
            return l*r
        else:
            return int(l/r)

    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operactors = {'+', '-', '*','/'}
        for o in tokens:
            if o in operactors:
                r = stk.pop()
                l = stk.pop()
                stk.append(self.operate(l,r,o))
            else:
                stk.append(int(o))
        return stk.pop()



        