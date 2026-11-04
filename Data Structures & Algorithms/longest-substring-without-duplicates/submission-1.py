class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        ans = 0

        l = 0
        r = 0
        while r <= len(s) - 1:
            #if it can expand
            if s[r] not in hashset:
                hashset.add(s[r])
                r += 1
                ans = max(ans, r - l)
                                
            #if it cannot Expand
            else:
                while s[r] in hashset:
                    if s[l] in hashset:
                        hashset.remove(s[l])
                    l += 1
        return ans