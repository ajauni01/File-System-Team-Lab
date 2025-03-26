class File:
    path = ""

    def __init__(self, path):
        self.path = path
        open(self.path, 'x')  # Create a file at location

    def read(self):
        pass

    def write(self):
        pass