"""
Демонстрационная программа.
Открывает sample.fasta и выводит все записи из файла.
"""

from fasta_reader import FastaReader

path = "sample.fasta"

print()
print(f"Чтение файла: {path}")
print()

reader = FastaReader(path)

# Вывод всех записей
print("Записи в файле:")

total = 0
for seq in reader.read():
    total += 1
    print(f"{seq.__str__()}")
    print()

print(f"Всего записей: {total}")