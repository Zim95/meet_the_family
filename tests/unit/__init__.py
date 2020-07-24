from unittest.mock import Mock


def create_fake_member(id=None, name=None, gender=None,
                       mother=None, spouse=None, father=None,
                       children=None):
    member = Mock()
    member.id = id
    member.name = name
    member.gender = gender
    member.mother = mother
    member.spouse = spouse
    member.father = father
    member.children = children
    return member
