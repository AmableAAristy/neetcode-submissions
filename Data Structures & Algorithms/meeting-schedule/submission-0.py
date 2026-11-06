"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x : x.start)

        for i in range(len(intervals) - 1):
            j = i + 1
            i1 = intervals[i].end
            j1 = intervals[j].start

            if i1> j1:
                return False
        return True