# imports both superclass and subclass
from a1 import OfficeFurniture

from b2 import Desk
# variables that define the furniture
office = OfficeFurniture("chair", "cloth", 20, 20, 36, 200)
desk = Desk("desk", "oak", 80, 30, 36,1000,"left",2)
# desplays all the data entered in the variables
def main():
    print(office.material, office.catagory + ",", office.length, "inch length,",office.width, "inch width,", office.height, "inch height, costs", office.price, "dollars." )
    print(desk.material, desk.catagory + ",", desk.length, "inch length,",desk.width, "inch width,", desk.height, "inch height,","drawers on", desk.location_of_drawers,"side,",desk.count, "drawers,", "costs", desk.price, "dollars." )
#calls the code in one command
main()
