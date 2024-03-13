#!/usr/bin/env python3

import json
import id_map

f = open("input_json/patient.input.json")
data = json.load(f)

def print_convert():
    location_key = (
        data["address"][0]["line"],
        data["address"][0]["city"],
        data["address"][0]["state"],
        data["address"][0]["postalCode"])
    location_id = id_map.get(location_key)

    print("person_id:  ", data["id"])
    print("race:       ", data["extension"][0]["extension"][0]["valueCoding"]["display"])
    print("ethnicity:  ", data["extension"][1]["extension"][0]["valueCoding"]["display"])
    print("gender:     ", data["gender"])
    print("birthdate:  ", data["birthDate"])
    print("location_id:", location_id)

def convert():
    location_key = (
        data['address'][0]['line'],
        data['address'][0]['city'],
        data['address'][0]['state'],
        data['address'][0]['postalCode'])
    location_id = id_map.get(location_key)

    dest = {'person_id': None, 'race': None, 'ethnicity': None, 'gender': None, 'birthdate': None, 'location_id': None}
    dest['person_id'] = data['id']
    dest['race'] = data['extension'][0]['extension'][0]['valueCoding']['display']
    dest['ethnicity'] = data['extension'][1]['extension'][0]['valueCoding']['display']
    dest['gender'] = data['gender']
    dest['birthdate'] = data['birthDate']
    dest['location_id'] = location_id

    return dest
