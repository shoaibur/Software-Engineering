class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.data.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        complement = {}
        for num in self.data:
            if value - num in complement:
                return True
            complement[num] = True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
