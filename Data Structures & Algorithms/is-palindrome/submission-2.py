class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr = ''

        for c in s:
            if c.isalnum():
                newStr += c.lower()


        for i in range(len(newStr) // 2):
            if newStr[i] != newStr[-1 -i]:
                return False

        return True