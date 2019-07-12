# Import random from standard library
import random

# Create and define product class
class Product:
    # Define initiate method
    def __init__(self, name=None, price=10, weight=20,
                 flammability=0.5, identifier=(random.randint(1000000,9999999))):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    # Define function for stealability
    def stealability(self):
        x = self.price/self.weight
        if x < 0.5:
            print('Not so stealable...')
        elif x >= 1:
            print('Very stealable!')
        else:
            print('Kinda stealable.')
    
    # Define fuction for explode
    def explode(self):
        y = self.flammability * self.weight
        if y < 10:
            print('...fizzle.')
        elif y >= 50:
            print('...BABOOM!!')
        else:
            print('...boom!')

# Create subclass of product named Glove
class BoxingGlove(Product):
    # Initiate subclass
    def __init__(self, name=None, price=10, weight=10,
                 flammability=0.5, identifier=(random.randint(1000000,9999999))):
        super(BoxingGlove, self).__init__(name=name, price=price, 
                                    weight=weight, flammability=flammability, 
                                    identifier=identifier)

    # Create method override for explode
    def explode(self):
        print("...it's a glove.")

    # Create method for punch
    def punch(self):
        if self.weight < 5:
            print('That tickles.')
        elif self.weight >= 15:
            print('OUCH!')
        else:
            print('Hey that hurt!')