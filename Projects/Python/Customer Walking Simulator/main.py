import pygame
from simulator.assets import MapDrawer
from simulator import Simulator


if __name__ == "__main__":
    pygame.init()
    map_drawer = MapDrawer(1900, 900)
    simulator_obj = Simulator(map_drawer)
    simulator_obj.run()
