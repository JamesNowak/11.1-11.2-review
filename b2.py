# Imports the OfficeFurniture super class
from a1 import OfficeFurniture


# this sets the subclass
class Desk(OfficeFurniture):
    def __init__(self, catagory, material, length, width, height, price, location_of_drawers, count):

        # calls the superclass and pass the arguments
        OfficeFurniture.__init__(self, catagory, material, length, width, height, price)

        # I initialize the location_of_drawers and count attributes
        self.location_of_drawers = location_of_drawers
        self.count = count
# This is where the mutators and accessors are created for the count and location_of_drawers attributes

    def set_location_of_drawers(self, location_of_drawers):
        self.location_of_drawers = location_of_drawers

    def set_count(self, count):
        self.count = count

    def get_location_of_drawers(self):
        return self.location_of_drawers

    def get_count(self):
        return self.count
