[![Build Status](https://travis-ci.org/Zim95/meet_the_family.svg?branch=develop)](https://travis-ci.org/Zim95/meet_the_family)


# meet_the_family
GEEKTRUST MEET THE FAMILY

# INSTRUCTIONS TO RUN:
- pip install -r requirements.txt
- python -m geektrust <absolute_path_to_filename>

# INSTRUCTIONS TO TEST:
Unit Test
- python -m unittest discover -s "./tests/unit/" -p "test_*.py" && flake8

Integration Test
- python -m unittest discover -s "./tests/integration/" -p "test_*.py" && flake8

System Test
- python -m unittest discover -s "./tests/system/" -p "test_*.py" && flake8

Origin: https://github.com/Zim95/meet_the_family.git