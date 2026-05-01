from collections import defaultdict
import heapq

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Feed:

    class FeedReader:

        def __init__(self, latest):
            self.latest = latest
        
        def __lt__(self, other):
            return self.latest.val[0] < other.latest.val[0]
        
        def has_post(self):
            return self.latest is not None

        def get_post(self):
            post = self.latest.val[1]
            self.latest = self.latest.left
            return post

    def __init__(self, max_size):
        self.old = None
        self.new = None
        self.size = 0
        self.max_size = max_size

    def post(self, tweetId, timestamp):
        if self.size == 0:
            self.old = Node((timestamp, tweetId))
            self.new = self.old
            self.size = 1
            return

        new_post = Node((timestamp, tweetId))
        new_post.left = self.new
        self.new.right = new_post
        self.new = new_post
        self.size += 1

        if self.size > self.max_size:
            to_delete = self.old
            self.old = to_delete.right
            self.old.left = None
            self.size -= 1
            del to_delete
    
    def get_reader(self):
        return Feed.FeedReader(self.new)

class Twitter:

    def __init__(self):
        self.max_feed = 10
        self.feeds = defaultdict(lambda: Feed(self.max_feed))
        self.follows = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feeds[userId].post(tweetId, self.timestamp)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        follows = [userId]
        follows.extend(self.follows[userId])
        follow_feed_readers = [self.feeds[follow].get_reader() for follow in follows]
        follow_feed_readers = [reader for reader in follow_feed_readers if reader.has_post()]
        heapq.heapify_max(follow_feed_readers)
        news_feed = []
        for _ in range(self.max_feed):
            if not follow_feed_readers:
                break
            feed = heapq.heappop_max(follow_feed_readers)
            news_feed.append(feed.get_post())
            if feed.has_post():
                heapq.heappush_max(follow_feed_readers, feed)
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return None
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return None
        self.follows[followerId].discard(followeeId)
