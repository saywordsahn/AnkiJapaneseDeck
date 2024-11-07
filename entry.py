

class Entry:

    def __init__(self):
        self.kanji = ''
        self.reading = ''
        self.meanings = []
        self.examples = []

    def print(self):
        print(self.kanji, ' ', self.reading)
        for i in range(len(self.meanings)):
            print((i + 1), self.meanings[i])

    def set_kanji(self, kanji):
        self.kanji = kanji

    def set_reading(self, reading):
        self.reading = reading

    def add_meaning(self, meaning):
        self.meanings.append(meaning)

    def add_example_sentence(self, japanese, english):
        self.examples.append([japanese, english])

    def get_anki_line(self):
        line = self.kanji + ';'
        line += self.reading + ';'
        for i in range(len(self.meanings)):

            if i == len(self.meanings) - 1:
                line += self.meanings[i]
            else:
                line += self.meanings[i] + '<br>'

        line += ';'

        for i in range(len(self.examples)):
            if i == len(self.examples) - 1:
                line += self.examples[i][0] + '\t' + self.examples[i][1]
            else:
                line += self.examples[i][0] + '\t' + self.examples[i][1] + '<br>'
