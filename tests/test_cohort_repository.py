from lib.cohort_repository import *
from lib.cohort import *     
from lib.student import *

    # Retrieve all artists
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/student_directory_2.sql") # Seed our database with some test data
    repository = CohortRepository(db_connection) # Create a new ArtistRepository

    cohorts = repository.all() # Get all artists

    # Assert on the results
    assert cohorts == [
        Cohort(1, 'October', 2023),
        Cohort(2, 'November', 2023),
        Cohort(3, 'March', 2022),
        Cohort(4, 'April', 2022),
    ]

# def test_find():
#     # def test_find(db_connection):
#     #     db_connection.seed("seeds/student_directory_2.sql")
#     #     repository = CohortRepository(db_connection)

#     #     result = repository.find(1)
#     #     assert result == Cohort(1, 'October', 2023)


def test_find_with_students(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = CohortRepository(db_connection)
    cohort = repository.find_with_students(1)

    assert cohort == Cohort(1, "October", 2023, [
        Student(1, "Dipanwita", 1),
        Student(2, "Shaun", 1),
    ])
