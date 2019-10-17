from dice import Dice
import pytest

def test_arandom_no_weight():
    dice_instance = Dice(6)
    assert dice_instance.value == 0
    dice_instance.roll()
    assert dice_instance.value == 1
    dice_instance.roll()
    assert dice_instance.value == 3
    dice_instance.roll()
    assert dice_instance.value == 3
    dice_instance.roll()
    assert dice_instance.value == 1

    dice_instance = Dice(100)
    assert dice_instance.value == 0
    dice_instance.roll()
    assert dice_instance.value == 73
    dice_instance.roll()
    assert dice_instance.value == 33
    dice_instance.roll()
    assert dice_instance.value == 73
    dice_instance.roll()
    assert dice_instance.value == 78

def test_arandom_with_weight():
    dice_instance = Dice(6,[1,1,1,1,1,1])
    assert dice_instance.value == 0
    dice_instance.roll()
    assert dice_instance.value == 5
    dice_instance.roll()
    assert dice_instance.value == 1
    dice_instance.roll()
    assert dice_instance.value == 6
    dice_instance.roll()
    assert dice_instance.value == 6

    dice_instance = Dice(10,[1,2,3,4,5,6,7,8,9,10])
    assert dice_instance.value == 0
    dice_instance.roll()
    assert dice_instance.value == 6
    dice_instance.roll()
    assert dice_instance.value == 9
    dice_instance.roll()
    assert dice_instance.value == 9
    dice_instance.roll()
    assert dice_instance.value == 8

def test_arandom_negative_numbers():
    with pytest.raises(Exception):
        result = Exception('negative probabilities not allowed')
        dice_instance = Dice(6,[1,-1,1,1,1,1])
        assert dice_instance.value == result
        dice_instance = Dice(6,[1,1,1,1,1,-1])
        assert dice_instance.value == result

def test_arandom_sum_of_numbers():
    dice_instance = Dice(6,[0,0,0,0,0,0])


def test_type():
    with pytest.raises(Exception):
        result = Exception('negative probabilities not allowed')
        dice_instance = Dice(6,[1,-1,'1',1,1,1])
        assert dice_instance.value == result