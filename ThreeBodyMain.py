import numpy as np

'''
MEASUREMENT UNITS:

Mass: Earth Mass (5.9722 x 10^24kg) (5.9722Rg Ronnagrams)
Distance: Solar Radius (695,700,000m meters)
Distance: Earth Radius (6378100m meters)
Time: Earth Day (86400 seconds)

'''


'''
CONSTANTS:

GRAVITATIONAL_CONSTANT: 6.674x10^-11 N*m^2/kg^2

'''

GRAVITATIONAL_CONSTANT = 6.6743e-11      # (N * m^2/kg^2)
EARTH_MASS_TO_KILOGRAM = 5.9722e24
SUN_MASS_TO_KILOGRAM = 1.989e30
SOLAR_RADIUS_TO_METER = 695700000
EARTH_RADIUS_TO_METER = 6378100
DAY_TO_SECOND = 86400




'''
FORMULAE:

Gravitational Force = (Gravitational Constant x Mass of first object x Mass of the second object) / (Distance between the centre of two bodies ^ 2).
Gravitational Force = (6.674e-11 * Mass1(Kg) * Mass2(Kg)) / (DistanceBetween(m) ^ 2) 
'''

def calc_absolute_distance(vector_1, vector_2):
    return (absolute_3d(vector_1 - vector_2))

def calc_gravitational_force(mass1, mass2, distance):
    return (GRAVITATIONAL_CONSTANT * mass1 * mass2) / (distance ** 2)

def absolute_3d(vector):
    return np.sqrt(np.sum(np.square(vector)))

def normalize_3d(vector):
    return np.divide(vector, absolute_3d(vector))


class Body:

    def __init__(self, mass, radius, position, velocity, acceleration):
        self.mass = mass
        self.diameter = radius * 2
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.radius = radius
        self.volume = (4/3) * np.pi * (radius ** 3)
    

    # Acceleration = Force / Mass
    def apply_force(self, force, direction):
        self.acceleration += (np.multiply(normalize_3d(direction), force) / self.mass)
        return
    
    def vector_distance_to(self, body_2):
        return (body_2.position - self.position)
    
    def absolute_distance_to(self, body_2):
        return absolute_3d(self.vector_distance_to(body_2))

    
    def gravitate_to(self, body_2):
        vector_towards = self.vector_distance_to(body_2)
        gravitational_force = calc_gravitational_force(self.mass, body_2.mass, absolute_3d(vector_towards))
        self.apply_force(gravitational_force, vector_towards)
        return
    
    def gravitate_between(self, body_2):
        vector_towards = self.vector_distance_to(body_2)
        gravitational_force = calc_gravitational_force(self.mass, body_2.mass, absolute_3d(vector_towards))
        self.apply_force(gravitational_force, vector_towards)
        body_2.apply_force(gravitational_force, vector_towards * -1)
        return
    
    def accelerate_velocity_day(self):
        self.velocity += self.acceleration * DAY_TO_SECOND
        return
    
    def update_position_day(self):
        self.position += self.velocity * DAY_TO_SECOND
        return
    
    def get_map_coordinates(self):
        x = 0
        y = 0
        







class Star(Body):

    def __init__(self, mass, radius, position, velocity, acceleration, luminance, colour, stage):
        super().__init__(mass, radius, position, velocity, acceleration)
        self.luminance = luminance
        self.colour = colour
        self.stage = stage



class Planet(Body):

    def __init__(self, mass, radius, position, velocity, acceleration, colour):
        super().__init__(mass, radius, position, velocity, acceleration)
        self.colour = colour




Sun = Star(SUN_MASS_TO_KILOGRAM, SOLAR_RADIUS_TO_METER, np.array([0,0,0], dtype='float64'), np.array([0,0,0], dtype='float64'), np.array([0,0,0], dtype='float64'), 1, 1, 1)
Earth = Planet(EARTH_MASS_TO_KILOGRAM, EARTH_RADIUS_TO_METER, np.array([149600000000,0,0], dtype='float64'), np.array([0,29780,0], dtype='float64'), np.array([0,0,0], dtype='float64'), "green")

working_set = [Sun, Earth]

map = [["_" for i in range(50)] for j in range(50)]



for i in range(365):
    working_set[1].gravitate_to(working_set[0])
    
    for orbit_body in working_set:
        orbit_body.accelerate_velocity_day()
        orbit_body.update_position_day()

    print("Distance from Sun: ", Earth.absolute_distance_to(Sun))


