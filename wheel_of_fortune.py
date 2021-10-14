import string
import random


ALPHABET = string.ascii_uppercase
VOWELS = 'AIEOU'
vowel_translation = {ord(letter): None for letter in VOWELS}
CONSONANTS = ALPHABET.translate(vowel_translation)



class Wheel:
    sections = [
        600, 650, 500, 700, 
        'ONE MILLION', 600, 550, 500, 
        600, 'BANKRUPT', 650, 'FREE PLAY', 
        700, 'LOSE A TURN', 800, 500, 
        650, 500, 900, 'BANKRUPT', 
        2500, 'WILD', 600, 700
        ]
    spin_power_options = {'easy': (24, 36), 'medium': (36, 60), 'hard': (60, 96)}

    def __init__(self):
        self.full_wheel = self._add_subsections()
        self.total_subsections = len(self.full_wheel)
        #generate random current section index
        self.current_section_index = random.randint(0, (self.total_subsections - 1))

    def _add_subsections(self):
        subsections = []
        for item in self.sections:
            if item == 'ONE MILLION':
                subsections.append('BANKRUPT')
                subsections.append('ONE MILLION')
                subsections.append('BANKRUPT')
            else:    
                for x in range(3):
                    subsections.append(item)
        return subsections

    def get_spin_power(self, option: str):
        value = self.spin_strength_options[option]
        return random.randint(*value)

    def spin_the_wheel(self, spin_power: int):
        self.current_section_index = (self.current_section_index + spin_power) % self.total_subsections
        return self.current_section_index


