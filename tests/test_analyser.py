import unittest
from analytics.analyser import CountryAnalyser

class TestAnalyser(unittest.TestCase):
    def setUp(self):
        
        self.sample = [
            {"country": "USA", "GPA": "4.0"},
            {"country": "USA", "GPA": "3.5"},
            {"country": "India", "GPA": "3.8"}
        ]

    def test_total_students(self):
        analyser = CountryAnalyser(self.sample)
        analyser.analyse()
        
        self.assertEqual(analyser.result["total_students"], 3)

    def test_total_countries(self):
        analyser = CountryAnalyser(self.sample)
        analyser.analyse()
        
        self.assertEqual(analyser.result["total_countries"], 2)

if __name__ == '__main__':
    unittest.main()

#..
#----------------------------------------------------------------------
#Ran 2 tests in 0.000s

#OK
#PS D:\python-3p> 