import itertools

numbers = [10, 15, 3, 7]
k = 10


def k_add(numbers, k):
    for num in numbers:
        for num2 in numbers:
            if num + num2 == k and num != num2:
                print(num, num2)
                return True
    return False


print(k_add(numbers, k))


def one_pass(numbers, k):
    for x in itertools.combinations(numbers, 2):
        if sum(x) == k:
            print(x)
            return True
    return False


print(one_pass(numbers, k))
