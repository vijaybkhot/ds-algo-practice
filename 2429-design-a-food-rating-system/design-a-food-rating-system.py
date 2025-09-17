from sortedcontainers import SortedList
from collections import defaultdict

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food_rating_map = {}
        self.cuisine_map = defaultdict(lambda: SortedList())

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_rating_map[f] = [r, c]
            self.cuisine_map[c].add((-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating, cuisine = self.food_rating_map[food]
        self.cuisine_map[cuisine].remove((-oldRating, food))
        self.cuisine_map[cuisine].add((-newRating, food))
        self.food_rating_map[food][0] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_map[cuisine][0][1]
