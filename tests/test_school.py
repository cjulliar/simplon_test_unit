import pytest
from source.school import Student, Course

@pytest.fixture
def student_factory():
    def create_student(student_id, name):
        return Student(student_id=student_id, name=name)
    return create_student

@pytest.fixture
def course_factory():
    def create_course(course_id, title):
        return Course(course_id=course_id, title=title)
    return create_course

def test_student_existing(student_factory, course_factory):
    student_01 = student_factory(1, "Pedro")
    course_english = course_factory(10, "English")

    course_english.add_student(student_01)
    assert student_01 in course_english.students



def test_add_student(student_factory, course_factory):
    student_01 = student_factory(1, "Pedro")
    student_02 = student_factory(2, "Rickitta")
    student_03 = student_factory(3, "Francesco")
    student_04 = student_factory(4, "Maria")
    course_english = course_factory(10, "English")
    course_math = course_factory(11, "Math")

    course_english.add_student(student_01)
    course_english.add_student(student_02)
    course_english.add_student(student_04)
    course_math.add_student(student_02)
    course_math.add_student(student_03)
    assert course_english.student_count() == 3
    assert course_math.student_count() == 2

