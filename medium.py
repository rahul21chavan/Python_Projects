import re

def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

# Example usage:
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("race a car"))  # Output: False

def get_even_numbers_desc(nums):
    return sorted([num for num in nums if num % 2 == 0], reverse=True)

# Example
print(get_even_numbers_desc([1, 2, 3, 4, 5, 6, 7, 8]))  # Output: [8, 6, 4, 2]


def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

# Example
print(find_primes_in_range(10, 30))  # Output: [11, 13, 17, 19, 23, 29]
