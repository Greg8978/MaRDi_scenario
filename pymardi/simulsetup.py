import sys
import time
import math
import json
from random import random

sys.path.insert(0, '/home/ferreira/openrobots/share/modules/python')
from morse.builder import *

class PositionSetter:
    def __init__(self):
        # x,y,z centroid coords
        self.centroids = { "human_table" : [ 4, 6.8, 0.8 ],
                           "kitchen_table" : [ 8.5, 11, 1.4],
                           "livingroom_table" : [7.4, 6.7, 1.2],
                           "bedroom_table" : [2.4, 12, 0.8],
                           "bedroom_shelf" : [2.3, 9.2, 1.2],
                           "bedroom_chest" : [5.6, 11.1, 1.4],
                           "bedroom_console" : [4, 12.9, 1.4],
                           "kitchen_cupboard" : [6.1, 10.6, 1.4]
                         }
        # x,y centroid diameters
        self.radius = { "human_table" : [ 0.2, 0.2 ],
                           "kitchen_table" : [ 0.2, 0.2],
                           "livingroom_table" : [ 0.2, 0.2],
                           "bedroom_table" : [0.1, 0.1],
                           "bedroom_shelf" : [0.1, 0.1],
                           "bedroom_chest" : [0.1, 0.1],
                           "bedroom_console" : [0.1, 0.1],
                           "kitchen_cupboard" : [0.1, 0.1]
                       }
    def setPosition(self, morsobj, idpos):
        try:
            self.centroids[idpos]
            self.radius[idpos]
        except Exception:
            idpos = "human_table"
        x = self.centroids[idpos][0] + (1.0 - 2.0 * random()) * self.radius[idpos][0]
        y = self.centroids[idpos][1] + (1.0 - 2.0 * random()) * self.radius[idpos][1]
        z = self.centroids[idpos][2]
        morsobj.translate(x=x, y=y, z=z)


if __name__ == "__main__":
    pass
