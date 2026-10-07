class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hashmap = {')' : '(' , 
        '}' : '{',
        ']' : '['}


        for c in s:
            if c in hashmap and not stack:
                return False

            if c in hashmap:
                if stack.pop() != hashmap[c]:
                    return False 

            if c not in hashmap:
                stack.append(c)
            



        return not stack
