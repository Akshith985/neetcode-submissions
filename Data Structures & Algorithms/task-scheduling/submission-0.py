from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. Count the frequencies of each task
        counts = Counter(tasks)
        
        # 2. Build a Max-Heap using negative frequencies
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)
        
        # 3. Create the cool-down queue: pairs of (remaining_count, available_time)
        cooldown_queue = deque()
        
        time = 0
        
        # Keep running the CPU while there are tasks left to execute or cool down
        while max_heap or cooldown_queue:
            time += 1
            
            # --- STEP 1: PROCESS AN AVAILABLE TASK ---
            if max_heap:
                # Pop the most frequent task (remember it's negative)
                count = heapq.heappop(max_heap) + 1  # Adding 1 brings it closer to 0
                
                # If it still needs to be run again in the future, send it to cool down
                if count < 0:
                    cooldown_queue.append((count, time + n))
            
            # --- STEP 2: CHECK THE COOL-DOWN UNLOCKS ---
            # If the task at the front of the queue has finished cooling down,
            # release it back into the active max-heap!
            if cooldown_queue and cooldown_queue[0][1] == time:
                available_count, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, available_count)
                
        return time