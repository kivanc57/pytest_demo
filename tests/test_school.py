import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents

# Custom fixture for initializing Hogwarts-themed classroom with students and teacher
@pytest.fixture
def hogwarts_classroom():
    teacher = Teacher("Minerva McGonagall")
    students = [
        Student("Harry Potter"),
        Student("Hermione Granger"),
        Student("Ron Weasley"),
        Student("Draco Malfoy"),
        Student("Luna Lovegood"),
    ]
    course_title = "Defense Against the Dark Arts"
    return Classroom(teacher, students, course_title)

# Fixture to create individual Hogwarts students
@pytest.fixture
def harry():
    return Student("Harry Potter")

@pytest.fixture
def dumbledore():
    return Teacher("Albus Dumbledore")

# Test that classroom initialization works as expected
def test_classroom_initialization(hogwarts_classroom):
    assert hogwarts_classroom.teacher.name == "Minerva McGonagall"
    assert len(hogwarts_classroom.students) == 5
    assert hogwarts_classroom.course_title == "Defense Against the Dark Arts"

# Test adding students up to limit
def test_add_student_within_limit(hogwarts_classroom):
    new_student = Student("Neville Longbottom")
    hogwarts_classroom.add_student(new_student)
    assert new_student in hogwarts_classroom.students
    assert len(hogwarts_classroom.students) == 6

# Test exceeding the student limit and triggering TooManyStudents exception
def test_add_student_exceeds_limit(hogwarts_classroom):
    additional_students = [
        Student("Seamus Finnigan"),
        Student("Dean Thomas"),
        Student("Cho Chang"),
        Student("Ginny Weasley"),
        Student("Cedric Diggory"),
        Student("Fleur Delacour"),
    ]
    for student in additional_students[:5]:
        hogwarts_classroom.add_student(student)

    with pytest.raises(TooManyStudents):
        hogwarts_classroom.add_student(additional_students[5])

# Test removing a student by name
def test_remove_student(hogwarts_classroom):
    hogwarts_classroom.remove_student("Draco Malfoy")
    assert all(student.name != "Draco Malfoy" for student in hogwarts_classroom.students)
    assert len(hogwarts_classroom.students) == 4

# Test changing the teacher of the classroom
def test_change_teacher(hogwarts_classroom, dumbledore):
    hogwarts_classroom.change_teacher(dumbledore)
    assert hogwarts_classroom.teacher == dumbledore

# Parameterized test for ensuring a variety of Hogwarts students can be added without exceeding limits
@pytest.mark.parametrize("student_name", [
    "Neville Longbottom",
    "Cedric Diggory",
    "Cho Chang",
    "Lavender Brown",
])
def test_parameterized_add_student(hogwarts_classroom, student_name):
    student = Student(student_name)
    if len(hogwarts_classroom.students) < 10:
        hogwarts_classroom.add_student(student)
        assert student in hogwarts_classroom.students
    else:
        with pytest.raises(TooManyStudents):
            hogwarts_classroom.add_student(student)
