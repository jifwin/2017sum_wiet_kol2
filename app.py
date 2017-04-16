import random
import argparse

import jsonpickle

from diary import Diary

SCORES = [5.0, 4.5, 4.0, 3.5, 3.0, 2.0]
CLASSES = ["python", "algebra", "circuit theory", "physics", "radio"]
NUMBER_OF_SCORES = 150
NUMBER_OF_ATTENDANCES = 15
DATES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
STUDENTS = ["Adam Nowak", "Janusz Golonka", "Henryk Janowski"]

def initialize_diary():
    diary = Diary(STUDENTS, CLASSES, DATES)
    for i in xrange(NUMBER_OF_SCORES):
        diary.add_score(random.choice(CLASSES), random.choice(STUDENTS), random.choice(SCORES))

    for clazz in CLASSES:
        for date in DATES:
            for student in STUDENTS:
                if random.choice([True, False]):
                    diary.add_attendance(clazz, student, date)
    return diary


def load_diary(dump_path):
    with open(dump_path, 'r') as file:
        dump = file.read()
        return jsonpickle.decode(dump)


def get_data_from_diary(diary):
    print "Overall average score == {}".format(diary.get_average_score_value())

    for clazz in CLASSES:
        print "Average score in {} == {}".format(clazz, diary.get_average_score_value_in_class(clazz))

    for student in STUDENTS:
        print "{} attendance count: {}".format(student, diary.get_student_attendance_count(student))


def dump_diary(diary, target_path):
    with open(target_path, 'w') as file:
        file.write(jsonpickle.encode(diary))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", dest="dump_path", required=True)
    parser.add_argument('-n', action="store", dest="new_diary")
    args = parser.parse_args()
    dump_path = args.dump_path

    if args.new_diary:
        newDiary = initialize_diary()
        dump_diary(newDiary, dump_path)
    else:
        loadedDiary = load_diary(dump_path)
        get_data_from_diary(loadedDiary)
