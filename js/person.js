#!/usr/bin/env node

data = require('./input_json/patient.input.json')
vocab = require('./vocab.json')

// Shows two syntaxes for getting values out of a deep JSON structure

// 1 looks like object notation    
person = {}
person.id =  data.id;
person.race =  data.extension[0].extension[0].valueCoding.display
race_code =  data.extension[0].extension[0].valueCoding.code
race_vocab =  data.extension[0].extension[0].valueCoding.system
console.log(vocab[race_vocab])
console.log(race_vocab)
console.log(race_code)
console.log(vocab[race_vocab][race_code])
person.race_concept_id = vocab[race_vocab][race_code]

person.ethnicity =  data.extension[1].extension[0].valueCoding.display
person.gender = data.gender
person.birthdate = data.birthDate
console.log(person)
 
// demonstrating that with JS you can use variables to get inside dictionaries/objects
console.log(vocab.gender.male)
x='gender'
y='male'
console.log(vocab[x][y])


console.log("----------------")

// 2 looks more like using strings as keys to access a dictionary/map.
// This is nearly exactly the pyton code. I changed print to console.log.
console.log("id:         ", data["id"]);
console.log("race:       ", data["extension"][0]["extension"][0]["valueCoding"]["display"])
console.log("ethnicity:  ", data["extension"][1]["extension"][0]["valueCoding"]["display"])
console.log("gender:     ", data["gender"])
console.log("birthdate:  ", data["birthDate"])

console.log("address:    ", data["address"][0]["line"])
console.log("city:       ", data["address"][0]["city"])
console.log("state:      ", data["address"][0]["state"])
console.log("zip:        ", data["address"][0]["postalCode"])

console.log("name.given: ", data["name"][0]["given"][0])
console.log("name.family:", data["name"][0]["family"])


