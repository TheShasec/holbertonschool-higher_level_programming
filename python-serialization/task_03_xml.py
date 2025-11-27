#!/usr/bin/python3
""" 234 """


import xml.etree.ElementTree as ET


def deserialize_from_xml(filename):
    with open(filename, "r") as mf:
        root = ET.parse(mf).getroot()
        di = {}
        for i in root:
            di[i.tag] = i.attrib
        return di

def serialize_to_xml(dictionary, filename):
    with open(filename, "w") as mf:
        root = ET.Element("root")
        for key, value in dictionary.items():
            elem = ET.SubElement(root, key)
            elem.text = value
        tree = ET.ElementTree(root)
        tree.write(mf)
