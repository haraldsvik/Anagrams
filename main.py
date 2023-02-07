
import time


def read_file(file_name):
    names = []
    with open(file_name, "r") as f:
        for line in f:
            # remove whitespace
            # dont include empty lines
            # dont include names with numbers
            if line.strip() and not any(char.isdigit() for char in line):
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
    population = read_file("./data/babynames.txt")

    before = time.time()

    anagrams = find_anagrams(population)
    no_duplicates = remove_anagrams_with_one_name(anagrams)

    after = time.time()
    time_taken = format(((after - before) * 1000), '.2f')

    for anagram in no_duplicates:
        print(anagram)

    print(f"Time taken: {time_taken} ms")


if __name__ == "__main__":
    run()
