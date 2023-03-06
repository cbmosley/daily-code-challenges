# Write a function that takes a list of elements as a parameter. The function should return a dictionary containing the frequency of each element in the list.
from collections import Counter


def function(list):
    dict = {}
    for element in list:
        if element not in dict:
            dict[element] = 0
        dict[element] += 1

    return dict


print(function(["code", "code", "momentum", 1]))
print(function([0, 0, 0, 0, 0]))


def func(list):
    return dict(Counter(list))


print(func(["code", "code", "momentum", 1]))
