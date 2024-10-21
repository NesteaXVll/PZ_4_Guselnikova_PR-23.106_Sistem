filename = input("Введите имя файла: ")
N = int(input("Введите количество строк: "))
with open(filename, 'r') as file:
     line_number = 1
     for line in file:
         if line_number > N:
             break
         print(line.rstrip())
         line_number += 1