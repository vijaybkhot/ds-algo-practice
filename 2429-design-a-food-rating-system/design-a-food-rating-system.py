# class Node:
#     def __init__(self, food, cuisine, rating, nxt=None, prev=None):
#         self.food = food
#         self.cuisine = cuisine
#         self.next = nxt
#         self.prev = prev
#         self.rating = rating

# class FoodRatings:

#     def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
#         self.food_node_map = {}
#         self.cuisine_list = {}

#         for i in range(len(foods)):
#             food = foods[i]
#             cuisine = cuisines[i]
#             rating = ratings[i]


#             new_node = Node(food, cuisine, rating)
#             if cuisine not in self.cuisine_list:
#                 head = Node('head', cuisine, float('inf'))
#                 tail = Node('tail', cuisine, float('-inf'))
#                 head.next = tail
#                 tail.prev = head
#                 self.cuisine_list[cuisine] = head
            
#             head_node = self.cuisine_list[cuisine]
#             first_node = self.cuisine_list[cuisine].next
#             head_node.next, first_node.prev = new_node, new_node
#             new_node.prev, new_node.next = head_node, first_node

#             # Put the new_node in correct position based on its rating
#             while new_node.next.rating > new_node.rating:
#                 self.exchange_pos_forward(new_node)
            
#             while new_node.next.rating == new_node.rating and  new_node.next.food < new_node.food:
#                 self.exchange_pos_forward(new_node)
            
#             self.food_node_map[food] = new_node
            
#     def exchange_pos_forward(self, node):
#         nxt = node.next
#         left = node.prev
#         right = nxt.next
#         left.next = nxt
#         nxt.prev = left
#         nxt.next = node
#         node.prev = nxt
#         node.next = right
#         right.prev = node
    
#     def exchange_pos_backward(self, node):
#         prev = node.prev
#         left = prev.prev
#         right = node.next
#         left.next = node
#         node.prev = left
#         node.next = prev
#         prev.prev = node
#         prev.next = right
#         right.prev = prev

#     def changeRating(self, food: str, newRating: int) -> None:
#         if food not in self.food_node_map:
#             return
#         node = self.food_node_map[food]
#         if newRating > node.rating:
#             node.rating = newRating
#             while node.prev.rating < node.rating:
#                 self.exchange_pos_backward(node)
#             while node.prev.rating == node.rating and node.prev.food > node.food:
#                 self.exchange_pos_backward(node)
        
#         elif newRating < node.rating:
#             node.rating = newRating
#             while node.next.rating > node.rating:
#                 self.exchange_pos_forward(node)
            
#             while node.next.rating == node.rating and  node.next.food < node.food:
#                 self.exchange_pos_forward(node)

        

#     def highestRated(self, cuisine: str) -> str:
#         return self.cuisine_list[cuisine].next.food

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating_map = {}   # (rating, cuisine)
        self.cuisine_q = {}

        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]

            self.food_rating_map[food] = [rating, cuisine]

            if cuisine not in self.cuisine_q:
                self.cuisine_q[cuisine] = []
            
            heapq.heappush(self.cuisine_q[cuisine], (-rating, food, cuisine))


    def changeRating(self, food: str, newRating: int) -> None:
        _, cuisine = self.food_rating_map[food]
        heapq.heappush(self.cuisine_q[cuisine], (-newRating, food, cuisine))
        self.food_rating_map[food][0] = newRating


    def highestRated(self, cuisine: str) -> str:
        while self.cuisine_q[cuisine] and self.cuisine_q[cuisine][0][0] != (-1 * self.food_rating_map[self.cuisine_q[cuisine][0][1]][0]):
            heapq.heappop(self.cuisine_q[cuisine])

        return self.cuisine_q[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)