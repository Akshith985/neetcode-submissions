from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.time = 0  # Global clock ticker to track tweet recency
        self.tweets = defaultdict(list)  # userId -> list of [time, tweetId]
        self.follow_map = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Decrement time so that newer tweets have a smaller value (floats to top of min-heap)
        self.time -= 1
        self.tweets[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        
        # A user always sees their own tweets in their feed
        followees = self.follow_map[userId] | {userId}
        
        for f_id in followees:
            if f_id in self.tweets:
                # Grab the index of the absolute newest tweet for this user (the last element)
                index = len(self.tweets[f_id]) - 1
                time, tweetId = self.tweets[f_id][index]
                
                # Push into heap: (timestamp, tweetId, user_id, index of next tweet to fetch)
                min_heap.append((time, tweetId, f_id, index - 1))
                
        heapq.heapify(min_heap)
        while min_heap and len(res) < 10:
            time, tweetId, f_id, next_idx = heapq.heappop(min_heap)
            res.append(tweetId)
            
            # If this user has older tweets left, push the next one into the heap
            if next_idx >= 0:
                next_time, next_tweetId = self.tweets[f_id][next_idx]
                heapq.heappush(min_heap, (next_time, next_tweetId, f_id, next_idx - 1))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
