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

    def spin_result(self, index):
        return self.full_wheel[index]



class Player:
    number_of_players = 0

    def __init__(self, name):
        self.name = name
        self.score = 0

    def bankrupt(self):
        self.score = 0

    def can_buy_a_vowel(self):
        return self.score > 250

    def increase_score(self, value):
        self.score += value

    def get_number_of_players(self):
        move_forward = False
        while not move_forward:
            number_of_players = input('Hi! Please enter the number of players: 1, 2 or 3: ')
            if number_of_players.isnumeric():
                num = int(number_of_players) 
                if num > 0 and num < 4:
                    move_forward = True
                    Player.number_of_players = num
                    print(f'All right, there will be {num} number of players')
                else:
                    print('Your number is bigger than 3! Please enter 1,2 or 3') 
            else:
                print('You didn\'t enter a number! Please enter a number 1, 2 or 3')

    def get_player_name(self):
        self.name = input('Please enter your name: ')

     





    # @staticmethod
    # def validate_number_of_players(number):
        
    #     assert type(number) == int,  'you entered not a number! please enter a number 1, 2 or 3' 
    #     assert , 'plase enter a number 1, 2 or 3'
    



class WordPresenter:
    def __init__(self):
        pass
