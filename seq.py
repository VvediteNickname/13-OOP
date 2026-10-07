"""
Модуль для работы с одной биологической последовательностью.

Содержит класс Seq, который хранит одну запись (последовательность + заголовок)
и умеет определять её тип (нуклеотидная / белковая).
"""

#: Множество символов нуклеотидного алфавита (ДНК и РНК).
#: Включает стандартные A, T, G, C, U и вырожденные IUPAC-коды.
NUCLEOTIDE_ALPHABET = set("ATGCUNRYSWKMBDHV")

#: Множество символов белкового алфавита (20 стандартных аминокислот
#: плюс редкие X, B, Z, U, O).
PROTEIN_ALPHABET = set("ARNDCQEGHILKMFPSTWYVXBUOZ")


class Seq:
    """
    Хранит одну биологическую последовательность и её заголовок.

    Объект Seq — это одна запись из FASTA-файла: заголовок (без символа ``>``)
    и сама последовательность. Пробельные символы удаляются автоматически,
    регистр приводится к верхнему.

    Атрибуты класса не описаны как публичные — доступ к данным идёт через
    свойства ``sequence`` и ``header``, а тип последовательности — через
    свойство ``alphabet``.
    """

    def __init__(self, sequence: str, header: str = "") -> None:
        """
        Создаёт объект Seq.

        Args:
            sequence: последовательность символов. Пробельные символы
                (пробелы, переводы строк, табы) удаляются автоматически,
                регистр приводится к верхнему.
            header: заголовок FASTA-записи (без символа ``>``). По умолчанию
                пустая строка.

        Raises:
            ValueError: если ``sequence`` пустая строка.
        """

        if sequence == "":
            raise ValueError("Последовательность не может быть пустой")

        self.__sequence = sequence.upper().replace(" ", "").replace("\n", "")
        self.__header = header.strip()

    # ---------- Свойства ----------

    @property
    def sequence(self) -> str:
        """
        Сама последовательность.

        Returns:
            str: последовательность в верхнем регистре без пробельных символов.
        """
        return self.__sequence

    @property
    def header(self) -> str:
        """
        Заголовок FASTA-записи.

        Returns:
            str: заголовок без символа ``>`` и без пробелов по краям.
        """
        return self.__header

    @property
    def alphabet(self) -> str:
        """
        Определяет тип последовательности.

        Сначала проверяется нуклеотидный алфавит (он уже), затем белковый.
        Если ни один не подошёл — возвращается ``"unknown"``.

        Returns:
            str: ``"nucleotide"``, ``"protein"`` или ``"unknown"``.
        """
        seq_set = set(self.__sequence)
        if seq_set <= NUCLEOTIDE_ALPHABET:
            return "nucleotide"
        if seq_set <= PROTEIN_ALPHABET:
            return "protein"
        return "unknown"

    # Методы 

    def __len__(self) -> int:
        """
        Возвращает длину последовательности.

        Returns:
            int: количество символов в последовательности.
        """
        return len(self.__sequence)

    def __str__(self) -> str:
        """
        Человекочитаемое представление объекта.

        Returns:
            str: многострочная строка с заголовком, длиной и алфавитом.
        """
        return (
            f"Заголовок:          {self.__header}\n"
            f"Длина:              {len(self)}\n"
            f"Алфавит:            {self.alphabet}"
        )

    def __repr__(self) -> str:
        """
        Техническое представление объекта для отладки.

        Returns:
            str: однострочное представление с заголовком, алфавитом и длиной.
        """
        return (
            f"Seq(header={self.__header!r}, "
            f"length={len(self)}), "
            f"alphabet={self.alphabet}"
        )