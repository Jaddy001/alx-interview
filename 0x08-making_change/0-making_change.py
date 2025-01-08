#!/usr/bin/python3

def make_change(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): A list of positive integers representing the available coin denominations.
        total (int): The total amount to make change for.

    Returns:
        int: The minimum number of coins needed to make the given total, or
             -1 if the total cannot be made with the given coins.

    Notes:
        - If the total is less than or equal to 0, the function returns 0 as no coins are needed.
        - This implementation uses Dynamic Programming (DP) to find the optimal solution.
        - The DP array `dp` holds the minimum number of coins required for each value from 0 to `total`.
        - If `dp[total]` remains infinity, it means the total cannot be made using the available coins.

    Example:
        >>> make_change([1, 2, 25], 37)
        7

        >>> make_change([1256, 54, 48, 16, 102], 1453)
        -1
    """
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

