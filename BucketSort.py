from random import randint


data = [randint(0x0, 0xffffff) for _ in range(int(1000))]

byte_size = 8
bytes_amount = 4
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

print("done")
