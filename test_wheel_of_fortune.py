from wheel_of_fortune import Wheel
import random

wheel = Wheel()

def test_full_wheel_length():
    assert len(wheel.full_wheel) == 72

def test_full_wheel_has_three_same_subsections():
    index_list = list(range(0, 72, 3))
    index_list.remove(12)
    for _ in range(5):
        rand_index = random.choice(index_list)
        assert wheel.full_wheel[rand_index] == wheel.full_wheel[rand_index + 1] == wheel.full_wheel[rand_index + 2]

def test_one_million_subsections():
    assert wheel.full_wheel[12] == wheel.full_wheel[14] == 'BANKRUPT'
    assert wheel.full_wheel[13] == 'ONE MILLION'


