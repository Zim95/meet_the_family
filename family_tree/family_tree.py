from family_tree.member import Member, Gender


class FamilyTree:

    def __init__(self):
        self.family_tree = {}

    def add_child(self, name, gender, mother_name=None):
        _id = len(self.family_tree.keys()) + 1
        member = Member(_id, name, gender)
        if not self.family_tree:
            self.family_tree[name] = member
            return 'CHILD_ADDITION_SUCCEDED'
        
        mother = self.family_tree.get(mother_name, None)
        if not mother:
            return 'PERSON_NOT_FOUND'
        if mother.gender != Gender.female:
            return 'CHILD_ADDITION_FAILED'

        father = mother.spouse
        if not father:
            return 'CHILD_ADDITION_FAILED'

        member.set_mother(mother)
        member.set_father(father)
        self.family_tree[mother_name].add_child(member)
        self.family_tree[father.name].add_child(member)
        self.family_tree[name] = member
        return 'CHILD_ADDITION_SUCCEDED'
