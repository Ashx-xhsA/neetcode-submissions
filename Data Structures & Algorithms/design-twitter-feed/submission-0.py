from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetsMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweetsMap[userId].append([tweetId,self.count])
        
    def getNewsFeed(self, userId: int) -> list[int]:
        h = []
        res = []
        self.followMap[userId].add(userId)
        for user in self.followMap[userId]:
            if user in self.tweetsMap:
                tweetId, time = self.tweetsMap[user][-1]
                l = len(self.tweetsMap[user])
                heapq.heappush(h,[-time,tweetId,user,1,l])
        while len(res) < 10:
            if not h:
                break
            latest = heapq.heappop(h)
            tweetId = latest[1]
            tweetAuthor = latest[2]
            tweetCount = latest[3]
            tweetsTotal = latest[4]

            res.append(tweetId)
            if tweetCount < tweetsTotal:
                tweetToAdd, timeOfTweetToAdd = self.tweetsMap[tweetAuthor][-tweetCount-1]
                heapq.heappush(h,[-timeOfTweetToAdd,tweetToAdd,tweetAuthor,tweetCount+1,tweetsTotal])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)