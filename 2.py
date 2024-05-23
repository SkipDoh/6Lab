
start_amoebas = int(input("Введите количество одноклеточных амёб: "))
amoebas = start_amoebas
for hours in range(3, 25, 3):
    amoebas *= 2
    print(f"Через {hours} часов будет {amoebas} амеб(ы)")
print(f"Изначально было {start_amoebas} амёб")
