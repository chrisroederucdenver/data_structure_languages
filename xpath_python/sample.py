#!/usr/bin/env python3

# hacking with code from here: https://docs.python.org/3/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
from pathlib import Path

tree = ET.parse("resources/sample.xml")
root = tree.getroot()

xpaths_text = Path("resources/sample_paths.txt").read_text()
for xpath_line in xpaths_text.splitlines():
    if len(xpath_line) > 0 and xpath_line[0] != '#':

        print("--------------------------")
        print(f"path: {xpath_line}")
        child_list = tree.findall(xpath_line)
        for child in child_list:
            print(child)
            print("    ", child.tag)
            print("    ", child.attrib)
