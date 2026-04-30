from classes import FileManager, DataLoader, DataAnalyser, ResultSaver

fm = FileManager("students.csv")

if not fm.check_file():
    print("Stopping program")
    exit()

fm.create_output_folder()

dl = DataLoader("students.csv")
dl.load()
dl.preview()

analyser = DataAnalyser(dl.students)
analyser.analyse()
analyser.print_results()

saver = ResultSaver(analyser.result, "output/result.json")
saver.save_json()