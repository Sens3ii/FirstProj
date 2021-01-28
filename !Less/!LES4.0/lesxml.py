import xml.etree.ElementTree as ET
myfile = 'user_settings.xml'
tree = ET.parse(myfile)
root = tree.getroot()
