# 11.1_part2
# Create a test Class to test our 11.1 function
    # Do not forget to import unittest as well as the function in 11.1

import unittest
# importing functions Python does not really like numbered titled programs
from city_function import city_country
from city_function_pop import city_country_pop,city_country_pop2
#class TestNamingFormat(unittest.TestCase):
#    """Testing the naming format for city and country naming pairs."""
#
#    def test_city_country(self):
#        """Formatting test to see if 'Santiago, Chile' will work."""
#        proper_format = city_country('santiago', 'chile')
#        self.assertEqual(proper_format, 'Santiago, Chile')
#
#if __name__=='__main__':
#    unittest.main()

#------------------------------------------------------------------------------------------------------

# Use the above test to test your the new city population function
# 11.2 Population test

class TestNamingFormat(unittest.TestCase):
    """Testing the naming format for city and country naming pairs."""

    def test_city_country(self):
        """Formatting test to see if 'Santiago, Chile' will work."""
        proper_format = city_country('santiago', 'chile')
        self.assertEqual(proper_format, 'Santiago, Chile')

    def test_city_country_pop(self):
        """Formatting test to see if 'Santiago, Chile - Population 500000' will work."""
        proper_format = city_country_pop2('santiago', 'chile', 500_000)
        self.assertEqual(proper_format, 'Santiago, Chile - Population 500000')

if __name__=='__main__':
    unittest.main()