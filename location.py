#!/usr/bin/env python3

import json
import id_map

f = open("input_json/patient.input.json")
data = json.load(f)

def convert():

    location_key = (
        data["address"][0]["line"],
        data["address"][0]["city"],
        data["address"][0]["state"],
        data["address"][0]["postalCode"])
    new_id = id_map.create(location_key)

    print("zip:        ", data["address"][0]["postalCode"])
    print("location_id:", new_id)
    print("address:    ", data["address"][0]["line"])
    print("city:       ", data["address"][0]["city"])
    print("state:      ", data["address"][0]["state"])
    print("zip:        ", data["address"][0]["postalCode"])



