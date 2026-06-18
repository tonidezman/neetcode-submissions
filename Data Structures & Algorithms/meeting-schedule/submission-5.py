"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_list = sorted(intervals, key=lambda x: x.start)
        for i in range(len(sorted_list)-1):
            if sorted_list[i].end > sorted_list[i+1].start:
                return False
        return True