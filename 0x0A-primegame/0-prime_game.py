#!/usr/bin/python3
"""Prime Game

This module contains the implementation of the Prime Game problem. Maria and Ben take turns choosing a prime number from a set of
consecutive integers starting from 1 up to n. The chosen prime number and its multiples are removed from the set. The player unable
to make a move loses the game. The function determines the winner of each round based on optimal play.

Requirements:
- Python 3.4.3
- PEP 8 style guide (version 1.7.x)
- Executable file"""

def isWinner(x, nums):
    """Determine the winner of the game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the upper limit of each round.

    Returns:
        str or None: Name of the player with the most wins or None if it's a tie.

    Constraints:
        - x and each element of nums will not be larger than 10000.
        - Only prime numbers are considered for moves.
        - Maria always goes first.
        - Both players play optimally."""
    if not nums or x < 1:
        return None

    # Precompute primes up to the maximum number in nums using Sieve of Eratosthenes
    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Precompute the cumulative count of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    """Example test case:

    Input:
        x = 5
        nums = [2, 5, 1, 4, 3]

    Output:
        Winner: Ben

    Run the script to see the output for the example case."""
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

