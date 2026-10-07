"""
Модуль для чтения FASTA-файлов.

Содержит класс FastaReader, который проверяет формат файла и
итеративно отдаёт объекты Seq по одной записи (генератор).
"""

import os
from seq import Seq


class FastaReader:
    """
    Читает FASTA-файл и возвращает объекты Seq.

    Класс не хранит последовательности — он лишь умеет их извлекать
    из файла. Для проверки формата используется метод :meth:`validate`,
    для итерации по записям — метод :meth:`read`.
    """

    def __init__(self, path: str) -> None:
        """
        Создаёт читатель для указанного файла.

        Args:
            path: путь к FASTA-файлу (строка).
        """
        self.__path = path

    def validate(self) -> bool:
        """
        Проверяет, что файл соответствует формату FASTA.

        Достаточное условие: файл существует, не пуст, и первая непустая
        строка начинается с символа ``>``.

        Returns:
            bool: ``True``, если файл похож на FASTA, иначе ``False``.
        """
        if not os.path.exists(self.__path) or not os.path.isfile(self.__path):
            return False

        try:
            with open(self.__path) as f:
                for line in f:
                    if line.strip():
                        return line.startswith(">")
                return False
        except OSError:
            return False

    def read(self):
        """
        Генератор: возвращает объекты Seq по одному.

        Файл читается построчно. Строки, начинающиеся с ``>``, считаются
        заголовками и начинают новую запись. Остальные строки добавляются
        к текущей последовательности. Пустые строки пропускаются.

        Yields:
            Seq: очередная запись из файла.

        Raises:
            FileNotFoundError: если файл по указанному пути не существует.
            ValueError: если файл не соответствует формату FASTA
                (не начинается с ``>``, содержит последовательность
                без заголовка).

        Example:
            >>> reader = FastaReader("sample.fasta")
            >>> for seq in reader.read():
            ...     print(len(seq), seq.alphabet)
        """
        if not os.path.exists(self.__path):
            raise FileNotFoundError(f"Файл не найден: {self.__path}")

        if not self.validate():
            raise ValueError(
                f"Файл не соответствует формату FASTA: {self.__path}"
            )

        header = None
        sequence = []

        with open(self.__path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                if line.startswith(">"):
                    if header is not None:
                        yield Seq("".join(sequence), header)
                    header = line[1:].strip()
                    sequence = []
                else:
                    if header is None:
                        raise ValueError(
                            "Файл не соответствует формату FASTA: "
                            "последовательность без заголовка"
                        )
                    sequence.append(line)

            if header is not None:
                yield Seq("".join(sequence), header)