filename = input("Введите имя входного файла: ")
N = int(input("Введите максимальное количество строк: "))

with open(filename, 'r') as file:
    lines = file.readlines()

file_count = 1

for i in range(0, len(lines), N):
    filename_new = f"{file_count}.txt"
    with open(filename_new, 'w') as file_new:
        file_new.writelines(lines[i:i + N])
    file_count += 1