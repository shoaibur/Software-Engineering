# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path, handler): # O(n*m) in time
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for item in path:
            if item not in node.children:
                node.children[item] = RouteTrieNode()
            node = node.children[item]
        node.handler = handler
        
    def find(self, path):  # O(n) in time
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for item in path:
            if item not in node.children:
                return None
            node = node.children[item]
        return node.handler
        
        
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}
        
    def insert(self, path):  # O(1) in time
        # Insert the node as before
        self.children[path] = RouteTrieNode()
#         
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie = RouteTrie(handler)
        self.not_found_handler = not_found_handler
        
    def add_handler(self, path, handler): 
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_item = self.split_path(path)
        self.routeTrie.insert(path_item, handler) # O(n) in time
        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_item = self.split_path(path)
        handler = self.routeTrie.find(path_item)# O(n) in time
        if handler is None:
            return self.not_found_handler
        return handler

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path = path.strip('/') # O(n) in space
        if path:
            return path.split('/')
        return []
# 

# Test cases
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

import unittest
class HTTPRouterTest(unittest.TestCase):

    def test_case1(self):
        test = router.lookup('/')
        expected = 'root handler'
        self.assertEqual(test, expected)
    
    def test_case2(self):
        test = router.lookup('/home')
        expected = 'not found handler'
        self.assertEqual(test, expected)
        
    def test_case3(self):
        test = router.lookup('/home/about')
        expected = 'about handler'
        self.assertEqual(test, expected)
        
    def test_case4(self):
        test = router.lookup('/home/about/')
        expected = 'about handler'
        self.assertEqual(test, expected)
        
    def test_case5(self):
        test = router.lookup('/home/about/me')
        expected = 'not found handler'
        self.assertEqual(test, expected)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.005s

# OK

