filenames = input("Введите имена файлов через ПРОБЕЛ: ").split()
output_filename = "data_join.txt"

with open(output_filename, 'w') as output_file:
    for file in filenames:
        with open(file, 'r') as input_file:
            output_file.writelines(input_file.readlines())