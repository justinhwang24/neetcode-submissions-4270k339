class StockSpanner:

    def __init__(self):
        self.data = []

    def next(self, price: int) -> int:
        res = 1
        curr = len(self.data) - 1
        while curr >= 0 and self.data[curr] <= price:
            res += 1
            curr -= 1
        self.data.append(price)
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)