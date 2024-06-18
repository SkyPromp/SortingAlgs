def CountingSort(data, min_val, max_val):
    range_data = [0] * (max_val - min_val + 1)

    for val in data:
        range_data[val] += 1

    index = 0
    val = min_val
    for amount in range_data:
        for _ in range(amount):
            data[index] = val
            index += 1

        val += 1

    return data
