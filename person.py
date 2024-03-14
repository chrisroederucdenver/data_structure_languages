#!/usr/bin/env python3

import json
import id_map
from vocab_map_file import vocab_map

f = open("input_json/patient.input.json")
data = json.load(f)

def create():
    dest = {'person_id': None, 'race': None, 'ethnicity': None, 'gender': None, 'birthdate': None, 'location_id': None}
    return dest

def convert():
    location_key = (
        data['address'][0]['line'],
        data['address'][0]['city'],
        data['address'][0]['state'],
        data['address'][0]['postalCode'])
    location_id = id_map.get(location_key)

    #print(data.keys())
    #print(data['extension'])
    print(data['extension'][0].keys())

    race_vocabulary_id = data['extension'][0]['extension'][0]['valueCoding']['system']
    race_concept_code  = data['extension'][0]['extension'][0]['valueCoding']['code']
    (concept_name, race_concept_id, vocab) = vocab_map[(race_vocabulary_id, race_concept_code)]
    print(concept_name)

    ethnicity_vocabulary_id = data['extension'][1]['extension'][0]['valueCoding']['system']
    ethnicity_concept_code  = data['extension'][1]['extension'][0]['valueCoding']['code']
    (concept_name, ethnicity_concept_id, vocab) = vocab_map[(ethnicity_vocabulary_id, ethnicity_concept_code)]
    print(concept_name)

    gender_vocabulary_id =  "TODO_gender_vocab"
    gender_concept_code  = data['gender']
    (concept_name, gender_concept_id, vocab) = vocab_map[(gender_vocabulary_id, gender_concept_code)]

    dest = create()
    dest['person_id'] = data['id']
    dest['race'] = data['extension'][0]['extension'][0]['valueCoding']['display']
    dest['ethnicity'] = data['extension'][1]['extension'][0]['valueCoding']['display']
    dest['gender'] = data['gender']
    dest['birthdate'] = data['birthDate']
    dest['location_id'] = location_id

    return dest
