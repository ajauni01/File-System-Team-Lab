class Directory:
    path = ""
    items = []

    def __init__(self, path):
        self.path = path

    def __add__(self, other):
        self.items.append(other)