from persist import persist
import csv


class CsvPersist(persist.IPersist):

    def __init__(self, mode='xlsx'):
        super().__init__()
        self.mode = mode

    def write(self, to_sink, data):
        csv.writer(to_sink, data)

    def read(self, source):
        return csv.reader(source)
