#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds."""
    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0
    # Find the maximum number in nums to set sieve limit
    n = max(nums)
    
    # Sieve of Eratosthenes to determine prime numbers up to n
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    
    # Simulate each round
    for num in nums:
        # Count how many primes are there up to `num`
        primes_count = sum(primes[0:num + 1])
        
        # Maria wins if the prime count is odd, Ben wins if it's even
        if primes_count % 2 == 0:
            bens_wins += 1
        else:
            marias_wins += 1

    # Determine the overall winner
    if marias_wins > bens_wins:
        return "Maria"
    elif bens_wins > marias_wins:
        return "Ben"
    else:
        return None

