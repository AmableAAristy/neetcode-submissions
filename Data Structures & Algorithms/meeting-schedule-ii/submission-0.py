"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #lets try the two array methods

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        count = 0
        ans = 0

        s = 0
        e = 0

        while s < len(intervals):
            if end[e] > start[s]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            ans = max(ans, count)

        return ans



