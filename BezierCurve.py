import numpy as np
from utils import Point

class BezierCurve:
    def __init__(self, p0, p1, p2):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        
        self.t = 0.0

    def foward(self, t):
        self.t = t
        x = ((1-t)**2)*self.p0.x + 2*(1-t)*t*self.p1.x + (t**2)*self.p2.x
        y = ((1-t)**2)*self.p0.y + 2*(1-t)*t*self.p1.y + (t**2)*self.p2.y
        return Point(x, y)
    
    def set_p0(self, p0):
        self.p0 = p0

    def set_p1(self, p1):
        self.p1 = p1

    def set_p2(self, p2):
        self.p2 = p2

    def get_control_points(self):
        return [(self.p0.x, self.p0.y), (self.p1.x, self.p1.y), (self.p2.x, self.p2.y)]