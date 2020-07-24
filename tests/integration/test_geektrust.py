from unittest import TestCase
from unittest.mock import patch, mock_open
from geektrust import Geektrust


class TestGeektrust(TestCase):

    def setUp(self):
        self.geektrust_app = Geektrust()

    def test_translate(self):
        with patch('builtins.open', create=True) as mock_open:
            mock_open.return_value.__enter__.return_value.readlines.return_value = (
                'ADD_CHILD Shan Male',
                'ADD_CHILD Shan',
                'ADD_CHILD Mother Member Male',
                'ADD_SPOUSE Spouse Wife Female',
                'ADD_SPOUSE Spouse Wife',
                'GET_RELATIONSHIP Member Brother-In-Law',
                'GET_RELATIONSHIP Member Random',
                'GET_RELATIONSHIP Member'
            )
            result = self.geektrust_app.translate('dummy_file.txt')
            self.assertEqual(
                result,
                [
                    'self.family_tree.add_child("Shan", "Male")',
                    'self.family_tree.add_child("Member", "Male", "Mother")',
                    'self.family_tree.add_spouse("Wife", "Female", "Spouse")',
                    'self.family_tree.get_relationship("Member", "brother_in_law")'
                ]
            )
