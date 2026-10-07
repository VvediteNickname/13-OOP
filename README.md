# Classes for FASTA

Библиотека на Python для работы с FASTA-файлами.

## Что умеет

- **`Seq`** — хранит одну FASTA-запись (заголовок + последовательность).
  - Определяет длину последовательности.
  - Определяет тип: `nucleotide`, `protein` или `unknown`.
  - Красиво выводится через `print()`.
- **`FastaReader`** — читает FASTA-файл.
  - Проверяет, что файл соответствует формату (`validate`).
  - Итеративно отдаёт записи через генератор (эффективно для больших файлов).

## Установка

Клонируйте репозиторий и установите зависимости для разработки:

```bash
git clone https://github.com/VvediteNickname/Classes-for-FASTA.git
cd Classes-for-FASTA

python -m venv .venv
source .venv/bin/activate       # Linux / macOS
.venv\Scripts\activate          # Windows

pip install -e ".[dev]"
```

Если не нужны тесты и документация — достаточно клонировать и запускать из папки проекта.

## Быстрый старт

```python
from fasta_reader import FastaReader

reader = FastaReader("sample.fasta")

if not reader.validate():
    print("Файл не соответствует формату FASTA")
else:
    for seq in reader.read():
        print(seq)
        print("-" * 40)
```

**Пример вывода:**

```
Последовательность: NC_000001.11 Homo sapiens chromosome 1
Длина:              60
Алфавит:            nucleotide
----------------------------------------
Последовательность: sp|P00698|LYSC_CHICK Lysozyme C
Длина:              129
Алфавит:            protein
----------------------------------------
```

## Использование классов отдельно

### `Seq` — одна запись

```python
from seq import Seq

seq = Seq("atgc atgc", "id1 описание")
print(seq.sequence)   # ATGCATGC  (пробелы убраны, регистр приведён)
print(seq.header)     # id1 описание
print(seq.alphabet)   # nucleotide
print(len(seq))       # 8
```

### `FastaReader` — чтение файла

```python
from fasta_reader import FastaReader

reader = FastaReader("sample.fasta")
print(reader.validate())   # True / False

for seq in reader.read():
    print(seq.identifier, len(seq), seq.alphabet)
```

## Требования к FASTA-файлу

- Каждая запись начинается со строки с символом `>` в начале.
- После заголовка идёт последовательность (возможно, на нескольких строках).
- Пустые строки игнорируются.
- Символы последовательности — буквы, без пробелов и цифр.

Пример:

```
>NC_000001.11 Homo sapiens chromosome 1
ATGCATGCATGC
ATGCATGCATGC
>sp|P00698|LYSC_CHICK Lysozyme C
MKALIVLGLVLLSVTVQGK
```

## Запуск демо

```bash
python demo.py
```

## Тесты

```bash
pytest -v
```

## Документация

Собранная HTML-документация лежит в `docs/_build/html/`.
Откройте `docs/_build/html/index.html` в браузере.

Чтобы пересобрать:

```bash
cd docs
sphinx-build -b html . _build/html
```

## UML-диаграмма

Диаграмма классов — в `UML_diagram.png`.

## Лицензия

MIT — см. файл `LICENSE`.