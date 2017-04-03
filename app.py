import random

from diary import Diary
from student import Student
from score import Score
from attendance import Attendance

SCORES = [5.0, 4.5, 4.0, 3.5, 3.0, 2.0]
CLASSES = ["python", "algebra", "circuit theory", "physics", "radio"]
NUMBER_OF_SCORES = 150
NUMBER_OF_ATTENDANCES = 15
DAYS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

diary = Diary()

students = [
    Student("first student name", "first student surname"),
    Student("second student name", "second student surname"),
    Student("third student name", "third student surname"),
]

if __name__ == "main":
    for i in xrange(NUMBER_OF_SCORES):
        score = Score(random.choice(students), random.choice(CLASSES), random.choice(SCORES))
        diary.add_score(score)

    for day in DAYS:
        for student in students:
            if random.choice([True, False]):
                diary.add_attendance(Attendance(student, day))

    print "Overall average score == {}".format(diary.get_average_score_value())
    for clazz in CLASSES:
        print "Average score in {} == {}".format(clazz, diary.get_average_score_value_in_class(clazz))
