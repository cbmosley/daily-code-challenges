def containsDuplicate(nums):
    set_nums = set()
    for num in nums:
        if num in set_nums:
            return True
        set_nums.add(num)
    return False


print(containsDuplicate([1, 2, 1]))
