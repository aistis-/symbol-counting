# Stores file information
class FileStats(object):

    def __init__(self, file_name):
        self.symbols = {}
        self.file_name = file_name
        self.analyze_name()

    def analyze_name(self):
        for char in self.file_name:
            try:
                self.symbols[ord(char)] += 1
            except KeyError:
                self.symbols[ord(char)] = 1

    def get_counted_symbols(self):
        result = self.file_name

        for symbol, times in self.symbols.items():
            result += '\n\t' + chr(symbol) + ' ' + str(times)

        return result