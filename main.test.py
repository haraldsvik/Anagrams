import unittest

from main import find_anagrams



class OppgaveTest(unittest.TestCase):
    def setUp(self):
    #self.population = [ "erik", "kire", "lene"]
        self.population = []
        with open("population.txt", "r") as f:
            for line in f:
                self.population.append(line.strip())
            

    def test_input(self):
        self.assertIsNotNone(self.population)

    def test_population_is_list(self):
        self.assertIsInstance(self.population, list)
    
    def test_population_is_not_empty(self):
        self.assertTrue(len(self.population) > 0)

    def test_find_anagrams(self):
        anagrams = find_anagrams(self.population)
        self.assertIsInstance(anagrams, list)
        self.assertTrue(len(anagrams) > 0)    

if __name__ == '__main__':
    unittest.main()
