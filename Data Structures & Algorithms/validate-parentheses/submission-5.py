class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        hashmap = {')' :'(' , ']': '[', '}': '{'}


        for i in s:
            if i not in hashmap:
                stack.append(i)
            else:
                if stack and stack[-1] == hashmap[i]:
                    stack.pop()
                else:
                    return False


        return True if not stack else False
