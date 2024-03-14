#!/usr/bin/env node

data = require('./input_json/patient.input.json')

// Shows two syntaxes for getting values out of a deep JSON structure

// 1 looks like object notation    
console.log("id:         ", data.id);
console.log("race:       ", data.extension[0].extension[0].valueCoding.display)
console.log("ethnicity:  ", data.extension[1].extension[0].valueCoding.display)
console.log("gender:     ", data.gender)
console.log("birthdate:  ", data.birthDate)

console.log(" querying a db for the concept mapping requires a database behind a REST server ----------------")
console.log("race vocab:       ", data.extension[0].extension[0].valueCoding.system)
console.log("race  code:       ", data.extension[0].extension[0].valueCoding.code)
console.log("ethnicity vocab:  ", data.extension[1].extension[0].valueCoding.system)
console.log("ethnicity  code:  ", data.extension[1].extension[0].valueCoding.code)

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


