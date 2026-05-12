import os

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")

        if not os.path.exists(self.filename):
            print("Error: file not found")
            return False

        print("File found:", self.filename)
        return True

    def create_output_folder(self, folder="output"):
        print("\nChecking output folder...")

        if not os.path.exists(folder):
            os.makedirs(folder)
            print("Output folder created:", folder)
        else:
            print("Output folder already exists:", folder)