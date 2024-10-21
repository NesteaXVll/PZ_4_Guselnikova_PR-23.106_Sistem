filename = input("Введите имя файла: ")
N = int(input("Введите количество последних строк: "))
with open(filename, 'r') as file:
    lines = file.readlines()
    line_number = len(lines) - N + 1
    for line in lines[-N:]:
        print(line.rstrip())
        line_number += 1