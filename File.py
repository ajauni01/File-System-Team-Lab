class File:
    path = ""

    def __init__(self, path):
        self.path = path
        open(self.path, 'x')  # Create a file at location

    def read(self):
        with open(self.path, "r") as file:
            content = file.read()
            if content != "":
                print(f"Content of {self.path}: {content}")
            else:
                print("File is empty")
        file.close()

    def write(self):
        with open(self.path, "w") as file:
            
            try:
                print("Enter data to write to file: ")
                data = input("Enter data: ")
                file.write(data)
            except:
                print("Error: File cannot be written to")

        print("Data has been written to file")