DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;
DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohorts_id_seq;


CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date int
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO cohorts (name, starting_date) VALUES ('October', 2023);
INSERT INTO cohorts (name, starting_date) VALUES ('November', 2023);
INSERT INTO cohorts (name, starting_date) VALUES ('March', 2022);
INSERT INTO cohorts (name, starting_date) VALUES ('April', 2022);


INSERT INTO students (name, cohort_id) VALUES ('Dipanwita', 1);
INSERT INTO students (name, cohort_id) VALUES ('Shaun', 1);
INSERT INTO students (name, cohort_id) VALUES ('Amy', 2);
INSERT INTO students (name, cohort_id) VALUES ('Robert', 2);