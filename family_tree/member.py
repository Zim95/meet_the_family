import enum


class Gender(enum.Enum):
    male = "Male"
    female = "Female"


class Member:

    def __init__(self, id, name, gender):
        self.id = id
        self.name = name
        self.gender = Gender(gender)
        self.mother = None
        self.father = None
        self.spouse = None
        self.children = []

    def set_mother(self, mother):
        if not isinstance(mother, Member):
            raise ValueError('Invalid value for mother')
        if mother.gender != Gender.female:
            raise ValueError(
                'Invalid gender value for mother.'
                'Mother should be a Female'
            )
        self.mother = mother

    def set_father(self, father):
        if not isinstance(father, Member):
            raise ValueError('Invalid value for father')
        if father.gender != Gender.male:
            raise ValueError(
                'Invalid gender value for father.'
                'Father should be a Male'
            )
        self.father = father

    def set_spouse(self, spouse):
        if not isinstance(spouse, Member):
            raise ValueError('Invalid value for spouse')
        if self.gender == spouse.gender:
            raise ValueError(
                'Invalid gender value for spouse.'
                'Spouse and member cannot have the same gender.'
            )
        self.spouse = spouse

    def add_child(self, child):
        if not isinstance(child, Member):
            raise ValueError('Invalid value for child')
        self.children.append(child)

    def get_paternal_grandmother(self):
        if not self.father:
            return None
        if not self.father.mother:
            return None
        return self.father.mother

    def get_maternal_grandmother(self):
        if not self.mother:
            return None
        if not self.mother.mother:
            return None
        return self.mother.mother

    def get_spouse_mother(self):
        if not self.spouse:
            return None
        if not self.spouse.mother:
            return None
        return self.spouse.mother

    def get_paternal_aunt(self):
        grandmother = self.get_paternal_grandmother()
        if not grandmother:
            return []
        if not grandmother.children:
            return []
        return list(
            filter(
                lambda x: x.gender == Gender.female,
                grandmother.children
            )
        )

    def get_paternal_uncle(self):
        grandmother = self.get_paternal_grandmother()
        if not grandmother:
            return []
        if not grandmother.children:
            return []
        return list(
            filter(
                lambda x: x.gender == Gender.male and
                x.name != self.father.name,
                grandmother.children
            )
        )

    def get_maternal_aunt(self):
        grandmother = self.get_maternal_grandmother()
        if not grandmother:
            return []
        if not grandmother.children:
            return []
        return list(
            filter(
                lambda x: x.gender == Gender.female and
                x.name != self.mother.name,
                grandmother.children
            )
        )

    def get_maternal_uncle(self):
        grandmother = self.get_maternal_grandmother()
        if not grandmother:
            return []
        if not grandmother.children:
            return []
        return list(
            filter(
                lambda x: x.gender == Gender.male,
                grandmother.children
            )
        )

    def get_sibling_spouses(self):
        siblings = self.get_siblings()
        if not siblings:
            return []
        sibling_spouses = [
            sibling.spouse for sibling in siblings if sibling.spouse
        ]
        return sibling_spouses

    def get_spouse_siblings(self):
        if not self.spouse:
            return []
        return self.spouse.get_siblings()

    def get_brother_in_law(self):
        results = self.get_sibling_spouses() + self.get_spouse_siblings()
        if not results:
            return []
        return list(
            filter(
                lambda x: x.gender == Gender.male,
                results
            )
        )

    def get_sister_in_law(self):
        results = self.get_sibling_spouses() + self.get_spouse_siblings()
        if not results:
            return []
        return list(
            filter(
                lambda x: x.gender == Gender.female,
                results
            )
        )

    def get_son(self):
        if not self.children:
            return []
        return list(
            filter(
                lambda x: x.gender == Gender.male,
                self.children
            )
        )

    def get_daughter(self):
        if not self.children:
            return []
        return list(
            filter(
                lambda x: x.gender == Gender.female,
                self.children
            )
        )

    def get_siblings(self):
        if not self.mother:
            return []
        if not self.mother.children:
            return []
        return list(
            filter(
                lambda x: x.name != self.name,
                self.mother.children
            )
        )

    def get_relationship(self, relationship_type):
        relationship_method_switch = {
            'paternal_aunt': self.get_paternal_aunt,
            'paternal_uncle': self.get_paternal_uncle,
            'maternal_aunt': self.get_maternal_aunt,
            'maternal_uncle': self.get_maternal_uncle,
            'brother_in_law': self.get_brother_in_law,
            'sister_in_law': self.get_sister_in_law,
            'son': self.get_son,
            'daughter': self.get_daughter,
            'siblings': self.get_siblings
        }

        relationship_method = relationship_method_switch.get(
            relationship_type, None)

        if relationship_method:
            return relationship_method()
        else:
            return []
