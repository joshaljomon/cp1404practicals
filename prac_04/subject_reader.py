"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subjects(FILENAME)
    print_subject_details(subjects)


def load_subjects(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            code, lecturer, number_of_students = line.split(',')
            subjects.append([code, lecturer, int(number_of_students)])
    return subjects

def print_subject_details(subjects):
    for code, lecturer, student_count in subjects:
        print(f"{code} is taught by {lecturer} and has {student_count} students")


main()