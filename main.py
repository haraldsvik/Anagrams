
import time


def read_file(file_name):
    names = []
    with open(file_name, "r") as f:
        for line in f:
            names.append(line.strip())
    return names


def remove_anagrams_with_one_name(anagrams):
    return [anagram for anagram in anagrams if len(anagram) > 1]


def find_anagrams(names):
    obj = {}

    for name in names:
        sorted_name = ''.join(sorted(name.lower()))

        if sorted_name in obj:
            if name not in obj[sorted_name]:
                obj[sorted_name].append(name)
        else:
            obj[sorted_name] = [name]

    return list(obj.values())


def run():
    population = read_file("population.txt")

    before = time.time()
    anagrams = find_anagrams(population)
    no_duplicates = remove_anagrams_with_one_name(anagrams)
    after = time.time()

    print(no_duplicates)
    print("Time: ", (after - before) * 1000, "ms")


if __name__ == "__main__":
    run()
