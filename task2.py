filename = input("Введите имя файла: ")

with open(filename, 'r') as file:
    lines = file.readlines()

#for index, line in enumerate(lines, start=1):
#    print(f"{index} {line.rstrip()}")

index = 1
for line in lines:
    print(f"{index} {line.rstrip()}")
    index+=1
