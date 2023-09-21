"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    
    list = []
    next_number = 0
    while len(list) < number_of_primes:
        if is_prime(next_number):
            list.append(next_number)
        
        next_number = next_number + 1
    return list
