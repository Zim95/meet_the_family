from unittest import TestCase
from unittest.mock import patch, Mock

from family_tree.family_tree import FamilyTree
from family_tree.member import Gender
from tests.unit import create_fake_member


class TestFamilyTree(TestCase):

    def setUp(self):
        self.ftree = FamilyTree()

    def test_initialization(self):
        self.assertEqual(self.ftree.family_tree, {})

    @patch('family_tree.family_tree.Member', return_value=create_fake_member(
        id=1, name="Zim", gender="Male"))
    def test_add_child(self, mock_member):
        # if tree is empty
        result = self.ftree.add_child("Zim", "Male", "Mother")
        mock_member.assert_called_with(1, "Zim", "Male")

        self.assertEqual(
            isinstance(self.ftree.family_tree.get("Zim", None), Mock),
            True
        )
        self.assertEqual(result, 'CHILD_ADDITION_SUCCEDED')

        # if either mother/ father do not exist
        mother = create_fake_member(id=2, name="Mother", gender=Gender.female)
        fakemother = create_fake_member(id=4, name="Fakemother", gender=Gender.male)
        father = create_fake_member(id=3, name="Father", gender=Gender.male)
        
        self.assertEqual(self.ftree.add_child("Zim2", "Male", "Mother"), "PERSON_NOT_FOUND")
        self.ftree.family_tree['Fakemother'] = fakemother
        self.assertEqual(self.ftree.add_child("Zim2", "Male", "Fakemother"), "CHILD_ADDITION_FAILED")
        self.ftree.family_tree['Mother'] = mother
        self.assertEqual(self.ftree.add_child("Zim2", "Male", "Mother"), "CHILD_ADDITION_FAILED")
        self.ftree.family_tree['Father'] = father
        self.ftree.family_tree['Mother'].spouse = father
        self.ftree.family_tree['Father'].spouse = mother

        self.assertEqual(self.ftree.add_child("Zim2", "Male", "Mother"), "CHILD_ADDITION_SUCCEDED")
        self.assertEqual(isinstance(self.ftree.family_tree.get("Zim2", None), Mock), True)
