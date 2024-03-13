#!/usr/bin/env python3

import json
from vocab_map_file import vocab_map
import id_map

f = open("input_json/observation.input.json")
data = json.load(f)

def convert():
    obs_vocabulary_id = data['code']['coding'][0]['system']
    obs_concept_code  = data['code']['coding'][0]['code']
    (concept_name, obs_concept_id) = vocab_map[(obs_vocabulary_id, obs_concept_code)]

    dest = { 'observation_id': None, 'person_id': None, 'observation_concept_id': None, 'observation_date': None, 'value_as_number': None, 'value_as_string': None, 'value_as_concept_id': None, 'provider_id': None}

    dest['observation_id']         = data['id']
    dest['.person_id']              = data['subject']['reference']
    dest['observation_concept_id'] = obs_concept_id
    dest['observation_date']       = data['effectiveDateTime']
    dest['value_as_number']        = 0
    dest['value_as_string']        = 0
    dest['value_as_concept_id']    = 0
    dest['provider_id']            = data['performer'][0]['reference']

    return dest




