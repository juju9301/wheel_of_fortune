import pytest
from .wheel_of_fortune import Wheel
import random

wheel = Wheel()

def test_full_wheel_length():
    assert len(wheel.full_wheel) == 72

def test_full_wheel_has_three_same_subsections():
    index_list = list(range(0, wheel.total_subsections, 3))
    index_list.remove(12)
    for _ in range(5):
        rand_index = random.choice(index_list)
        assert wheel.full_wheel[rand_index] == wheel.full_wheel[rand_index + 1] == wheel.full_wheel[rand_index + 2]

def test_one_million_subsections():
    assert wheel.full_wheel[12] == wheel.full_wheel[14] == 'BANKRUPT'
    assert wheel.full_wheel[13] == 'ONE MILLION'


@pytest.mark.parametrize('current_index,spin_power,result_index', 
    [
        (0, 36, 36), (0, 72, 0), (0, 71, 71), 
        (0, 73, 1), (0, 85, 13), (0, 133, 61), 
        (0, 144, 0), (13, 45, 58), (65, 45, 38),
        (65, 145, 66), (79, 137, 0)
        ]
)
def test_spin_the_wheel(current_index, spin_power, result_index):
    #test pin the wheel for different current_section_index and different spin power
    wheel.current_section_index = current_index
    assert wheel.spin_the_wheel(spin_power) == result_index
