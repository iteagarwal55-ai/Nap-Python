def harmonic_sum(n):
    """Calculates the sum 1 + 1/2 + 1/3 + ... + 1/N"""
    if n < 1:
        return 0
    return sum(1 / i for i in range(1, n + 1))

# Example usage:
N = 10
result = harmonic_sum(N)
print(f"The harmonic sum for N = {N} is: {result:.4f}")
