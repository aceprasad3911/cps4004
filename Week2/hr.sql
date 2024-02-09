/*Enter file path to make file amendments (open PycharmProjects
  folder in finder, locate file, open more info and copy, paste "where" section*/
/*Open file in terminal and execute commands after typying following:*/
/* sqlite3 (dictates what type of language + program is used*/
/*.open in hr.db (hr.db is associated database in week 2 pycharm folder)*/
/* copy and past relevant commands into terminal*/
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