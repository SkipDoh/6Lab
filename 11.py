start_num = 6
end_num = 36
total_sum = 0

for i in range(start_num, end_num+1):
    if i % 2 == 0:
        total_sum += i**3

print(f"total_sum: {total_sum}")