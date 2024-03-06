from lib.cohort import *
from lib.student import *

class CohortRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM cohorts')
        cohort = []
        for row in rows:
            item = Cohort(row["id"], row["name"], row["starting_date"])
            cohort.append(item)
        return cohort

# Find a single artist by their id 
    # def find(self, cohort_id):
    #     rows = self._connection.execute(
    #         'SELECT * from cohorts WHERE id = %s', [cohort_id])
    #     row = rows[0]
    #     return Cohort(row["id"], row["name"], row["starting_date"])

    def find_with_students(self, cohort_id):
            rows = self._connection.execute(
                "SELECT cohorts.id as cohort_id, cohorts.name, students.id AS students_id, students.name, students.cohort_id" \
                "FROM cohorts JOIN students ON cohorts.id = students.cohort_id " \
                "WHERE cohorts.id = %s", [cohort_id])
            students = []
            for row in rows:
                student = Student(row["student_id"], row["name"], row["cohort_id"])
                students.append(student)

        # Each row has the same id, name, and genre, so we just use the first
            return Cohort(rows[0]["cohort_id"], rows[0]["name"], rows[0]["starting_date"], students)
    