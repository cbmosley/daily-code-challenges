# John and Jane just learned about palidromes and want to know if a given string has a palindrome in it. A palindrome is a string that reads the same forwards and backwards. For example, “bob”, “racecar”, and “noon” are all palindromes, while “cat”, “dog”, and “nascar” are not palindromes.
# John knows JavaScript and Jane knows Python. John has written a function in JavaScript called `isPalindrome` that takes in a string and returns Palindromes found: and the given palidroms found in the string and `None` otherwise. Jane has written a function in Python called `is_palindrome` that takes in a string and returns Palindromes found: and the given palidroms found in the string and `None` otherwise.
# John and Jane want to test their functions so they swap functions and test each other’s functions. It looks like they both have bugs in their code. Can you help them fix their code?
# Try to fix the code without changing the function names or the function parameters. You can add helper functions if you need to. We always want to stay in the same spirit as John and Janes, so try to resolve the bugs in the language you are least familiar with.
# Bouns:
# - Once you have fixed the code can you find the additional issue in the code?


def is_palindrome(string):

    string = ''.join(filter(str.isalnum, string)).lower()
    if string:
        return string == string[::-1]


while True:
    sentence = input("Please enter a sentence: ")

    if sentence:
        break
    print("Error: Please enter a non-empty sentence.")


words = sentence.split()

print(words)


palindromes = []
for word in words:
    if is_palindrome(word):
        palindromes.append(word)
if not palindromes:
    print("No palindromes found.")
else:
    print("Palindromes found:")
    for palindrome in palindromes:
        print(palindrome)
print(palindromes)
