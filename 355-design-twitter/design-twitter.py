class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # Get tweets from all followees and the user
        # Get all followeeIds
        if userId not in self.tweets:
            self.tweets[userId] = []
        tweets = list(self.tweets[userId])  # make a copy of the user's tweets
        followees = self.users.get(userId, set())

        for followee in followees:
            tweets.extend(self.tweets.get(followee, []))

        heapq.heapify(tweets)
        res = []
        for i in range(10):
            if not tweets:
                break
            res.append(heapq.heappop(tweets)[1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = set()
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)