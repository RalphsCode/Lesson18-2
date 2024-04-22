list_of_manufacturers = {}

class Boats:
    """A class to make boat manufacturer objects"""

    def __init__(self, mode, manufacturer):
        self.mode = mode                # first one is assigned, second is the argument.
        self.manufacturer = manufacturer
        list_of_manufacturers[self.manufacturer] = self.mode

    def sail_manufacturers():
        """Prints the sailboat manufacturers"""
        print('Here is a list of Sailboat Manufacturers:')
        print('Type\t Manufacturer')
        for k,v in list_of_manufacturers.items():
            if v == 'sail':
                print(v, '\t', k)

    def __repr__(self):
        return f'Boat type: {self.mode}, Manufacturer: {self.manufacturer}

"""
beneteau = Boats('sail', 'beneteau')

isinstance(beneteau, Boats)     # True

Boats.sail_manufacturers()

Here is a list of Sailboat Manufacturers:
Type	 Manufacturer
sail 	 beneteau
"""