from unittest import TestCase
from geektrust import Geektrust


class TestGeektrust(TestCase):

    def setUp(self):
        self.geektrust_app = Geektrust()

    def test_translate(self):
        result = self.geektrust_app.translate('setup.instructions.txt')
        self.assertEqual(
            result,
            [
                'self.family_tree.add_child("Shan", "Male")',
                'self.family_tree.add_spouse("Anga", "Female", "Shan")',
                'self.family_tree.add_child("Chit", "Male", "Anga")',
                'self.family_tree.add_child("Ish", "Male", "Anga")',
                'self.family_tree.add_child("Vich", "Male", "Anga")',
                'self.family_tree.add_child("Aras", "Male", "Anga")',
                'self.family_tree.add_child("Satya", "Female", "Anga")',
                'self.family_tree.add_spouse("Amba", "Female", "Chit")',
                'self.family_tree.add_spouse("Lika", "Female", "Vich")',
                'self.family_tree.add_spouse("Chitra", "Female", "Aras")',
                'self.family_tree.add_spouse("Vyan", "Male", "Satya")',
                'self.family_tree.add_child("Dritha", "Female", "Amba")',
                'self.family_tree.add_child("Tritha", "Female", "Amba")',
                'self.family_tree.add_child("Vritha", "Male", "Amba")',
                'self.family_tree.add_child("Vila", "Female", "Lika")',
                'self.family_tree.add_child("Chika", "Female", "Lika")',
                'self.family_tree.add_child("Jnki", "Female", "Chitra")',
                'self.family_tree.add_child("Ahit", "Male", "Chitra")',
                'self.family_tree.add_child("Asva", "Male", "Satya")',
                'self.family_tree.add_child("Vyas", "Male", "Satya")',
                'self.family_tree.add_child("Atya", "Female", "Satya")',
                'self.family_tree.add_spouse("Jaya", "Male", "Dritha")',
                'self.family_tree.add_spouse("Arit", "Male", "Jnki")',
                'self.family_tree.add_spouse("Satvy", "Female", "Asva")',
                'self.family_tree.add_spouse("Krpi", "Female", "Vyas")',
                'self.family_tree.add_child("Yodhan", "Male", "Dritha")',
                'self.family_tree.add_child("Laki", "Male", "Jnki")',
                'self.family_tree.add_child("Lavnya", "Female", "Jnki")',
                'self.family_tree.add_child("Vasa", "Male", "Satvy")',
                'self.family_tree.add_child("Kriya", "Male", "Krpi")',
                'self.family_tree.add_child("Krithi", "Female", "Krpi")'
            ]
        )

    def test_execute(self):
        result = self.geektrust_app.execute(
            [
                'self.family_tree.add_child("Shan", "Male")',
                'self.family_tree.add_spouse("Anga", "Female", "Shan")',
                'self.family_tree.add_child("Chit", "Male", "Anga")',
                'self.family_tree.add_child("Ish", "Male", "Anga")',
                'self.family_tree.add_child("Vich", "Male", "Anga")',
                'self.family_tree.add_child("Aras", "Male", "Anga")',
                'self.family_tree.add_child("Satya", "Female", "Anga")',
                'self.family_tree.add_spouse("Amba", "Female", "Chit")',
                'self.family_tree.add_spouse("Lika", "Female", "Vich")',
                'self.family_tree.add_spouse("Chitra", "Female", "Aras")',
                'self.family_tree.add_spouse("Vyan", "Male", "Satya")',
                'self.family_tree.add_child("Dritha", "Female", "Amba")',
                'self.family_tree.add_child("Tritha", "Female", "Amba")',
                'self.family_tree.add_child("Vritha", "Male", "Amba")',
                'self.family_tree.add_child("Vila", "Female", "Lika")',
                'self.family_tree.add_child("Chika", "Female", "Lika")',
                'self.family_tree.add_child("Jnki", "Female", "Chitra")',
                'self.family_tree.add_child("Ahit", "Male", "Chitra")',
                'self.family_tree.add_child("Asva", "Male", "Satya")',
                'self.family_tree.add_child("Vyas", "Male", "Satya")',
                'self.family_tree.add_child("Atya", "Female", "Satya")',
                'self.family_tree.add_spouse("Jaya", "Male", "Dritha")',
                'self.family_tree.add_spouse("Arit", "Male", "Jnki")',
                'self.family_tree.add_spouse("Satvy", "Female", "Asva")',
                'self.family_tree.add_spouse("Krpi", "Female", "Vyas")',
                'self.family_tree.add_child("Yodhan", "Male", "Dritha")',
                'self.family_tree.add_child("Laki", "Male", "Jnki")',
                'self.family_tree.add_child("Lavnya", "Female", "Jnki")',
                'self.family_tree.add_child("Vasa", "Male", "Satvy")',
                'self.family_tree.add_child("Kriya", "Male", "Krpi")',
                'self.family_tree.add_child("Krithi", "Female", "Krpi")'
            ]
        )
        self.assertEqual(
            result,
            [
                'CHILD_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED'
            ]
        )
