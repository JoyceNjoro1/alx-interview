#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """ Generate a list of prime numbers up to n using the Sieve of Eratosthenes """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return primes

def isWinner(x, nums):
    """ Determines the winner of the prime game """
    if not nums or x < 1:
        return None
    
    # Find the maximum number in nums to optimize sieve generation
    max_num = max(nums)
    
    # Get primes up to the largest number in the game using Sieve of Eratosthenes
    primes = sieve_of_eratosthenes(max_num)
    
    # Track wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0
    
    # Simulate each round
    for n in nums:
        available_numbers = list(range(1, n + 1))
        prime_moves = [i for i in range(2, n + 1) if primes[i]]
        maria_turn = True
        while prime_moves:
            # Pick the first available prime
            current_prime = prime_moves[0]
            
            # Remove this prime and its multiples from the list
            available_numbers = [num for num in available_numbers if num % current_prime != 0]
            prime_moves = [num for num in prime_moves if num % current_prime != 0]
            
            # Switch turns
            maria_turn = not maria_turn
        
        # If it's Maria's turn and no primes are left, Ben won, else Maria won
        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1
    
    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

