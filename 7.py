k = 3
total_sum = 0

for num in range(1000, 10000):
    if num % k == 0:
        total_sum += num

print(f"total_sum: {total_sum}")