from seq import Seq

class FastaReader:
    def __init__(self, path):
        self.__path = path

    def read(self):
        """Генератор: возвращает объекты Seq по одному."""

        header = None
        sequence = []

        with open(self.__path) as f:
            for line in f:
                line = line.strip()

                if line.startswith(">"):
                    if header is not None:
                        yield Seq("".join(sequence), header)
                    header = line[1:].strip()
                    sequence = []
                else:
                    sequence.append(line)

            if header is not None:
                yield Seq("".join(sequence), header)