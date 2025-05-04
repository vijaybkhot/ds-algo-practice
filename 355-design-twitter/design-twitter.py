class Twitter:

    # def __init__(self):
    #     self.users = {}
    #     self.tweets = {}
    #     self.timestamp = 0

    # def postTweet(self, userId: int, tweetId: int) -> None:
    #     if userId not in self.tweets:
    #         self.tweets[userId] = []
    #     self.tweets[userId].append((-self.timestamp, tweetId))
    #     self.timestamp += 1
        

    # def getNewsFeed(self, userId: int) -> List[int]:
    #     # Get tweets from all followees and the user
    #     # Get all followeeIds
    #     if userId not in self.tweets:
    #         self.tweets[userId] = []
    #     tweets = list(self.tweets[userId])  # make a copy of the user's tweets
    #     followees = self.users.get(userId, set())

    #     for followee in followees:
    #         tweets.extend(self.tweets.get(followee, []))

    #     heapq.heapify(tweets)
    #     res = []
    #     for i in range(10):
    #         if not tweets:
    #             break
    #         res.append(heapq.heappop(tweets)[1])
    #     return res
        

    # def follow(self, followerId: int, followeeId: int) -> None:
    #     if followerId not in self.users:
    #         self.users[followerId] = set()
    #     self.users[followerId].add(followeeId)
        

    # def unfollow(self, followerId: int, followeeId: int) -> None:
    #     if followerId in self.users:
    #         self.users[followerId].remove(followeeId)


    def __init__(self):
        self.posts = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        # users = [userId] + [user for user in self.followers[userId]]
        # feed_posts = []
        # for user in users:
        #     feed_posts += self.posts[user]
        # heapq.heapify(feed_posts)
        # res = []
        # for i in range(10):
        #     if feed_posts:
        #         post = heapq.heappop(feed_posts)[1]
        #         res.append(post)
        # return res

        users = [userId] + list(self.followers[userId])
        heap = []
        for user in users:
            for tweet in self.posts[user][-10:]:  # Only consider last 10
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)  # Maintain heap size 10
        return [tweetId for _, tweetId in sorted(heap, reverse=True)]

        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].remove(followeeId)
       


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)