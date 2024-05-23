A = float(input("Введите размер ежемесячной стипендии: "))
B = float(input("Введите размер расходов на проживание: "))
growth_rate = 0.03

total_money_needed = 0

for month in range(1, 11):
    total_money_needed += B
    B *= (1 + growth_rate)

total_money_needed += A


print(f"Общая сумма денег, необходимая на учебный год: {total_money_needed} руб.")
