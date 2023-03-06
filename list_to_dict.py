# Write a function that takes a list of strings as a parameter. The function should return a dictionary of key/value pairs where every key is a word in the list of strings and every value is the length of that word.


def count_str(list):
    dict = {}
    for string in list:
        dict[string] = len(string)
    return print(dict)


count_str(["code", "dog", "momentum"])
count_str(["m", ""])
