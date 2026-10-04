import math


NUCLEOTIDE_ALPHABET = set("ATGCUNRYSWKMBDHV")
PROTEIN_ALPHABET = set("ARNDCQEGHILKMFPSTWYVXBUOZ")


class Seq:
    """
    Хранит одну биологическую последовательность и её заголовок.
    """

    def __init__(self, sequence: str, header: str = ""):

        if sequence == "":
            raise ValueError("Последовательность не может быть пустой")
        
        self.__sequence = sequence.upper().replace(" ", "").replace("\n", "")
        self.__header = header.strip()

    # Свойства

    @property
    def sequence(self) -> str:
        return self.__sequence

    @property
    def header(self) -> str:
        return self.__header

    @property
    def alphabet(self) -> str:
        """Определяет тип: 'nucleotide' или 'protein'."""
        chars = set(self.__sequence)
        if chars <= NUCLEOTIDE_ALPHABET:
            return "nucleotide"
        if chars <= PROTEIN_ALPHABET:
            return "protein"

    # Методы

    def __len__(self) -> int:
        return len(self.__sequence)

    def __str__(self) -> str:
        return f"Seq(length={len(self)}, alphabet={self.alphabet})"

    def __repr__(self) -> str:
        return f"Seq(header={self.__header!r}, length={len(self)})"