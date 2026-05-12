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
            return self.students

        except FileNotFoundError:
            print("Error: file not found")
            return []

    def preview(self, n=5):
        print("\nFirst", n, "rows:")
        print("-" * 30)

        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")

        print("-" * 30)


class DataAnalyser:
    def __init__(self, students):
        # Сохраняем данные и готовим место под результат 
        self.students = students
        self.result = {}

    def analyse(self):
        # Базовый класс не делает расчетов сам 
        print("Not implemented - use a child class")

    def print_results(self):
        # Просто выводим всё, что накопилось в словаре результатов 
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        # Красивое описание объекта 
        return f"DataAnalyser: base class, {len(self.students)} students"
    

# Task 2: Дочерний класс для Варианта B
class CountryAnalyser(DataAnalyser):
    def __init__(self, students):
        # Вызываем конструктор родителя [cite: 52]
        super().__init__(students)

    def analyse(self):
        # Логика анализа из Практики 5 [cite: 54]
        counts = {}
        for s in self.students:
            country = s.get("country", "Unknown")
            counts[country] = counts.get(country, 0) + 1
        
        # Сортируем топ-3 для примера [cite: 158]
        top_3 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]
        
        # Сохраняем в self.result [cite: 55]
        self.result = {
            "total_students": len(self.students),
            "total_countries": len(counts),
            "top_3": top_3
        }

    # Task 3: Переопределение вывода [cite: 77]
    def print_results(self):
        print("\nCOUNTRY ANALYSIS REPORT") # Заголовок [cite: 78]
        print("============")
        super().print_results()             # Вызов родительского метода [cite: 79]
        print("=============")            # Футер [cite: 80]

    def __str__(self):
        # Описание для Task 2 [cite: 57]
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"


# Task 4: Association
class Report:
    def __init__(self, analyser, saver):
        # Сохраняем ссылки на объекты (Ассоциация)
        self.analyser = analyser  # USES-A DataAnalyser
        self.saver = saver        # USES-A ResultSaver

    def generate(self):
        print("\nGenerating report...")
        # Менеджер отдает команды объектам
        self.analyser.analyse()
        self.analyser.print_results()
        self.saver.save_json()
        print("Report complete.")



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
