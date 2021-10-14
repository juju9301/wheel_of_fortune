import string
import random


ALPHABET = string.ascii_uppercase
VOWELS = 'AIEOU'
vowel_translation = {ord(letter): None for letter in VOWELS}
CONSONANTS = ALPHABET.translate(vowel_translation)



class Wheel:
    SECTIONS = [
        600, 650, 500, 700, 
        'ONE MILLION', 600, 550, 500, 
        600, 'BANKRUPT', 650, 'FREE PLAY', 
        700, 'LOSE A TURN', 800, 500, 
        650, 500, 900, 'BANKRUPT', 
        2500, 'WILD', 600, 700
        ]
    options = {'easy': (24, 36), 'medium': (36, 60), 'hard': (60, 96)}

    def __init__(self):
        self.current_section_index = random.randint(0, 23)
        self.full_wheel = self._add_subsections()

    def _add_subsections(self):
        subsections = []
        for item in self.SECTIONS:
            if item == 'ONE MILLION':
                subsections.append('BANKRUPT')
                subsections.append('ONE MILLION')
                subsections.append('BANKRUPT')
            else:    
                for x in range(3):
                    subsections.append(item)
        return subsections

    def get_strength(self, option: str):
        value = self.options[option]
        return random.randint(*value)

    def spin_the_wheel(self, strength: int):
        rest = strength % 24 + self.current_section_index
        if rest <= 23:
            self.current_section_index = rest
            return self.current_section_index
        else:
            pass
        

        return current_section_index


