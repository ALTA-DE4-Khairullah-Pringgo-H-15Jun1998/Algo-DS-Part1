def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes(start, count):
    primes = []
    num = start + 1  
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def generate_primes_grid(width, height, start):
    total_primes = width * height
    primes = generate_primes(start, total_primes)
    result = ""
    max_width = len(str(primes[-1]))
    for row in range(height):
        row_primes = primes[row * width: (row + 1) * width]
        result += " ".join(f"{num:{max_width}}" for num in row_primes).strip() + "\n"
    return result

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """