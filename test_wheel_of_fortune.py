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

def test_spin_the_wheel():
    #test pin the wheel for different current_section_index and different spin power
    #tests for current_sction_index 0
    wheel.current_section_index = 0
    assert wheel.spin_the_wheel(36) == 36
    wheel.current_section_index = 0
    assert wheel.spin_the_wheel(72) == 0
    wheel.current_section_index = 0
    assert wheel.spin_the_wheel(71) == 71
    wheel.current_section_index = 0
    assert wheel.spin_the_wheel(73) == 1
    wheel.current_section_index = 0
    assert wheel.spin_the_wheel(85) == 13
    wheel.current_section_index = 0
    assert wheel.spin_the_wheel(133) == 61
    wheel.current_section_index = 0
    assert wheel.spin_the_wheel(144) == 0

    #test for current_section_index > 0
    wheel.current_section_index = 13
    assert wheel.spin_the_wheel(45) == 58
    wheel.current_section_index = 65
    assert wheel.spin_the_wheel(45) == 38
    wheel.current_section_index = 65
    assert wheel.spin_the_wheel(145) == 66
    wheel.current_section_index = 79
    assert wheel.spin_the_wheel(137) == 0
