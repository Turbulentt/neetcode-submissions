class Solution:
    def isValid(self, s: str) -> bool:
        openStack = []
        for x in s:
            if x == '(' or x == '{' or x == '[':
                openStack.append(x)
            if x == ')':
                if openStack and openStack[-1] == '(':
                    openStack.pop()
                else:
                    return False
            if x == '}':
                if openStack and openStack[-1] == '{':
                    openStack.pop()
                else:
                    return False
            if x == ']':
                if openStack and openStack[-1] == '[':
                    openStack.pop()
                else:
                    return False
        
        return not bool(openStack)