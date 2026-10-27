class Twitter:

    def __init__(self):
        self.count = 0
        self.users = defaultdict(set) # user_id: [followeeId]
        self.tweetMap = defaultdict(list) #user_id [time, tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # показываем сначала новые затем старые
        res = []
        minHeap = []
        self.users[userId].add(userId)
        if len(self.users[userId]) >= 10:
            maxHeap = []
            for followeeId in self.users[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1 # последний твит
                    count, tweetId = self.tweetMap[followeeId][index] # приоритет и сам твит
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            while maxHeap:
                count, tweetId, followeeId, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-count, tweetId, followeeId, index])
        else:
            for followeeId in self.users[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followeeId]:
            self.users[followerId].remove(followeeId)

# нужна будет очередь для getNewsFeed
# нужно так использовать heap для хранения новостей по приоритету, либо это будет очередь с приоритетом