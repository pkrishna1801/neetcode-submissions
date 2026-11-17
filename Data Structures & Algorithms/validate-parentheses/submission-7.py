class Solution:
    def isValid(self, s: str) -> bool:
        paren = []
        maping_p ={'[':']',
                    '{':'}',
                    '(':')'}
        if len(s) % 2 != 0:
            return False
        for i in s:
            print(i)
            if i == "[" or i =="("  or i =="{":
                paren.append(i)
            else :
                if len(paren) == 0 or maping_p[paren.pop()] != i  :
                    return False
        if len(paren)==0:
            return True
        else:
            return False

        
        