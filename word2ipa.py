import re
import argparse


class Phonetics:

    consonant = {
        'jx': 'ʒ',
        'sx': 'ʃ',
        'hx': 'x',
        'gx': 'dʒ',
        'cx': 'tʃ',
        'ux': 'w',
        'c': 'ts'
    }

    mark = {
        'long': 'ː'
    }

    prefix = [
        '^bo',
        '^dis',
        '^eks',
        '^ek',
        '^ge',
        '^mal',
        '^mis',
        '^pra',
        '^re',
        '^vic'
    ]

    def add_long(self, word):

        added_word = ""
        reversed_word = word[::-1]
        vowels = 0

        for i in reversed_word:
            if i in ['a', 'i', 'u', 'e', 'o']:
                vowels += 1

            if vowels == 2:
                i = self.mark['long'] + i
                vowels += 1

            added_word += i

        added_word = added_word[::-1]
        return added_word

    def to_ipa(self, word):

        for reg in self.prefix:
            word = re.sub(reg, reg[1:]+"'", word)

        for k, v in self.consonant.items():
            word = word.replace(k, v)

        return word

    def to_ipa_from_context(self, context):
        ipa_context = ""
        for word in context.lower().split(" "):
            ipa_context += self.to_ipa(self.add_long(word)) + " "

        return ipa_context


if __name__ == '__main__':

    parse = argparse.ArgumentParser(description='''
    this is translating IPA from context of Esperanto.
    then prefix exist, add apostrophe.
    ''')

    parse.add_argument('-t', '--text', default=None, type=str)
    args = parse.parse_args()

    ins = Phonetics()
    text = args.text
    print(text)

    eo = ins.to_ipa_from_context(text)
    print(eo)
