"""
Демонстрационная программа.
Открывает sample.fasta и выводит все записи из файла.
"""

from fasta_reader import FastaReader

def demo(path): 
    print()
    print(f"Чтение файла: {path}")
    print()

    reader = FastaReader(path)

    # Вывод всех записей
    print("Записи в файле:")
    print()

    total = 0
    for seq in reader.read():
        total += 1
        print(f"{str(seq)}")
        print()

    print(f"Всего записей: {total}")

print(
    "Демонстрационная программа. Выберите файл для проверки работы классов: "
    "sample.fasta -- три коротких последовательности;   "
    "uniprot.fasta -- 25 белковых последовательностей;   "
    "Human_DNA_fragment.fasta -- фрагмент ДНК человека;   "
    "test.txt -- для проверки ошибок;   "
    )
path = input()
demo(path)