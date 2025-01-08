#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize the dp array with infinity (meaning that amount can't be made)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: zero coins are needed to make 0

    # Iterate through all coins
    for coin in coins:
        # Update the dp array for each value that can be reached by using the current coin
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total can't be made
    return dp[total] if dp[total] != float('inf') else -1

