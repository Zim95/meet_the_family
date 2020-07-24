from unittest import TestCase
from unittest.mock import patch, Mock

from family_tree.family_tree import FamilyTree
from family_tree.member import Member, Gender
from family_tree import constants
from tests.unit import create_fake_member


class TestFamilyTree(TestCase):

    def setUp(self):
        self.ftree = FamilyTree()

    def test_initialization(self):
        self.assertEqual(self.ftree.family_tree, {})

    @patch('family_tree.family_tree.Member', return_value=create_fake_member(
        id=1, name="Zim", gender=Gender.male))
    def test_add_child(self, mock_member):
        # if tree is empty
        result = self.ftree.add_child("Zim", "Male", "Mother")
        mock_member.assert_called_with(1, "Zim", "Male")

        self.assertEqual(
            isinstance(self.ftree.family_tree.get("Zim", None), Mock),
            True
        )
        self.assertEqual(result, constants.CHILD_ADDITION_SUCCEEDED)

        # if either mother/ father do not exist
        mother = create_fake_member(id=2, name="Mother", gender=Gender.female)
        fakemother = create_fake_member(
            id=4, name="Fakemother", gender=Gender.male)
        father = create_fake_member(id=3, name="Father", gender=Gender.male)

        self.assertEqual(
            self.ftree.add_child("Zim2", "Male", "Mother"),
            constants.PERSON_NOT_FOUND
        )
        self.ftree.family_tree['Fakemother'] = fakemother
        self.assertEqual(
            self.ftree.add_child("Zim2", "Male", "Fakemother"),
            constants.CHILD_ADDITION_FAILED
        )
        self.ftree.family_tree['Mother'] = mother
        self.assertEqual(
            self.ftree.add_child("Zim2", "Male", "Mother"),
            constants.CHILD_ADDITION_FAILED
        )
        self.ftree.family_tree['Father'] = father
        self.ftree.family_tree['Mother'].spouse = father
        self.ftree.family_tree['Father'].spouse = mother

        self.assertEqual(
            self.ftree.add_child("Zim2", "Male", "Mother"),
            constants.CHILD_ADDITION_SUCCEEDED
        )
        self.assertEqual(
            self.ftree.add_child("Zim2", "Male", "Mother"),
            constants.CHILD_ADDITION_FAILED
        )
        self.assertEqual(
            isinstance(
                self.ftree.family_tree.get("Zim2", None),
                Mock
            ),
            True
        )

    @patch('family_tree.family_tree.Member', return_value=create_fake_member(
        id=1, name="Wife", gender=Gender.female))
    def test_add_spouse(self, mock_member):
        # if tree is empty
        result = self.ftree.add_spouse("Wife", "Female", "Zim")
        mock_member.assert_called_with(1, "Wife", "Female")

        self.assertEqual(
            self.ftree.family_tree.get("Zim", None),
            None
        )
        self.assertEqual(result, constants.SPOUSE_ADDITION_FAILED)

        # if spouse does not exist
        dummy_member = create_fake_member(
            id=0, name="DummyMember", gender=Gender.male)
        self.ftree.family_tree["DummyMember"] = dummy_member
        spouse_a = create_fake_member(id=2, name="Zim", gender=Gender.male)
        spouse_b = create_fake_member(
            id=3, name="FakeMember", gender=Gender.female)
        spouse_c = create_fake_member(
            id=3, name="MarriedMember", gender=Gender.male, spouse=spouse_b)

        self.assertEqual(
            self.ftree.add_spouse("Wife", Gender.female, "Zim"),
            constants.PERSON_NOT_FOUND
        )
        self.ftree.family_tree["Zim"] = spouse_a
        self.ftree.family_tree["FakeMember"] = spouse_b
        self.ftree.family_tree["MarriedMember"] = spouse_c

        self.assertEqual(
            self.ftree.add_spouse("Wife", Gender.female, "FakeMember"),
            constants.SPOUSE_ADDITION_FAILED
        )
        self.assertEqual(
            self.ftree.add_spouse("Wife", Gender.female, "MarriedMember"),
            constants.SPOUSE_ADDITION_FAILED
        )
        self.assertEqual(
            self.ftree.add_spouse("Wife", Gender.female, "Zim"),
            constants.SPOUSE_ADDITION_SUCCEEDED
        )
        self.assertEqual(
            self.ftree.add_spouse("Wife", Gender.female, "Zim"),
            constants.SPOUSE_ADDITION_FAILED
        )

    @patch('family_tree.family_tree.Member.get_relationship', side_effect=[
        [],
        [
            create_fake_member(id=1, name="Zim"),
            create_fake_member(id=2, name="Wife")
        ]
    ])
    def test_get_relationship(self, mock_get_relationship):
        self.assertEqual(
            self.ftree.get_relationship("Zim", "brother_in_law"),
            constants.PERSON_NOT_FOUND
        )
        self.ftree.family_tree["Zim"] = Member(1, "Zim", "Male")
        self.assertEqual(
            self.ftree.get_relationship("Zim", "brother_in_law"),
            constants.NONE
        )
        self.assertEqual(
            self.ftree.get_relationship("Zim", "brother_in_law"),
            "Zim Wife"
        )
