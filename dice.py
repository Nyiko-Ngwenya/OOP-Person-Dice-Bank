import random

class Dice:
    #random.seed(9001)
    def __init__(self,sides,probabilities=[]):
        self.sides = sides
        self.value = 0
        self.probabilities = probabilities
        if len(self.probabilities) > 0 and len(self.probabilities) != self.sides:
            raise Exception
       
    def roll(self):
        if len(self.probabilities) == 0:
            self.value = random.randint(1,self.sides)
        else:
            self.checkNegatives()
            numbers = [1,2,3,4,5,6]
            numbers_after = []
            for i in range(self.sides):
                print(numbers[i],'The actaul number ')
                print(self.probabilities[i], 'The probability')
                if self.probabilities[i] >= 1:
                    for a in range(self.probabilities[i]):
                        numbers_after.append(numbers[i])
            random_number = random.randint(0,len(numbers_after)-1)
            self.value = numbers_after[random_number]
        return self.value

    def set_value(self,value):
        self.value = value
    def checkNegatives(self):
        for i in self.probabilities:
                if i <= 0:
                    print('no negatives fam')
                    raise Exception
    def get_value(self):
        return self.value 
    def showProb(self):
        return self.probabilities
    def checkSum(self):
        sum = 0
        for i in self.probabilities:
            sum += i
        if sum < 1:
            raise Exception
    def checkType(self):
        for i in self.probabilities:
            if type(i) != int:
                

dice_instance = Dice(6,[1,2,1,4,5,6])
print(dice_instance.showProb())
dice_instance.roll()
print(dice_instance.get_value())
# dice_instance = Dice(20)
# print(dice_instance.showProb())
# dice_instance.roll()
# print(dice_instance.get_value())