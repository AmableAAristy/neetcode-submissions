class Solution:

    def encode(self, strs: List[str]) -> str:
        joinedStrings = ''
        for string in strs:
            wordL = len(string)

            tempString = str(wordL) + '#'

            joinedStrings += tempString + string

        return joinedStrings

        

    def decode(self, s: str) -> List[str]:

        ans = []
        numAsString = ''
        i = 0
        while i < len(s):
            
            if s[i] != '#':
                numAsString += s[i]
                i += 1   
            else:
                num = int(numAsString)
                string = ''
                for j in range(i + 1, i + 1 + num):
                    string += s[j]  
                ans.append(string)
                i += num + 1
                numAsString = ''
                

                
        return ans


