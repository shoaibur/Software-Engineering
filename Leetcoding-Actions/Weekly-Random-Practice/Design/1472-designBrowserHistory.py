class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.currIndex = 0

    def visit(self, url: str) -> None:
        self.currIndex += 1
        self.history = self.history[:self.currIndex]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.currIndex -= steps
        self.currIndex = max(self.currIndex, 0)
        return self.history[self.currIndex]

    def forward(self, steps: int) -> str:
        self.currIndex += steps
        self.currIndex = min(self.currIndex, len(self.history)-1)
        return self.history[self.currIndex]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
