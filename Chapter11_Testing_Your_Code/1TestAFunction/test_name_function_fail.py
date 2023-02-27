### A failing test ###

    # testing the revised get_formatted_name function (which added a middle name argument)

import unittest
from name_function import get_formatted_name2

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        # Since our test only has two names entered this test should fail as there is no 
            # 3 argument {last}.
        formatted_name = get_formatted_name2('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()

