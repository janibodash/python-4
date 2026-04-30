#4-5-6

import os
import csv
import json

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



class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("\nLoading data...")

        try:
            with open(self.filename, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.students.append(row)

            print("Data loaded successfully:", len(self.students), "students")

        except FileNotFoundError:
            print("Error: file not found")

    def preview(self, n=5):
        print("\nFirst", n, "rows:")
        print("-" * 30)

        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")

        print("-" * 30)


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        country_counts = {}

        for s in self.students:
            country = s["country"]

            if country in country_counts:
                country_counts[country] += 1
            else:
                country_counts[country] = 1

        top_3 = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]

        self.result = {
            "total_students": len(self.students),
            "total_countries": len(country_counts),
            "top_3": top_3,
            "all_countries": country_counts
        }

    def print_results(self):
        print("\nCountry Analysis")
        print("-" * 30)
        print("Total students:", self.result["total_students"])
        print("Total countries:", self.result["total_countries"])

        print("\nTop 3 Countries:")
        for i, (c, n) in enumerate(self.result["top_3"], 1):
            print(f"{i}. {c}: {n}")

        print("-" * 30)


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, "w") as f:
                json.dump(self.result, f, indent=4)

            print("\nResult saved to", self.output_path)

        except Exception:
            print("Error saving file")

