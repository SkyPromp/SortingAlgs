from random import randint


data = [randint(0x0, 0xfff) for _ in range(int(1e7))]

byte_size = 16  # 8
bytes_amount = 2  # 4
and_ing = 0

for _ in range(byte_size):
    and_ing <<= 1
    and_ing |= 1

for i in range(bytes_amount):
    output = [0] * len(data)
    prefix_sum = [0] * (and_ing + 1)

    # Calculate frequencies
    for val in data:
        last_byte = (val >> (i * byte_size)) & and_ing
        prefix_sum[last_byte] += 1

    # Calculate prefix sum
    for j in range(1, len(prefix_sum)):
        prefix_sum[j] += prefix_sum[j - 1]

    # Swap numbers
    for val in data[::-1]:
        last_byte = (val >> (i * byte_size)) & and_ing
        prefix_sum[last_byte] -= 1
        output[prefix_sum[last_byte]] = val

    data = output

#print(data)
print("done")
