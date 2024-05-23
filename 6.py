U = int(input("Введите количество страниц, которое студент прочитал в первый день: "))
daily_norm = U
increase_rate = 0.05


for day in range(2, 11):
    daily_norm += daily_norm * increase_rate

total_pages_read = sum([U + U * increase_rate ** i for i in range(10)])

print(f"Студент прочитал {total_pages_read} страниц в книге за 10 дней.")
