#!/usr/bin/python3
""" 234 """


import xml.etree.ElementTree as ET


def deserialize_from_xml(filename):
    root = ET.parse(filename).getroot()
    di = {}
    for i in root:
        try:
            value = int(child.text)
        except ValueError:
            try:
                value = float(child.text)
            except ValueError:
                value = child.text
    return di

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        elem = ET.SubElement(root, key)
        elem.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8")
