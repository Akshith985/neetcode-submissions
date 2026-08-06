class Solution:
    def canAttendMeetings(self, intervals: list) -> bool:
        
        intervals.sort(key=lambda x: x.start if hasattr(x, 'start') else x[0])
        
        for i in range(1, len(intervals)):
            prev_end = intervals[i - 1].end if hasattr(intervals[i - 1], 'end') else intervals[i - 1][1]
            curr_start = intervals[i].start if hasattr(intervals[i], 'start') else intervals[i][0]
            
           
            if curr_start < prev_end:
                return False
                
        return True