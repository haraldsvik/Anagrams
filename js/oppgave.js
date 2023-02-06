const { open } = require("fs/promises")
// time complexity:
// +size of population
// +length of words
// +number of anagrams
// = 
async function findAnagrams() {
  const file = await open("population.txt")
  let obj = {}
  for await (const line of file.readLines()) {
    let s = line.toLowerCase().split('').sort();
    if (!obj[s]) {
      obj[s] = []
      obj[s].push(line)
    } else {
      if (obj[s].indexOf(line) === -1) {
        obj[s].push(line)
      }
    }
  }
  return Object.values(obj).filter((v) => v.length > 1)
}


console.time('findAnagrams')
findAnagrams().then((results) => {
  console.timeLog('findAnagrams', "findAnagrams ferdig")
  console.log('results : ', JSON.stringify(results, null, 2))
  console.timeEnd('findAnagrams')
})

