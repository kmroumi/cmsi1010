# ----------------------------------------------------------------------
# This is the file functions_cardio.py

# The intent is to give you practice writing functions.

# Complete the functions below.
# Remove this comment when you have completed the functions.
# ----------------------------------------------------------------------

def is_odd(n):
    return n % 2 != 0


def median_of_three(a, b, c):
   return sorted([a, b, c])[1]


def is_palindrome(s):
    return s == s[::-1]


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def count_of_latin_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def longest_string(strings):
    """
    Returns the longest string from a list of strings.

    If there are multiple strings with the same maximum length, return
    the first one encountered.
    """
    # replace the pass statement with your code
    pass


def word_frequencies(s):
    """
    Returns a dictionary with the frequency of each word in the string s.
    The keys of the dictionary are the words, and the values are the
    number of times each word appears in the string.

    A word is defined as a sequence of characters separated by spaces.
    You can implement this function using the split method.
    """
    # replace the pass statement with your code
    pass


assert is_odd(3) == True
assert is_odd(8) == False
assert is_odd(-3) == True
assert is_odd(-8) == False

assert median_of_three(1, 2, 3) == 2
assert median_of_three(1, 3, 2) == 2
assert median_of_three(2, 1, 3) == 2
assert median_of_three(2, 3, 1) == 2
assert median_of_three(3, 1, 2) == 2
assert median_of_three(3, 2, 1) == 2

assert factorial(5) == 120
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(6) == 720
assert factorial(20) == 2432902008176640000

assert is_palindrome("racecar") == True
assert is_palindrome("hello") == False
assert is_palindrome("madam") == True
assert is_palindrome("python") == False

assert count_of_latin_vowels("hello world") == 3
assert count_of_latin_vowels("aeiou") == 5
assert count_of_latin_vowels("xyz") == 0
assert count_of_latin_vowels("Python programming") == 4
assert count_of_latin_vowels("Aeiou") == 5

assert longest_string(["apple", "banana", "cherry"]) == "banana"
assert longest_string(["cat", "dog", "elephant"]) == "elephant"
assert longest_string(["short", "longer", "longest"]) == "longest"
assert longest_string(["a", "ab", "abc"]) == "abc"
assert longest_string(["one", "two", "three", "four"]) == "three"

assert word_frequencies("hello world hello") == {'hello': 2, 'world': 1}
assert word_frequencies("a b a c b a") == {'a': 3, 'b': 2, 'c': 1}
assert word_frequencies("test test test") == {'test': 3}
assert word_frequencies("") == {}