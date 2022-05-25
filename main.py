import xml.etree.ElementTree as et
tree = et.parse('JMdict_e.xml')
root = tree.getroot()
print(root.tag)

for entry in root:
    for x in entry:

        if x.tag == 'k_ele':
            print(x.find('keb').text)
            print()

        if x.tag == 'r_ele':
            print(x.find('reb').text)
            print()

        if x.tag == 'sense':
            for gloss in x.findall('gloss'):
                print(gloss.text)
                print()
                print()
                print()

