class DataHandler:

    def __init__(self, file):
        self.file = file

    def __enter__(self):
        self.file = open(self.file, 'a')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        