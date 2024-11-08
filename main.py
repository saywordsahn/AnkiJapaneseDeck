from entry import Entry
import xml.etree.ElementTree as et
import csv

# def prettify(elem):
#     """Return a pretty-printed XML string for the Element.
#     """
#     rough_string = et.tostring(elem, 'utf-8')
#     reparsed = minidom.parseString(rough_string)
#     return reparsed.toprettyxml(indent="\t")



tree = et.parse('JMdict_e.xml')
root = tree.getroot()
print(root.tag)
found = False

kanjis = []

for entry in root:

    kEntry = Entry()

    for x in entry:

        if x.tag == 'k_ele':
            kanji = x.find('keb').text

            kEntry.set_kanji(kanji)
            # print(x.find('keb').text)
            # print()

        elif x.tag == 'r_ele':
            kEntry.set_reading(x.find('reb').text)

            # print(x.find('reb').text)
            # print()

        elif x.tag == 'sense':
            for gloss in x.findall('gloss'):
                kEntry.add_meaning(gloss.text)
                # print(gloss.text)


    kanjis.append(kEntry)

#
# with open("sentences.tsv", encoding='utf-8') as file:
#     tsv_file = csv.reader(file, delimiter="\t")
#     for line in tsv_file:
#         for kanji in kanjis:
#             if line[1].find(kanji.kanji) != -1 and line[3].find(';') == -1:
#                 kanji.add_example_sentence(line[1], line[3])






with open('notes.txt', 'w') as f:
    for kanji in kanjis:

        f.write(kanji.get_anki_line())
        f.write('\n')
    # print(kanji.kanji)
    #
    # print(kanji.reading)
    #
    # for meaning in kanji.meanings:
    #     print(meaning)
    #
    # for s in kanji.examples:
    #     print(s[0], '\t', s[1])