import os


class Directory:
    path = ""
    items = []

    def __init__(self, path):
        self.path = path

    def __add__(self, other):
        self.items.append(other)


class File:
    path = ""

    def __init__(self, path):
        self.path = path

    def read(self):
        pass

    def write(self):
        pass


if __name__ == "__main__":
    # Driver Code