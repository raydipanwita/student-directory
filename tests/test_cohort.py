from lib.cohort import *

def test_constructs():
    cohort = Cohort(1, "October", 2023)
    assert cohort.id == 1
    assert cohort.name == "October"
    assert cohort.starting_date == 2023
