sample_dic = {
    (1, 30),
    (2, 22),
}


def min_val_two(sample_dic):
    return min(sample_dic, key=sample_dic.get)


print("Key for min value:", (min_val_two(sample_dic)))
