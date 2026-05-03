class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stacks = {}
        self.maxCount = 0

    def push(self, val: int) -> None:
        valCount = self.freq.get(val, 0) + 1
        self.freq[val] = valCount
        if valCount > self.maxCount:
            self.maxCount = valCount
            self.stacks[valCount] = []
        self.stacks[valCount].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCount].pop()
        self.freq[res] -= 1
        if not self.stacks[self.maxCount]:
            self.maxCount -= 1
        return res
        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()