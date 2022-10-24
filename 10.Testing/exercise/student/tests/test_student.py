import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    STUDENT_NAME = "Tanya"

    def setUp(self) -> None:
        self.student = Student(self.STUDENT_NAME)

    def test_student_init_without_courses(self):
        self.assertEqual(self.STUDENT_NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_student_init_with_courses(self):
        courses = {"Python Advanced": ['note1', 'note2']}

        student = Student(self.STUDENT_NAME, courses)

        self.assertEqual(self.STUDENT_NAME, student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll_if_course_exists__expect_adding_all_notes_to_course(self):
        course_name = "Python Advanced"
        courses = {course_name: ['note1', 'note2']}

        student = Student(self.STUDENT_NAME, courses)

        result = student.enroll(course_name, ['note3', 'note4'])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['note1', 'note2', 'note3', 'note4'], student.courses[course_name])

    def test_enroll_if_course_doesnt_exists_and_add_notes_empty__expect_create_course_with_given_notes(self):
        student = Student(self.STUDENT_NAME, {'Python OOP': []})
        course_name = "Python Advanced"
        notes = ['note1', 'note2', 'note3', 'note4']

        result = student.enroll(course_name, notes)

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'Python OOP': [], course_name: notes}, student.courses)

    def test_enroll_if_course_doesnt_exists_and_add_notes_Y__expect_create_course_with_given_notes(self):
        student = Student(self.STUDENT_NAME, {'Python OOP': []})
        course_name = "Python Advanced"
        notes = ['note1', 'note2', 'note3', 'note4']

        result = student.enroll(course_name, notes, 'Y')

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'Python OOP': [], course_name: notes}, student.courses)

    def test_enroll_if_course_doesnt_exists_and_add_notes_different_of_Y_or_empty__expect_create_course_with_empty_notes(self):
        student = Student(self.STUDENT_NAME, {'Python OOP': []})
        course_name = "Python Advanced"
        notes = ['note1', 'note2', 'note3', 'note4']

        result = student.enroll(course_name, notes, 'M')

        self.assertEqual("Course has been added.", result)
        self.assertEqual({'Python OOP': [], course_name: []}, student.courses)

    def test_add_notes_if_course_not_in_courses__raise(self):
        student = Student(self.STUDENT_NAME, {'Python OOP': []})

        with self.assertRaises(Exception) as error:
            student.add_notes("Python Advanced", "note1")
        self.assertEqual("Cannot add notes. Course not found.", str(error.exception))

    def test_add_notes_if_course_in_courses__expect_added_note(self):
        course_name = 'Python OOP'
        student = Student(self.STUDENT_NAME, {course_name: []})

        result = student.add_notes(course_name, "note1")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["note1"], student.courses[course_name])

    def test_leave_course_if_course_not_in_courses__expect_raise(self):
        course_name = 'Python OOP'
        student = Student(self.STUDENT_NAME, {"Python Advanced": []})

        with self.assertRaises(Exception) as error:
            student.leave_course(course_name)
        self.assertEqual("Cannot remove course. Course not found.", str(error.exception))

    def test_leave_course_if_course_in_courses__expect_remove_course_from_courses(self):
        course_name = 'Python OOP'
        student = Student(self.STUDENT_NAME, {course_name: []})

        result = student.leave_course(course_name)

        self.assertEqual("Course has been removed", result)
        self.assertTrue(course_name not in student.courses)


if __name__ == "__main__":
    unittest.main()




