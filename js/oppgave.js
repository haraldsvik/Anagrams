const { open } = require("fs/promises")
// time complexity:
// +size of population
// +length of words
// +number of anagrams
// = 
const readFile = async (filename) => {
  let list = []
  const file = await open(filename)
  for await (const line of file.readLines()) {
    list.push(line)
  }
  return list
}

const findAnagrams = (names) => {
  let obj = {}
  let len = names.length
  while (len--) {
    let name = names[len]
    let sortedName = name.toLowerCase().split('').sort();
    if (!obj[sortedName]) {
      obj[sortedName] = []
      obj[sortedName].push(name)
    } else {
      if (obj[sortedName].indexOf(name) === -1) {
        obj[sortedName].push(name)
      }
    }
  }
  return Object.values(obj).filter((v) => v.length > 1)
}


async function run() {
  const names = await readFile('population.txt')
  console.time('findAnagrams')
  const results = findAnagrams(names)
  console.timeLog('findAnagrams', "readFile ferdig")
  console.log('results : ', JSON.stringify(results, null, 2))
  console.timeEnd('findAnagrams')
}

run()
