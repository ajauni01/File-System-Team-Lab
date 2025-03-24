import os


class Directory:
    name = ""
    items = []

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        self.items.append(other)


class File:
    name = ""

    def __init__(self, name):
        self.name = name

    def read(self):
        pass

    def write(self):
        pass


if __name__ == "__main__":
    # Driver Code