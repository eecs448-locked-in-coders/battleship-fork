from src.grid import Grid
from src.ship import Ship, ShipNode

class GameState:
    """
        This class stores information about the current state of the game.
        It allows this information to be sent from the controller to the view.
    """
    
    def __init__(self):
        self.grid = Grid()
        self.shipDir = 0 # Direction of the ship currently being placed (index of c.DIRS)
        self.lenShip = 1 # Length of the ship to place next
        self.numShipsPerPlayer = 0
        self.p1Ships = []
        self.p2Ships = []
        self.is_P1_turn = False
        self.is_placing = False
        self.is_shooting = False
        self.msg = "" # Message to display below game board