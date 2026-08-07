class Solution:
    def minMeetingRooms(self, intervals: list) -> int:
        if not intervals:
            return 0
        
        starts = sorted([x.start if hasattr(x, 'start') else x[0] for x in intervals])
        ends = sorted([x.end if hasattr(x, 'end') else x[1] for x in intervals])
        
        used_rooms = 0
        end_ptr = 0
        
        for start in starts:
            
            if start >= ends[end_ptr]:
                end_ptr += 1
            else:
                
                used_rooms += 1
                
        return used_rooms