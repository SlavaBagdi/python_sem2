number = int(input("Введите количество чисел в списке: "))
sum = 0
d = {i: 3*i + 1 for i in range(1, number+1)}
print(f"Для n = {number}: {d}")


def sequence(number):
    return [round((1 + 1 / i)**i, 2) for i in range(1, number + 1)]


print(f'Список для {number} чисел =', sequence(number))
