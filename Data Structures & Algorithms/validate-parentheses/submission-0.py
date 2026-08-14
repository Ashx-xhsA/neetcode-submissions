class Solution:
    def matches(self,rp,p):
        if rp == ']':
            return p == '['
        elif rp == ')':
            return p == '('
        else:
            return p == '{'

    def isValid(self, s: str) -> bool:
        l = []
        for p in s:
            if p == '{' or p == '(' or p =='[':
                l.append(p)
            else:
                if not l:
                    return False
                else:
                    if self.matches(p,l[-1]):
                        l.pop()
                    else:
                        return False
        return not l
        
        