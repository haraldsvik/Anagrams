
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
    anagrams_with_two_or_more_names = {}

    for name in names:
        sorted_name = ''.join(sorted(name.lower()))

        if sorted_name in obj:
            if name not in obj[sorted_name]:
                obj[sorted_name].append(name)
        else:
            obj[sorted_name] = [name]

    return list(obj.values())


def find_anagrams_alt(names):
    obj = {}
    anagrams_with_two_or_more_names = {}

    for name in names:
        sorted_name = ''.join(sorted(name.lower()))

        if sorted_name in obj:
            if name not in obj[sorted_name]:
                obj[sorted_name].append(name)
                if len(obj[sorted_name]) > 1:
                    anagrams_with_two_or_more_names[sorted_name] = obj[sorted_name]
        else:
            obj[sorted_name] = [name]

    return list(anagrams_with_two_or_more_names.values())


def run():
    population = read_file("./data/larger_population.txt")

    before = time.time()
    anagrams = find_anagrams(population)
    no_duplicates = remove_anagrams_with_one_name(anagrams)
    after = time.time()

    print(no_duplicates)
    print(f"Time taken: {(after - before) * 1000} ms")

    before_alt = time.time()
    anagrams_alt = find_anagrams_alt(population)
    after_alt = time.time()
    print(anagrams_alt)
    print(f"Time taken alt: {(after_alt - before_alt) * 1000} ms")
    


if __name__ == "__main__":
    run()
