# Given a list of numbers and a number k, return any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17

def two_sum(list, k):
    for num1 in list:
        for num2 in list:
            if num1 + num2 == k & num1 != num2:
                return True
    return False


print(two_sum([10, 15, 3, 7], 17))
