from unittest import TestCase
from unittest.mock import patch
from geektrust import Geektrust
from family_tree import constants


class TestGeektrust(TestCase):

    def setUp(self):
        self.geektrust_app = Geektrust()

    def test_construct_add_child_method_call(self):
        result_one_arg = self.geektrust_app.construct_add_child_method_call(
            "Shan")
        result_two_args = self.geektrust_app.construct_add_child_method_call(
            "Shan", "Male")
        result_three_args = self.geektrust_app.construct_add_child_method_call(
            "Mother", "Shan", "Male")
        self.assertEqual(result_one_arg, None)
        self.assertEqual(
            result_two_args,
            'self.family_tree.add_child("Shan", "Male")'
        )
        self.assertEqual(
            result_three_args,
            'self.family_tree.add_child("Shan", "Male", "Mother")'
        )

    def test_construct_add_spouse_method_call(self):
        result_two_args = self.geektrust_app.construct_add_spouse_method_call(
            "Wife", "Female")
        result_three_args = self.geektrust_app.construct_add_spouse_method_call(  # noqa
            "Husband", "Wife", "Female")
        self.assertEqual(result_two_args, None)
        self.assertEqual(result_three_args, 'self.family_tree.add_spouse("Wife", "Female", "Husband")')  # noqa

    def test_construct_get_relationship_method_call(self):
        result_one_args = self.geektrust_app.construct_get_relationship_method_call(  # noqa
            "Name")
        result_two_args = self.geektrust_app.construct_get_relationship_method_call(  # noqa
            "Name", "Brother-In-Law")
        result_invalid_args = self.geektrust_app.construct_get_relationship_method_call(  # noqa
            "Name", "Random")
        self.assertEqual(result_one_args, None)
        self.assertEqual(
            result_two_args,
            'self.family_tree.get_relationship("Name", "brother_in_law")'
        )
        self.assertEqual(result_invalid_args, None)

    @patch(
        'geektrust.Geektrust.construct_add_child_method_call',
        return_value='self.family_tree.add_child("Member", "Male", "Mother")'
    )
    @patch(
        'geektrust.Geektrust.construct_add_spouse_method_call',
        return_value='self.family_tree.add_spouse("Wife", "Female", "Spouse")'
    )
    @patch(
        'geektrust.Geektrust.construct_get_relationship_method_call',
        return_value='self.family_tree.get_relationship("Member", "brother_in_law")'  # noqa
    )
    def test_translate(self, mock_construct_get_relationship_method_call,
                       mock_construct_add_spouse_method_call,
                       mock_construct_add_child_method_call):
        with patch('builtins.open', create=True) as mock_open:  # noqa
            mock_open.return_value.__enter__.return_value.readlines.return_value = (  # noqa
                'ADD_CHILD Mother Member Male',
                'ADD_SPOUSE Spouse Wife Female',
                'GET_RELATIONSHIP Member Brother-In-Law'
            )
            result = self.geektrust_app.translate('dummy_file.txt')
            self.assertEqual(
                result,
                [
                    'self.family_tree.add_child("Member", "Male", "Mother")',
                    'self.family_tree.add_spouse("Wife", "Female", "Spouse")',
                    'self.family_tree.get_relationship("Member", "brother_in_law")'  # noqa
                ]
            )

    @patch(
        'geektrust.FamilyTree.get_relationship',
        return_value=constants.NONE
    )
    @patch(
        'geektrust.FamilyTree.add_spouse',
        return_value=constants.SPOUSE_ADDITION_SUCCEEDED
    )
    @patch(
        'geektrust.FamilyTree.add_child',
        return_value=constants.CHILD_ADDITION_SUCCEEDED
    )
    def test_execute(self, mock_add_child, mock_add_spouse,
                     mock_get_relationship):
        results = self.geektrust_app.execute(
            [
                'self.family_tree.add_child("Member", "Male", "Mother")',
                'self.family_tree.add_spouse("Wife", "Female", "Spouse")',
                'self.family_tree.get_relationship("Member", "brother_in_law")'
            ]
        )
        self.assertEqual(
            results,
            [
                constants.CHILD_ADDITION_SUCCEEDED,
                constants.SPOUSE_ADDITION_SUCCEEDED,
                constants.NONE
            ]
        )
        mock_add_child.assert_called_with("Member", "Male", "Mother")
        mock_add_spouse.assert_called_with("Wife", "Female", "Spouse")
        mock_get_relationship.assert_called_with("Member", "brother_in_law")

    @patch('builtins.print')
    def test_log(self, mock_print):
        self.geektrust_app.log(
            [
                constants.CHILD_ADDITION_SUCCEEDED,
                constants.SPOUSE_ADDITION_SUCCEEDED,
                constants.NONE
            ]
        )
        mock_print.assert_called_with(constants.NONE)

    @patch('geektrust.Geektrust.execute')
    @patch('geektrust.Geektrust.translate', return_value=['RESULT'])
    def test_setup(self, mock_translate, mock_execute):
        self.geektrust_app.setup('filename')
        mock_translate.assert_called_with('filename')
        mock_execute.assert_called_with(['RESULT'])
