import time
import unittest

from main import find_anagrams, read_file, remove_anagrams_with_one_name


class OppgaveTest(unittest.TestCase):
    def setUp(self):
        self.population = read_file("./data/population.txt")

    def test_input_is_not_none(self):
        self.assertIsNotNone(self.population)

    def test_population_is_list(self):
        self.assertIsInstance(self.population, list)

    def test_population_is_not_empty(self):
        self.assertTrue(len(self.population) > 0)

    def test_find_anagrams(self):
        anagrams = find_anagrams(self.population)

        self.assertIsInstance(anagrams, list)
        self.assertTrue(len(anagrams) > 0)

    def test_find_case_insensitive_anagrams(self):
        args = ["erik", "Kire", "lene"]
        anagrams = find_anagrams(args)
        self.assertEqual(len(anagrams), 2)

    def test_retuns_empty_list_if_no_anagrams(self):
        args = [""]
        anagrams = find_anagrams(args)
        self.assertEqual(len(anagrams), 1)

    def test_no_duplicate_anagrams(self):
        anagrams = find_anagrams(self.population)
        for anagram in anagrams:
            self.assertEqual(len(anagram), len(set(anagram)))

    def test_no_empty_anagrams(self):
        anagrams = find_anagrams(self.population)
        no_duplicates = remove_anagrams_with_one_name(anagrams)

        for anagram in no_duplicates:
            self.assertTrue(len(anagram) > 1)

    def test_check_if_to_slow(self):
        before = time.time()
        anagrams = find_anagrams(self.population)
        no_duplicates = remove_anagrams_with_one_name(anagrams)
        after = time.time()

        time_taken = (after - before) * 1000
        name_lenght = len(self.population)
        time_per_name = time_taken / name_lenght

        # 0.0015 ms per name is an arbitrary limit
        self.assertTrue(time_per_name < 0.0015)


if __name__ == '__main__':
    unittest.main()
