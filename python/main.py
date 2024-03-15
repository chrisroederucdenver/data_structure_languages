#!/usr/bin/env python3

import location
import person
import observation

target = {  'location': location.convert(),
            'person': person.convert(),
            'observation': observation.convert() }


print(target)


