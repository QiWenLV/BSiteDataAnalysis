from persist import persist


class CsvPersist(persist.IPersist):

    def __init__(self, mode):
        super().__init__()
        self.mode = mode

    def write(self):
        pass

    def read(self):
        pass
