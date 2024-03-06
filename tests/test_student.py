from lib.student import *

def test_constructs():
    student = Student(1, "Dipanwita", 1)
    assert student.id == 1
    assert student.name == "Dipanwita"
    assert student.cohort_id == 1