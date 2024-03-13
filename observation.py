#!/usr/bin/env python3

import json
from vocab_map_file import vocab_map
import id_map

f = open("input_json/observation.input.json")
data = json.load(f)

def convert():
    obs_vocabulary_id = data["code"]["coding"][0]["system"]
    obs_concept_code  = data["code"]["coding"][0]["code"]
    (concept_name, obs_concept_id) = vocab_map[(obs_vocabulary_id, obs_concept_code)]

    print("observation_id:         ", data["id"]);
    print("person_id:              ", data["subject"]["reference"]);
    print("observation_concept_id: ", obs_concept_id)
    print("observation_date:       ", data["effectiveDateTime"])
    print("value_as_number:        ", 0)
    print("value_as_string:        ", 0)
    print("value_as_concept_id:    ", 0)
    print("provider_id:            ", data["performer"][0]["reference"]);




