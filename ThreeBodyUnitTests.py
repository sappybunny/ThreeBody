import unittest
import numpy as np
import ThreeBodyMain as tb

class TestVector3Methods(unittest.TestCase):

    def test_absolute_3d(self):
        vector_1 = np.array([2, -26, 7])
        self.assertTrue(tb.absolute_3d(vector_1) == 27)
        self.assertFalse(tb.absolute_3d(vector_1) == 25)

    def test_normalize_3d(self):
        vector_1 = np.array([3,-4,5])
        normalized_vector_1 = np.array([3/(5 * np.sqrt(2)), -(2 * np.sqrt(2)/5), 1/np.sqrt(2)])
        np.testing.assert_array_equal(tb.normalize_3d(vector_1), normalized_vector_1)

    def test_calc_absolute_distance(self):
        vector_1 = np.array([7,-4,12])
        vector_2 = np.array([-3,-5,9])
        # xDif = 10, yDif = 1, zDif = 3
        absolute_distance = np.sqrt(110)
        self.assertTrue(tb.calc_absolute_distance(vector_1, vector_2) == absolute_distance)
        self.assertFalse(tb.calc_absolute_distance(vector_1, vector_2) == 12)

    def test_calc_gravitational_force(self):
        mass1 = tb.EARTH_MASS_TO_KILOGRAM
        mass2 = tb.EARTH_MASS_TO_KILOGRAM * 2
        distance = tb.SOLAR_RADIUS_TO_METER
        np.testing.assert_approx_equal(tb.calc_gravitational_force(mass1, mass2, distance), 9836948527918423877727)


class TestBodyMethods(unittest.TestCase):

    def test_apply_force(self):
        force = 10000000000
        body = tb.Body(tb.EARTH_MASS_TO_KILOGRAM, tb.EARTH_RADIUS_TO_METER, np.array([0,0,0], dtype='float64'), np.array([0,0,0], dtype='float64'), np.array([0,0,0], dtype='float64'))
        body.apply_force(force, np.array([1,-2,3]))
        acceleration_scalar = force / tb.EARTH_MASS_TO_KILOGRAM
        # Normalized direction = [1/root(14), -root(2/7), 3/root(14)]
        # Acceleration = Force / Mass = 10000000000 / 5.9722e24 = 1.6744248e-15
        new_acceleration = np.array([1/np.sqrt(14), -np.sqrt(2/7), 3/np.sqrt(14)]) * acceleration_scalar
        np.testing.assert_array_almost_equal(body.acceleration, new_acceleration)
        

if __name__ == '__main__':
    unittest.main(verbosity=2)
