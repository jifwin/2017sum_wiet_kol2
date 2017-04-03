import random

from diary import Diary
from student import Student
from score import Score

SCORES = [5.0, 4.5, 4.0, 3.5, 3.0, 2.0]
NUMBER_OF_SCORES = 150

diary = Diary()

students = [
    Student("first student name", "first student surname"),
    Student("second student name", "second student surname"),
    Student("third student name", "third student surname"),
]

for i in xrange(NUMBER_OF_SCORES):
    score = Score(random.choice(students), random.choice(SCORES))
    diary.add_score(score)



    # todo: add main function check
