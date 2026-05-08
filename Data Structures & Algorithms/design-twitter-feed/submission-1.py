from collections import defaultdict, deque
import heapq
from itertools import chain, count


class Twitter:

    def __init__(self):
        self.tweets = defaultdict(deque)  # userId -> [[timestamp, tweetId], ...]
        self.followers = defaultdict(set)  # follower_id -> [followee_id,...]
        self.count = iter(count())
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweets = self.tweets[userId]
        tweets.appendleft([next(self.count), tweetId])
        if len(tweets) > 10:
            tweets.pop()
        

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []  # 10 tweets with highest timestamp of last tweet
        for followee in chain(self.followers[userId], [userId]):
            tweets = self.tweets[followee]
            if not tweets:
                continue
            if len(min_heap) < 10:
                heapq.heappush(min_heap, tweets)
            else:
                heapq.heappushpop(min_heap, tweets)
        max_heap = [[-tweets[0][0], 0, tweets] for tweets in reversed(min_heap)]  # [[-timestamp, index, tweets], ...]
        result = []
        while max_heap and len(result) < 10:
            neg_timestamp, index, tweets = heapq.heappop(max_heap)
            result.append(tweets[index][1])
            if len(tweets) > index + 1:
                heapq.heappush(max_heap, [-tweets[index+1][0], index+1, tweets])
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
