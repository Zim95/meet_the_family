from unittest import TestCase
from family_tree.member import Member


class TestMember(TestCase):

    def setUp(self):
        self.member = Member(1, "Zim", "Male")
        self.mother = Member(2, "Mother", "Female")
        self.father = Member(3, "Dad", "Male")
        self.mothers_sister_a = Member(4, "MaternalAuntA", "Female")
        self.mothers_sister_b = Member(5, "MaternalAuntB", "Female")
        self.mothers_brother_a = Member(6, "MaternalUncleA", "Male")
        self.mothers_brother_b = Member(7, "MaternalUncleB", "Male")
        self.fathers_sister_a = Member(8, "PaternalAuntA", "Female")
        self.fathers_sister_b = Member(9, "PaternalAuntB", "Female")
        self.fathers_brother_a = Member(10, "PaternalUncleA", "Male")
        self.fathers_brother_b = Member(11, "PaternalUncleB", "Male")
        self.spouse = Member(12, "Wife", "Female")
        self.brother_a = Member(13, "BrotherA", "Male")
        self.brother_b = Member(14, "BrotherB", "Male")
        self.sister_a = Member(15, "SisterA", "Female")
        self.sister_b = Member(16, "SisterB", "Female")
        self.son_a = Member(17, "SonA", "Male")
        self.son_b = Member(18, "SonB", "Male")
        self.daughter_a = Member(19, "DaughterA", "Female")
        self.daughter_b = Member(20, "DaughterB", "Female")
        self.paternal_grandmother = Member(21, "PaternalGrandmother", "Female")
        self.maternal_grandmother = Member(22, "MaternalGrandmother", "Female")

        # adding our parents
        self.member.set_mother(self.mother)
        self.member.set_father(self.father)

        # adding our siblings
        self.father.add_child(self.brother_a)
        self.father.add_child(self.brother_b)
        self.father.add_child(self.sister_a)
        self.father.add_child(self.sister_b)
        self.father.add_child(self.member)
        self.mother.add_child(self.brother_a)
        self.mother.add_child(self.brother_b)
        self.mother.add_child(self.sister_a)
        self.mother.add_child(self.sister_b)
        self.mother.add_child(self.member)

        # add spouse
        self.member.set_spouse(self.spouse)
        self.spouse.set_spouse(self.member)

        # adding our paternal aunt/uncle s
        self.paternal_grandmother.add_child(self.fathers_sister_a)
        self.paternal_grandmother.add_child(self.fathers_sister_b)
        self.paternal_grandmother.add_child(self.fathers_brother_a)
        self.paternal_grandmother.add_child(self.fathers_brother_b)
        self.paternal_grandmother.add_child(self.father)
        self.father.set_mother(self.paternal_grandmother)

        # adding our maternal aunt/uncle s
        self.maternal_grandmother.add_child(self.mothers_sister_a)
        self.maternal_grandmother.add_child(self.mothers_sister_b)
        self.maternal_grandmother.add_child(self.mothers_brother_a)
        self.maternal_grandmother.add_child(self.mothers_brother_b)
        self.maternal_grandmother.add_child(self.mother)
        self.mother.set_mother(self.maternal_grandmother)

        # adding our sons and daughters
        self.member.add_child(self.son_a)
        self.member.add_child(self.son_b)
        self.member.add_child(self.daughter_a)
        self.member.add_child(self.daughter_b)

    def test_set_methods(self):
        # test parents
        self.assertEqual(self.member.mother.name, "Mother")
        self.assertEqual(self.member.father.name, "Dad")
        self.assertEqual(self.member in self.member.father.children, True)
        self.assertEqual(self.member in self.member.mother.children, True)

        # test siblings
        self.assertEqual(len(self.member.mother.children), 5)
        self.assertEqual(self.brother_a in self.member.mother.children, True)
        self.assertEqual(self.brother_b in self.member.mother.children, True)
        self.assertEqual(self.sister_a in self.member.mother.children, True)
        self.assertEqual(self.sister_b in self.member.mother.children, True)
        self.assertEqual(len(self.member.father.children), 5)
        self.assertEqual(self.brother_a in self.member.father.children, True)
        self.assertEqual(self.brother_b in self.member.father.children, True)
        self.assertEqual(self.sister_a in self.member.father.children, True)
        self.assertEqual(self.sister_b in self.member.father.children, True)

        # test spouse
        self.assertEqual(self.member.spouse.name, "Wife")

        # test paternal/maternal aunts and uncles
        self.assertEqual(len(self.member.mother.mother.children), 5)
        self.assertEqual(
            self.mothers_brother_a in self.member.mother.mother.children, True)
        self.assertEqual(
            self.mothers_brother_b in self.member.mother.mother.children, True)
        self.assertEqual(
            self.mothers_sister_a in self.member.mother.mother.children, True)
        self.assertEqual(
            self.mothers_sister_b in self.member.mother.mother.children, True)
        self.assertEqual(
            self.mother in self.member.mother.mother.children, True)
        self.assertEqual(len(self.member.father.mother.children), 5)
        self.assertEqual(
            self.fathers_brother_a in self.member.father.mother.children, True)
        self.assertEqual(
            self.fathers_brother_b in self.member.father.mother.children, True)
        self.assertEqual(
            self.fathers_sister_a in self.member.father.mother.children, True)
        self.assertEqual(
            self.fathers_sister_b in self.member.father.mother.children, True)
        self.assertEqual(
            self.father in self.member.father.mother.children, True)

        # test children
        self.assertEqual(len(self.member.children), 4)
        self.assertEqual(self.son_a in self.member.children, True)
        self.assertEqual(self.son_b in self.member.children, True)
        self.assertEqual(self.daughter_a in self.member.children, True)
        self.assertEqual(self.daughter_b in self.member.children, True)

    def test_get_relationship_methods(self):
        self.assertEqual(
            len(self.member.get_relationship("paternal_aunt")), 2)
        self.assertEqual(
            len(self.member.get_relationship("paternal_uncle")), 2)
        self.assertEqual(
            len(self.member.get_relationship("maternal_aunt")), 2)
        self.assertEqual(
            len(self.member.get_relationship("maternal_uncle")), 2)
        self.assertEqual(
            len(self.member.get_relationship("siblings")), 4)
        self.assertEqual(
            len(self.member.get_relationship("son")), 2)
        self.assertEqual(
            len(self.member.get_relationship("daughter")), 2)
        self.assertEqual(
            len(self.member.spouse.get_relationship("brother_in_law")), 2)
        self.assertEqual(
            len(self.member.spouse.get_relationship("sister_in_law")), 2)
