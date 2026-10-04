"""
Демонстрационная программа.
Открывает sample.fasta и выводит все записи из файла.
"""

from fasta_reader import FastaReader

path = "sample.fasta"

print("=" * 60)
print(f"Чтение файла: {path}")
print("=" * 60)

reader = FastaReader(path)

# Вывод всех записей
print("Записи в файле:")
print("-" * 60)

total = 0
for seq in reader.read():
    total += 1
    print(f"  {seq}")

print("-" * 60)
print(f"Всего записей: {total}")