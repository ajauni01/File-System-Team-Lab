class File:
    path = ""

    def __init__(self, path):
        self.path = path

    def read(self):
        pass

    def write(self):
        with open(self.path, "w") as file:
            
            try:
                data = input("Enter data: ")
                file.write(data)
            except:
                print("Error: File cannot be written to")

        print("Data has been written to file")