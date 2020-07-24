from unittest import TestCase
from unittest.mock import patch
from geektrust import Geektrust


class TestSystem(TestCase):

    def setUp(self):
        self.geektrust_app = Geektrust()

    @patch('geektrust.Geektrust.log')
    def test_system(self, mock_log):
        self.geektrust_app.main("./instructions.txt")
        mock_log.assert_called_with(
            [
                "CHILD_ADDITION_SUCCEEDED",
                "Aria",
                "Jnki Ahit",
                "PERSON_NOT_FOUND",
                "PERSON_NOT_FOUND",
                "CHILD_ADDITION_FAILED",
                "NONE",
                "Satvy Krpi"
            ]
        )
