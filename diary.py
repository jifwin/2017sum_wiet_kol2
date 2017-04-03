import numpy


class Diary:
    def __init__(self, students):
        self.scores = []
        self.attendances = []
        self.students = students

    def add_score(self, score):
        self._validate_student(score.student)
        self.scores.append(score)

    def add_attendance(self, attendance):
        self._validate_student(attendance.student)
        self.attendances.append(attendance)

    def get_average_score_value(self):
        return numpy.mean([score.value for score in self.scores])

    def get_average_score_value_in_class(self, clazz):
        return numpy.mean([score.value for score in self.scores if score.clazz == clazz])

    def get_students(self):
        return self.students

    def _validate_student(self, student):
        if not self._is_existing_student(student):
            raise Exception("{} does not exist in this diary".format(student))

    def _is_existing_student(self, student):
        return student in self.students
