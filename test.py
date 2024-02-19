# test.py
from main import StudentsInMLOps

def test_enroll_students():
    students_class = StudentsInMLOps()
    students_class.enrollStudents(5)
    assert students_class.getTotalStrength() == 5

def test_drop_students():
    students_class = StudentsInMLOps()
    students_class.enrollStudents(10)
    students_class.dropStudents(3)
    assert students_class.getTotalStrength() == 7

def test_get_class_name():
    students_class = StudentsInMLOps()
    assert students_class.getClassName() == "MLOps"
