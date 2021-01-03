# Problem 1: Square root of an integer
* Algorithmic idea: Binary search until result^2 < n < (result+1)^2.
* Complexity: O(log n) in time and O(1) in space because of binary search.
* Alternative solution would be, start from 1 and compare its square with n. Repeat the procedure until the square exceeds n. Runtime of this approach would be O(sqrt(n)).


# Problem 2: Search in a rotated sorted array
* Algorithmic idea: Binary search
  * Check which of left and right side is sorted based on the mid point calculated in the binary search.
  * Continue searching in the appropriate side (left/right) by checking where the target falls in.
* Complexity: O(log n) in time and O(1) in space because of binary search.


# Problem 3: Rearrange array digits to maximize sum
* Algorithmic idea:
  * Maximum sum of two numbers is produced by two maximum numbers. Maximum numbers start with maximum digits. So, sort the array in descending order and form two arrays using every other digit.
  * Convert two arrays into two integers, which are the maximum numbers that give maximum sum.
* Complexity:
  * Time: O(n log n) because Python's .sort() uses sample sort with this runtime. Other runtimes, i.e., traversing the array and converting arrays into integer numbers are O(n).
  * Space: O(n) because the total space required for two additional arrays is O(n/2 + n/2)


# Problem 4: Dutch national flag problem
* Algorithmic idea:
  * Traverse the array with pointer i. Two additional pointers (pos0 and pos2) indicate first and last positions of the array, respectively. If the value at the ith position is 0, swap that with the value at pos0 position. If the value at the ith position is 2, swap that with the value at pos2 position. Update the value of pointers after each check.
* Complexity: O(n) in time and O(1) in space, because it requires one pass to traverse the array and no additional space is used.


# Problem 5: Autocomplete with Trie
* Algorithmic idea:
  * TrieNode class - node in the Trie; includes insert and suffixes methods. Suffixes method is recursive to find/autocomplete the word based on the current input.
  * Trie class - contains root node; includes insert and find methods. Insert method is used to insert any new word into the Trie and find method is used to find the suffixes.
* Complexity: Runtime is O(n*m) for each of insert, where n is the length word and m is the average of trienodes encountered down the trie. Space complexity is also O(n * m) to store the words/characters.


# Problem 6: Min/Max in an unsorted integer array
* Algorithmic idea: Traverse the array and check if the current element is lower/higher than the current min/max value. If so, update current min/max value.
* Complexity: O(n) in time and O(1) space, because only one pass (traverse) is sufficient and no additional space is used except some variables.


# Problem 7: Request routing in a web server with a Trie
* Algorithmic idea:
  * RouteTrie class - stores the routes and their associated handlers; includes to insert and find paths.
  * RouteTrieNode class - similar to traditional Trie Node, except now it contains a handler instead of is_word; includes method to insert path.
  * Router class - wrap the Trie and handler; includes methods to add handlers, lookup and path splitting.

* Complexity:
  * O(n * m) in time, as in problem 5.
  * O(n * m) in space, as in problem 5.
