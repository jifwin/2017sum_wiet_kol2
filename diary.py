import numpy
from flatten_dict import flatten


class Diary:
    def __init__(self, students, classes, dates):
        self.scores = {}
        self.attendances = {}
        self.classes = classes
        self.students = students
        self.dates = dates

        for student in students:
            self.scores[student] = {}
            self.attendances[student] = {}
            for clazz in classes:
                self.scores[student][clazz] = []
                self.attendances[student][clazz] = {}
                for date in dates:
                    self.attendances[student][clazz][date] = False

    def add_score(self, clazz, student, value):
        self._validate_class(clazz)
        self._validate_student(student)
        self.scores[student][clazz] = value

    def add_attendance(self, clazz, student, date):
        self._validate_student(student)
        self._validate_date(date)
        self.attendances[student][clazz][date] = True

    def get_average_score_value(self):
        return numpy.mean(self._get_flattened_scores().values())

    def get_average_score_value_in_class(self, clazz):
        class_scores = [score_value for (student, current_class), score_value
                        in self._get_flattened_scores().iteritems()
                        if current_class == clazz]
        return numpy.mean(class_scores)

    def get_student_attendance_count(self, student):
        self._validate_student(student)
        return numpy.sum(flatten(self.attendances[student]).values())

    def _get_flattened_scores(self):
        return flatten(self.scores)

    def _validate_class(self, clazz):
        self._validate_entity(clazz, self.classes)

    def _validate_student(self, student):
        self._validate_entity(student, self.students)

    def _validate_date(self, date):
        self._validate_entity(date, self.dates)

    def _validate_entity(self, entity, allowed_values):
        if entity not in allowed_values:
            raise Exception("{} does not exist in this diary".format(entity))
