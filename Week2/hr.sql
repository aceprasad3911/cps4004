/*Enter file path to make file amendments (open PycharmProjects
  folder in finder, locate file, open more info and copy, paste "where" section*/
/*Open file in terminal and execute commands after typying following:*/
/* sqlite3 (dictates what type of language + program is used*/
/*.open in hr.db (hr.db is associated database in week 2 pycharm folder)*/
/* copy and past relevant commands into terminal*/
/* to delete table, enter "DROP TABLE -TABLE NAME-;"*/
CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT UNIQUE,
    phone_number TEXT,
    hire_date DATE,
    job_title TEXT,
    salary REAL
);

CREATE TABLE department (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT UNIQUE,
    manager_id INTEGER,
    location_id INTEGER
);

CREATE TABLE task (
    task_id INTEGER PRIMARY KEY,
    task_name TEXT,
    description TEXT
);

CREATE TABLE employee_task (
    employee_id INTEGER,
    task_id INTEGER
);

CREATE TABLE job_title (
    job_title_id INTEGER PRIMARY KEY,
    title_name TEXT,
    description TEXT,
    base_salary REAL
);

CREATE TABLE location (
    city TEXT,
    state TEXT,
    country TEXT
);