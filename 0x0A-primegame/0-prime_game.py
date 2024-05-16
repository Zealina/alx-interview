#!/usr/bin/python3
"""Prime Games Module"""


def isWinner(x, nums):
    """Determine the winner in a prime game"""
    if not x or not nums or type(nums) is not list:
        return

    def sieve(n):
        """Get all the primes in the number"""
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_list = [p for p in range(2, n + 1) if is_prime[p]]
        return prime_list

    max_n = max(nums)
    primes = sieve(max_n)

    def game_winner(n):
        """Determine the winner of each round"""
        p_in_s = [p for p in primes if p <= n]
        maria_turn = True
        while p_in_s:
            current_prime = p_in_s[0]
            p_in_s = [p for p in p_in_s if p % current_prime != 0]
            maria_turn = not maria_turn
        return not maria_turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if game_winner(n):
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
