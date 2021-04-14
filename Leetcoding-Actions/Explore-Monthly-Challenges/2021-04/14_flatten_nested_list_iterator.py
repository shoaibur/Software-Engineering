# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(a):
            req = []
            for ele in a:
                if ele.isInteger():
                    req.append(ele.getInteger())
                else:
                    req.extend(flatten(ele.getList()))
            return req
        
        self.flatten = flatten(nestedList)
        self.curr = 0
        
    
    def next(self) -> int:
        t = self.flatten[self.curr]
        self.curr+=1
        return t
    
    def hasNext(self) -> bool:
         return self.curr<len(self.flatten)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
