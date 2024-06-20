def get_primes(nums):
    for n in nums:
        if is_prime(n):
            yield n

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True
        
print(list(get_primes([15])))