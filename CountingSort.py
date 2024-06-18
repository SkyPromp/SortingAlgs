from random import randint


min_i = 0
max_i = 10

data = [randint(min_i, max_i) for _ in range(int(1e6))]
range_data = [0] * (max_i - min_i + 1)

for val in data:
    range_data[val] += 1

index = 0
val = min_i
for amount in range_data:
    for _ in range(amount):
        data[index] = val
        index += 1

    val += 1

print("done")
