
def read_file(file_name):
    with open(file_name, "r") as f:
        return f.read()


def find_anagrams(names):
  obj = {}

  for name in names:
    sorted_name = ''.join(sorted(name))

    if sorted_name in obj:  
      obj[sorted_name].append(name)
    else:
      obj[sorted_name] = [name]

  return obj.values()
 

def run():
    population = read_file("population.txt")
    anagrams = find_anagrams(population)
    print(anagrams)


if __name__ == "__main__":
    run()
