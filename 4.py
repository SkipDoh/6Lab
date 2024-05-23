X = 10
daily_distance = X
total_distance = X
for day in range(2, 8):
    daily_distance *= 1.1
    total_distance += daily_distance
print(f"Спортсмен пробежит за неделю: {total_distance} км")
