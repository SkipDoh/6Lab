n = 40
total_sum = 0

for i in range(1, n+1):
    num = 2*i - 1
    total_sum += num**2

print(f"total_sum: {total_sum}")