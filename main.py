from analytics import FileManager, DataLoader, ResultSaver, Report, CountryAnalyser, DataAnalyser


fm = FileManager("students.csv")
if not fm.check_file():
    exit()

fm.create_output_folder()

dl = DataLoader("students.csv")
students_data = dl.load()


analysers = [
    CountryAnalyser(students_data), 
    DataAnalyser(students_data)
]

print('\n' + '='*30)
print('RUNNING ALL ANALYSERS (POLYMORPHISM)')
print('='*30)

for a in analysers:
    print(a)
    a.analyse()
    a.print_results()
    print("-" * 20)


saver = ResultSaver(analysers[0].result, "output/result.json")
report = Report(analysers[0], saver)
report.generate()