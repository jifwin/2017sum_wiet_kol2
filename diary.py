class Diary:
    def __init__(self):
        self.scores = []
        self.attendances = []

    def add_score(self, score):
        self.scores.append(score)

    def add_attendance(self, attendance):
        self.attendances.append(attendance)