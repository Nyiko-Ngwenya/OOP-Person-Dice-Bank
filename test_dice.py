from dice import Dice

def test_addition():
    dice_instance = Dice(6)
    assert dice_instance.value == 1
    dice_instance.roll()
    assert dice_instance.value == 1
    dice_instance.roll()
    assert dice_instance.value == 3
    dice_instance.roll()
    assert dice_instance.value == 3
    dice_instance.roll()
    assert dice_instance.value == 1
