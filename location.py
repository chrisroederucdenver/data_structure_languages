#!/usr/bin/env python3

import json
import id_map

f = open("input_json/patient.input.json")
data = json.load(f)

def create():
    dest = { 'location_id': None, 'address': None, 'city': None, 'state': None, 'zip': None }
    return dest

def convert():

    location_key = (
        data['address'][0]['line'],
        data['address'][0]['city'],
        data['address'][0]['state'],
        data['address'][0]['postalCode'])
    new_id = id_map.create(location_key)

    dest = create()

    dest['location_id'] = new_id
    dest['address']     = data['address'][0]['line']
    dest['city']        = data['address'][0]['city']
    dest['state']       = data['address'][0]['state']
    dest['zip']         = data['address'][0]['postalCode']

    return dest


