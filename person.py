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
        data["address"][0]["line"],
        data["address"][0]["city"],
        data["address"][0]["state"],
        data["address"][0]["postalCode"])
    location_id = id_map.get(location_key)

    dest = {}
    dest.id = data["id"]
    dest.race = data["extension"][0]["extension"][0]["valueCoding"]["display"]
    dest.ethnicity = data["extension"][1]["extension"][0]["valueCoding"]["display"]
    dest.gender = data["gender"]
    dest.birthdate = data["birthDate"]
    dest.location_id = location_id

    return dest

def play():
    # if the output structure is deeper, you have to generate/create/"vivify" the intermediate structures.
    # contrived, but like this:
    # (Perl implicitly does the creation with only something similar to the last line.)
    dest = { "part_a": null, "part_b": null, "part_c": null }
    dest.part_a = [null, null, null]
    dest.part_a[1] = {"person": null, "addr": null, "event":null}
    dest.part_a[1].person = convert()}
    
    # The upshot of auto-vivification in Perl (as if it matters), is that you can
    # assign from a source path to a destination path with minimal extra code.

    return dest
