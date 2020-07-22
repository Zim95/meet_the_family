from unittest import TestCase
from family_tree.member import Member
from family_tree.family_tree import FamilyTree


class TestFamilyTree(TestCase):

    def setUp(self):
        self.ftree = FamilyTree()
    
    def test_add_child(self):
        result = self.ftree.add_child("Father", "Male")
        self.assertEqual(result, "CHILD_ADDITION_SUCCEDED")
        self.assertEqual(self.ftree.family_tree.get("Father", None) is not None,
            True)

        self.assertEqual(self.ftree.add_child("Zim", "Male", "Mother"), "PERSON_NOT_FOUND")
        self.assertEqual(self.ftree.add_child("Zim", "Male", "Father"), "CHILD_ADDITION_FAILED")

        mother = Member(2, "Mother", "Female")
        mother.spouse = self.ftree.family_tree["Father"]
        self.ftree.family_tree["Father"].set_spouse(mother)
        self.ftree.family_tree["Mother"] = mother

        self.assertEqual(self.ftree.add_child("Zim", "Male", "Mother"), "CHILD_ADDITION_SUCCEDED")
        self.assertEqual(self.ftree.family_tree.get("Zim", None) is not None,
            True)