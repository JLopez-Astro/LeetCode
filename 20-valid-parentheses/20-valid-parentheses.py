class Solution:
    def isValid(self, s: str) -> bool:
        openB = ['(','{','[']
        brack = []
        for c in s:
            if c in openB:
                brack.append(c)
            elif c == ')' and len(brack) != 0 and brack[-1] == '(':
                brack.pop()
            elif c == '}' and len(brack) != 0 and brack[-1] == '{':
                brack.pop()
            elif c == ']' and len(brack) != 0 and brack[-1] == '[':
                brack.pop()
            else:
                return False
        return brack == []