# You are given coins of different denominations and a total amount of money. 
# Write a function to compute the number of combinations that make up that amount. 
# You may assume that you have infinite number of each kind of coin.

# Inputs: coins = [1,2,5] and amount = 6

''' Algorithm:
curr_amount = range(0, amount+1)
IF amount >= coin:
    combinations[curr_amount] += combinations[curr_amount - coin]
curr_amount-----> 0  1  2  3  4  5  6
coin [ ]--------> 1  -  -  -  -  -  -
coin [1]--------> 1  1  1  1  1  1  1
coin [2]--------> 1  1  2  2  3  3  4   # combinations[curr_amount] += combinations[curr_amount-coin]
coin [5]--------> 1  1  2  2  2  4  5   # combinations[curr_amount] += combinations[curr_amount-coin]
'''
# Code
def change(amount, coins):
    # Base condition
    combinations = [0] * (amount+1)
    combinations[0] = 1
    # Loop each coin and each amount: O(nm)
    for coin in coins:
        for curr_amount in range(amount+1):
            if curr_amount >= coin:
                combinations[curr_amount] += combinations[curr_amount-coin]
    return combinations[-1]
