# Write a function that takes a dictionary as a parameter. Use a loop to return the key associated with the largest value in the dictionary.
# Example:
#Input = {1:100, 2:1, 3:4, 4:10}
#Output = 1
# Input = {“a”:100, “b”:10, “c”:1000}
# Output = “c”


def largest_value(dict):
    value = []
    for key_value in dict.keys():
        value.append(dict[key_value])
    return max(value)


#print(largest_value({1: 100, 2: 1, 3: 4, 4: 10}))

def largest_val(dict):
    return max(dict, key=dict.get)


print(largest_val({1: 100, 2: 1, 3: 4, 4: 10}))


def max_key(my_dictionary):
    largest_key = 0
    largest_value = 0
    for key, value in my_dictionary.items():
        if value > largest_value:
            largest_value = value
            largest_key = key
    return largest_key
