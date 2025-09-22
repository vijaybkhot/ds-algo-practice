class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        from sortedcontainers import SortedSet
        self.available = {}
        self.rented = SortedSet()
        self.priceMap = {}
        for shop, movie, price in entries:
            if movie not in self.available:
                self.available[movie] = SortedSet()
            self.available[movie].add((price, shop))
            self.priceMap[(shop, movie)] = price

    def search(self, movie: int) -> list[int]:
        res = []
        if movie in self.available:
            for price, shop in self.available[movie]:
                res.append(shop)
                if len(res) == 5: break
        return res

    def rent(self, shop: int, movie: int) -> None:
        price = self.priceMap[(shop, movie)]
        self.available[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.priceMap[(shop, movie)]
        self.rented.discard((price, shop, movie))
        self.available[movie].add((price, shop))

    def report(self) -> list[list[int]]:
        res = []
        for price, shop, movie in self.rented:
            res.append([shop, movie])
            if len(res) == 5: break
        return res