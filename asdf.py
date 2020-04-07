def array_sum(array):
    my_sum = 0

    for sub_arr in array:
        my_sum += min(sub_arr)

    return my_sum

test_arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
print(array_sum(test_arr))