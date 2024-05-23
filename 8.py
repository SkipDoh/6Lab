total_sum = 0

for num in range(7, 38):
    if num % 2 != 0:
        total_sum += num**3

print(f"total_sum: {total_sum}")