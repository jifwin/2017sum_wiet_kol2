import numpy


class Diary:
    def __init__(self):
        self.scores = []
        self.attendances = []

    def add_score(self, score):
        self.scores.append(score)

    def add_attendance(self, attendance):
        self.attendances.append(attendance)

    def get_average_score_value(self):
        return numpy.mean([score.value for score in self.scores])

    def get_average_score_value_in_class(self, clazz):
        return numpy.mean([score.value for score in self.scores if score.clazz == clazz])