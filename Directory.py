class Directory:
    path = ""
    items = []

    def __init__(self, path):
        self.path = path

    def __iadd__(self, other):
        self.items.append(other)