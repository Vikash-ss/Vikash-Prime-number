def is_prime(n):
    """Returns True if the given number is prime, else False"""

    # 0 and 1 are not prime numbers
    if n < 2:
        return False

    # Check if the number is divisible by any number between 2 and its square root
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is not divisible by any number between 2 and its square root, then it's prime
    return True
