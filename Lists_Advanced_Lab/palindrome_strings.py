def palindrome_words(is_palindrome: list) -> list:
    """Returns a list containing all the found palindromes in the sequence"""
    # We use a list comprehension to filter words that are the same forwards and backwards
    return [data for data in is_palindrome if data == data[::-1]]


# Read the sequence of words and the specific palindrome to count
is_palindrome_words = input().split()
compare_word = input()

# Get the list of all palindromes from the input
result = palindrome_words(is_palindrome_words)

# Count how many times the specific palindrome appears in the result list
repetition = result.count(compare_word)

# Print the list of all found palindromes
print(result)
# Print the count of the searched palindrome
print(f"Found palindrome {repetition} times")
