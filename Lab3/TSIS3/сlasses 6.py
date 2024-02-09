class Solution:
    def __init__(self, numbers : list):
        self.numbers = numbers

    def prime_number_filter(self) -> list:
        is_prime = lambda n: all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
        self.numbers = [num for num in self.numbers if is_prime(num)]
        return self.numbers