import random

class Dice:
    random.seed(9001)
    def __init__(self,sides,probabilities=[]):
        self.sides = sides
        self.value = 0
        self.probabilities = probabilities
        self.checkType()
        self.checkNegatives()
        if self.probabilities == []:
            pass
        else:
            self.checkSum()
        
        
       
    def roll(self):
        if len(self.probabilities) == 0:
            self.value = random.randint(1,self.sides+1)
        else:
            self.checkNegatives()
            numbers = [ i for i in range(1,self.sides+1)]
            numbers_after = []
            for i in range(self.sides):
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
                if i < 0:
                    raise Exception('negative probabilities not allowed')
    
    def get_value(self):
        return self.value 
    
    def showProb(self):
        return self.probabilities
    
    def checkSum(self):
        sum = 0
        for i in self.probabilities:
            sum += i
        if sum < 0:
            raise Exception('probability sum must be greater than 0')
    
    def checkType(self):
        for i in self.probabilities:
            if type(i) != int:
                raise Exception('This is not a integer')
    
    def setProbabilities(self,new_probabilities):
        self.probabilities = new_probabilities
                
    def checkEqualSides(self):
        if len(self.probabilities) > 0 and len(self.probabilities) != self.sides:
            raise Exception

class DiceFactory:
    def __init__(self,num_of_sides):
        self.num_of_sides = num_of_sides
    def make_die(self):
        dice_instance = Dice(self.num_of_sides)
        return dice_instance
        