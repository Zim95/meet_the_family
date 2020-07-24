from family_tree.member import Member, Gender
from family_tree import constants


class FamilyTree:

    def __init__(self):
        self.family_tree = {}

    def add_child(self, name, gender, mother_name=None):
        _id = len(self.family_tree.keys()) + 1
        member = Member(_id, name, gender)
        if not self.family_tree:
            self.family_tree[name] = member
            return constants.CHILD_ADDITION_SUCCEEDED

        if name in self.family_tree:
            return constants.CHILD_ADDITION_FAILED

        mother = self.family_tree.get(mother_name, None)
        if not mother:
            return constants.PERSON_NOT_FOUND
        if mother.gender != Gender.female:
            return constants.CHILD_ADDITION_FAILED

        father = mother.spouse
        if not father:
            return constants.CHILD_ADDITION_FAILED

        try:
            member.set_mother(mother)
            member.set_father(father)
            self.family_tree[mother_name].add_child(member)
            self.family_tree[father.name].add_child(member)
            self.family_tree[name] = member
            return constants.CHILD_ADDITION_SUCCEEDED
        except ValueError:
            return constants.CHILD_ADDITION_FAILED

    def add_spouse(self, name, gender, spouse_name):
        _id = len(self.family_tree.keys()) + 1
        member = Member(_id, name, gender)
        if not self.family_tree:
            return constants.SPOUSE_ADDITION_FAILED

        if name in self.family_tree:
            return constants.SPOUSE_ADDITION_FAILED

        spouse = self.family_tree.get(spouse_name, None)
        if not spouse:
            return constants.PERSON_NOT_FOUND
        if spouse.gender == member.gender:
            return constants.SPOUSE_ADDITION_FAILED
        if spouse.spouse is not None:
            return constants.SPOUSE_ADDITION_FAILED

        try:
            member.set_spouse(self.family_tree[spouse.name])
            self.family_tree[spouse.name].set_spouse(member)
            self.family_tree[name] = member
            return constants.SPOUSE_ADDITION_SUCCEEDED
        except ValueError:
            return constants.SPOUSE_ADDITION_FAILED

    def get_relationship(self, name, relationship_type):
        member = self.family_tree.get(name, None)
        if not member:
            return constants.PERSON_NOT_FOUND
        result = member.get_relationship(relationship_type)
        if not result:
            return constants.NONE
        else:
            return ' '.join(
                list(
                    map(
                        lambda x: x.name,
                        sorted(result, key=lambda key: key.id)
                    )
                )
            )
