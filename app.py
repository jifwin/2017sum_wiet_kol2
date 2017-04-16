import random
from collections import namedtuple

from diary import Diary

Student = namedtuple("Student", ('first_name', 'surname'))

SCORES = [5.0, 4.5, 4.0, 3.5, 3.0, 2.0]
CLASSES = ["python", "algebra", "circuit theory", "physics", "radio"]
NUMBER_OF_SCORES = 150
NUMBER_OF_ATTENDANCES = 15
DATES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
STUDENTS = [
    Student("Adam", "Nowak"),
    Student("Janusz", "Golonka"),
    Student("Henryk", "Janowski"),
]

diary = Diary(STUDENTS, CLASSES, DATES)

def initialize_diary():
    for i in xrange(NUMBER_OF_SCORES):
        diary.add_score(random.choice(CLASSES), random.choice(STUDENTS), random.choice(SCORES))

    for clazz in CLASSES:
        for date in DATES:
            for student in STUDENTS:
                if random.choice([True, False]):
                    diary.add_attendance(clazz, student, date)


def get_data_from_diary():
    print "Overall average score == {}".format(diary.get_average_score_value())

    for clazz in CLASSES:
        print "Average score in {} == {}".format(clazz, diary.get_average_score_value_in_class(clazz))

    for student in STUDENTS:
        print "{} student attendance count: {}".format(student, diary.get_student_attendance_count(student))

def dump_diary():
    print diary.dump()


if __name__ == "__main__":
    initialize_diary()
    get_data_from_diary()
    dump_diary()
