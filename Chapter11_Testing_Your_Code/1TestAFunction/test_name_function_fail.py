### A failing test ###

    # testing the revised get_formatted_name function (which added a middle name argument)

import unittest
from name_function import get_formatted_name2
from name_function import get_formatted_name3

#class NamesTestCase(unittest.TestCase):
#    """Tests for 'name_function.py'."""
#    
#    def test_first_last_name(self):
#        """Do names like 'Janis Joplin' work?"""
#        # Since our test only has two names entered this test should fail as there is no 
#            # 3 argument {last}.
#        formatted_name = get_formatted_name2('janis', 'joplin')
#        self.assertEqual(formatted_name, 'Janis Joplin')
#
#if __name__ == '__main__':
#    unittest.main()

#---------------------------------------------------------------------------------------------------

### Responding to a failed test ###
    
    # When trying to decided what to do with a failed test, it is important to know that best practice is to not change how the test functions but augment the function itself to work the way you need and still pass. 

    # Lets redesign get_formatted_name to allow first and last names as well

# Test to see if our revisions worked. 
#class NamesTestCase(unittest.TestCase):
#    """Tests for 'name_function.py'."""
#    
#    def test_first_last_name(self):
#        """Do names like 'Janis Joplin' work?"""
#        formatted_name = get_formatted_name3('janis', 'joplin')
#        self.assertEqual(formatted_name, 'Janis Joplin')
#
#if __name__ == '__main__':
#    unittest.main()

#---------------------------------------------------------------------------------------------------

### Adding new tests ###

    # Now lets include another test to see if our function works properly with middle names added.

# Test to see if last names will also be formatted as well. 
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name3('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name3('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()