import heapq
from collections import defaultdict

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food_rating_map = {}   # food -> (rating, cuisine)
        self.cuisine_q = defaultdict(list)

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_rating_map[f] = [r, c]
            heapq.heappush(self.cuisine_q[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating, cuisine = self.food_rating_map[food]
        self.food_rating_map[food][0] = newRating
        # push new rating
        heapq.heappush(self.cuisine_q[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # pop until valid
        heap = self.cuisine_q[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.food_rating_map[food][0]:
                return food   # ✅ valid top
            heapq.heappop(heap)   # discard stale
