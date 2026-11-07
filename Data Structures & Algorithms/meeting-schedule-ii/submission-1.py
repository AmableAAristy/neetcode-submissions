"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = sorted([s.start for s in intervals])
        end = sorted([e.end for e in intervals])


        s = 0
        e = 0
        ans = 0
        count = 0

        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            ans = max(ans, count)

        return ans


        
