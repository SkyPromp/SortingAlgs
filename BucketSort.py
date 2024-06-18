def BucketSort(data, byte_size=16, bytes_amount=2):
    and_ing = 0

    for _ in range(byte_size):
        and_ing <<= 1
        and_ing |= 1

    buckets = [[] for _ in range(and_ing + 1)]

    for i in range(bytes_amount):
        for val in data:
            last_byte = (val >> (i * byte_size)) & and_ing
            buckets[last_byte].append(val)

        index = 0
        for bucket in buckets:
            while bucket:
                data[index] = bucket.pop(0)
                index += 1

    return data
