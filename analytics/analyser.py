import json

class DataAnalyser:
    def __init__(self, students):
        
        self.students = students
        self.result = {}

    def analyse(self):
        
        print("Not implemented - use a child class")

    def print_results(self):
        
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        
        return f"DataAnalyser: base class, {len(self.students)} students"
    

class CountryAnalyser(DataAnalyser):
    def __init__(self, students):
        
        super().__init__(students)

    def analyse(self):
        
        counts = {}
        for s in self.students:
            country = s.get("country", "Unknown")
            counts[country] = counts.get(country, 0) + 1
        
        
        top_3 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]
        
        
        self.result = {
            "total_students": len(self.students),
            "total_countries": len(counts),
            "top_3": top_3
        }

    
    def print_results(self):
        print("\nCOUNTRY ANALYSIS REPORT") 
        print("============")
        super().print_results()             
        print("=============")            

    def __str__(self):
        
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"

