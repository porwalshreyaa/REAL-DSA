from dataclasses import dataclass
from typing import Any
import time, random

@dataclass
class Student:
    roll: str
    name: str
    email: str
    batch: int
    department: str
    grade: str

STUDENTS = {
    # Batch 2021
    "21f2004662": Student("21f2004662", "Aarav Shah",        "aarav.shah@study.iitm.ac.in",        2021, "CS", "A"),
    "21f2493662": Student("21f2493662", "Priya Nair",        "priya.nair@study.iitm.ac.in",        2021, "DS", "B"),
    "21f2053862": Student("21f2053862", "Rohan Verma",       "rohan.verma@study.iitm.ac.in",       2021, "CS", "F"),
    "21f2424422": Student("21f2424422", "Sneha Iyer",        "sneha.iyer@study.iitm.ac.in",        2021, "ES", "I"),
    "21f2027362": Student("21f2027362", "Karan Mehta",       "karan.mehta@study.iitm.ac.in",       2021, "DS", "S"),
    "21f2057662": Student("21f2057662", "Tanvi Desai",       "tanvi.desai@study.iitm.ac.in",       2021, "CS", "B"),
    "21f2904662": Student("21f2904662", "Rahul Pandey",      "rahul.pandey@study.iitm.ac.in",      2021, "ES", "U"),
    "21f3084662": Student("21f3084662", "Ankit Joshi",       "ankit.joshi@study.iitm.ac.in",       2021, "DS", "D"),
    "21f5604662": Student("21f5604662", "Pooja Kulkarni",    "pooja.kulkarni@study.iitm.ac.in",    2021, "CS", "E"),
    "21f1000662": Student("21f1000662", "Siddharth Rao",     "siddharth.rao@study.iitm.ac.in",     2021, "MA", "C"),
    "21f7000662": Student("21f7000662", "Ishaan Gupta",      "ishaan.gupta@study.iitm.ac.in",      2021, "CS", "A"),
    "21f2005662": Student("21f2005662", "Neha Pillai",       "neha.pillai@study.iitm.ac.in",       2021, "DS", "B"),
    "21f1907662": Student("21f1907662", "Yash Malhotra",     "yash.malhotra@study.iitm.ac.in",     2021, "MA", "C"),
    "21f2043552": Student("21f2043552", "Riya Sharma",       "riya.sharma@study.iitm.ac.in",       2021, "ES", "D"),
    "21f4356662": Student("21f4356662", "Aditya Kumar",      "aditya.kumar@study.iitm.ac.in",      2021, "CS", "S"),
    # Batch 2022
    "22f1004662": Student("22f1004662", "Divya Pillai",      "divya.pillai@study.iitm.ac.in",      2022, "CS", "A"),
    "22f2193662": Student("22f2193662", "Arjun Reddy",       "arjun.reddy@study.iitm.ac.in",       2022, "CS", "B"),
    "22f2350862": Student("22f2350862", "Meera Joshi",       "meera.joshi@study.iitm.ac.in",       2022, "DS", "A"),
    "22f2421422": Student("22f2421422", "Kabir Singh",       "kabir.singh@study.iitm.ac.in",       2022, "MA", "C"),
    "22f2097362": Student("22f2097362", "Lavanya Menon",     "lavanya.menon@study.iitm.ac.in",     2022, "ES", "S"),
    "22f2017662": Student("22f2017662", "Nikhil Bhat",       "nikhil.bhat@study.iitm.ac.in",       2022, "DS", "B"),
    "22f2900062": Student("22f2900062", "Simran Kaur",       "simran.kaur@study.iitm.ac.in",       2022, "CS", "U"),
    "22f3004662": Student("22f3004662", "Dhruv Patel",       "dhruv.patel@study.iitm.ac.in",       2022, "MA", "D"),
    "22f5004662": Student("22f5004662", "Kritika Saxena",    "kritika.saxena@study.iitm.ac.in",    2022, "ES", "E"),
    "22f1100662": Student("22f1100662", "Vivaan Trivedi",    "vivaan.trivedi@study.iitm.ac.in",    2022, "CS", "A"),
    "22f7200662": Student("22f7200662", "Shruti Agarwal",    "shruti.agarwal@study.iitm.ac.in",    2022, "DS", "B"),
    "22f2305662": Student("22f2305662", "Pranav Nambiar",    "pranav.nambiar@study.iitm.ac.in",    2022, "MA", "C"),
    "22f1307662": Student("22f1307662", "Aditi Bhatt",       "aditi.bhatt@study.iitm.ac.in",       2022, "CS", "A"),
    "22f2343552": Student("22f2343552", "Ronak Chauhan",     "ronak.chauhan@study.iitm.ac.in",     2022, "ES", "D"),
    "22f4956662": Student("22f4956662", "Sanya Mishra",      "sanya.mishra@study.iitm.ac.in",      2022, "DS", "S"),
    # Batch 2023
    "23f1004662": Student("23f1004662", "Vikram Rao",        "vikram.rao@study.iitm.ac.in",        2023, "ES", "B"),
    "23f2193662": Student("23f2193662", "Ananya Sharma",     "ananya.sharma@study.iitm.ac.in",     2023, "CS", "A"),
    "23f2350862": Student("23f2350862", "Harsh Tiwari",      "harsh.tiwari@study.iitm.ac.in",      2023, "DS", "C"),
    "23f2421422": Student("23f2421422", "Nandini Ghosh",     "nandini.ghosh@study.iitm.ac.in",     2023, "CS", "A"),
    "23f2097362": Student("23f2097362", "Samarth Dubey",     "samarth.dubey@study.iitm.ac.in",     2023, "MA", "F"),
    "23f2017662": Student("23f2017662", "Ishita Kapoor",     "ishita.kapoor@study.iitm.ac.in",     2023, "ES", "S"),
    "23f2900062": Student("23f2900062", "Aakash Srivastava", "aakash.srivastava@study.iitm.ac.in", 2023, "DS", "B"),
    "23f3004662": Student("23f3004662", "Kriti Pandey",      "kriti.pandey@study.iitm.ac.in",      2023, "CS", "A"),
    "23f5004662": Student("23f5004662", "Parth Oberoi",      "parth.oberoi@study.iitm.ac.in",      2023, "MA", "D"),
    "23f1100662": Student("23f1100662", "Tanisha Malviya",   "tanisha.malviya@study.iitm.ac.in",   2023, "ES", "C"),
    "23f7200662": Student("23f7200662", "Dev Rathore",       "dev.rathore@study.iitm.ac.in",       2023, "CS", "A"),
    "23f2305662": Student("23f2305662", "Bhavna Choudhary",  "bhavna.choudhary@study.iitm.ac.in",  2023, "DS", "B"),
    "23f1307662": Student("23f1307662", "Gaurav Naik",       "gaurav.naik@study.iitm.ac.in",       2023, "MA", "E"),
    "23f2343552": Student("23f2343552", "Swati Kulkarni",    "swati.kulkarni@study.iitm.ac.in",    2023, "CS", "A"),
    "23f4956662": Student("23f4956662", "Rajat Hegde",       "rajat.hegde@study.iitm.ac.in",       2023, "ES", "U"),
}

@dataclass
class Course:
    course_id: str
    name: str
    credits: int
    department: str
    instructor: str

COURSES = {
    "CS101": Course("CS101", "Intro to Programming",        4, "CS", "Dr. Balakrishnan"),
    "CS201": Course("CS201", "Data Structures",             4, "CS", "Dr. Mittal"),
    "CS301": Course("CS301", "Algorithms",                  4, "CS", "Dr. Sundar"),
    "DS101": Course("DS101", "Statistics for DS",           3, "DS", "Dr. Ramesh"),
    "DS201": Course("DS201", "Machine Learning",            4, "DS", "Dr. Priya"),
    "ES101": Course("ES101", "English Communication",       2, "ES", "Dr. Kavitha"),
    "MA101": Course("MA101", "Linear Algebra",              4, "CS", "Dr. Krishnamurthy"),
    "MA201": Course("MA201", "Probability & Statistics",    4, "DS", "Dr. Iyer"),
}

@dataclass
class Assignment:
    assignment_id: str
    course_id: str
    title: str
    due_date: str
    max_marks: int

ASSIGNMENTS = {
    "AS001": Assignment("AS001", "CS101", "Hello World in Python",  "2024-02-10", 100),
    "AS002": Assignment("AS002", "CS101", "OOP Basics",             "2024-03-01", 100),
    "AS003": Assignment("AS003", "CS201", "Linked List impl",       "2024-03-15", 100),
    "AS004": Assignment("AS004", "DS101", "EDA on dataset",         "2024-02-20", 100),
    "AS005": Assignment("AS005", "MA101", "Matrix operations",      "2024-02-28", 100),
}

@dataclass
class Enrollment:
    roll: str
    course_id: str
    semester: int
    status: str          # "active", "dropped", "completed"

@dataclass
class Submission:
    submission_id: str
    assignment_id: str
    roll: str
    submitted_at: str
    marks: int

ENROLLMENTS = {
    # Batch 2021 enrollments
    "ENR001": Enrollment("21f2004662", "CS101", 1, "completed"),
    "ENR002": Enrollment("21f2004662", "MA101", 1, "completed"),
    "ENR003": Enrollment("21f2004662", "CS201", 2, "completed"),
    "ENR004": Enrollment("21f2004662", "CS301", 3, "active"),

    "ENR005": Enrollment("21f2493662", "DS101", 1, "completed"),
    "ENR006": Enrollment("21f2493662", "MA201", 2, "completed"),
    "ENR007": Enrollment("21f2493662", "DS201", 3, "active"),

    "ENR008": Enrollment("21f2053862", "CS101", 1, "completed"),
    "ENR009": Enrollment("21f2053862", "MA101", 1, "completed"),
    "ENR010": Enrollment("21f2053862", "CS201", 2, "dropped"),

    "ENR011": Enrollment("21f2424422", "ES101", 1, "completed"),
    "ENR012": Enrollment("21f2424422", "MA101", 2, "completed"),
    "ENR013": Enrollment("21f2424422", "DS101", 3, "active"),

    "ENR014": Enrollment("21f2027362", "DS101", 1, "completed"),
    "ENR015": Enrollment("21f2027362", "DS201", 2, "completed"),
    "ENR016": Enrollment("21f2027362", "MA201", 3, "active"),

    "ENR017": Enrollment("21f2057662", "CS101", 1, "completed"),
    "ENR018": Enrollment("21f2057662", "CS201", 2, "completed"),
    "ENR019": Enrollment("21f2057662", "CS301", 3, "active"),

    "ENR020": Enrollment("21f2904662", "ES101", 1, "completed"),
    "ENR021": Enrollment("21f2904662", "MA101", 2, "dropped"),

    "ENR022": Enrollment("21f3084662", "DS101", 1, "completed"),
    "ENR023": Enrollment("21f3084662", "MA201", 2, "completed"),
    "ENR024": Enrollment("21f3084662", "DS201", 3, "active"),

    "ENR025": Enrollment("21f5604662", "CS101", 1, "completed"),
    "ENR026": Enrollment("21f5604662", "MA101", 2, "dropped"),

    "ENR027": Enrollment("21f1000662", "MA101", 1, "completed"),
    "ENR028": Enrollment("21f1000662", "MA201", 2, "completed"),
    "ENR029": Enrollment("21f1000662", "CS201", 3, "active"),

    "ENR030": Enrollment("21f7000662", "CS101", 1, "completed"),
    "ENR031": Enrollment("21f7000662", "CS201", 2, "completed"),
    "ENR032": Enrollment("21f7000662", "CS301", 3, "active"),

    "ENR033": Enrollment("21f2005662", "DS101", 1, "completed"),
    "ENR034": Enrollment("21f2005662", "DS201", 2, "active"),

    "ENR035": Enrollment("21f1907662", "MA101", 1, "completed"),
    "ENR036": Enrollment("21f1907662", "MA201", 2, "completed"),
    "ENR037": Enrollment("21f1907662", "CS201", 3, "active"),

    "ENR038": Enrollment("21f2043552", "ES101", 1, "completed"),
    "ENR039": Enrollment("21f2043552", "DS101", 2, "active"),

    "ENR040": Enrollment("21f4356662", "CS101", 1, "completed"),
    "ENR041": Enrollment("21f4356662", "CS201", 2, "completed"),
    "ENR042": Enrollment("21f4356662", "CS301", 3, "active"),

    # Batch 2022 enrollments
    "ENR043": Enrollment("22f1004662", "CS101", 1, "completed"),
    "ENR044": Enrollment("22f1004662", "MA101", 1, "completed"),
    "ENR045": Enrollment("22f1004662", "CS201", 2, "active"),

    "ENR046": Enrollment("22f2193662", "CS101", 1, "completed"),
    "ENR047": Enrollment("22f2193662", "CS201", 2, "active"),

    "ENR048": Enrollment("22f2350862", "DS101", 1, "completed"),
    "ENR049": Enrollment("22f2350862", "MA201", 2, "active"),

    "ENR050": Enrollment("22f2421422", "MA101", 1, "completed"),
    "ENR051": Enrollment("22f2421422", "MA201", 2, "active"),

    "ENR052": Enrollment("22f2097362", "ES101", 1, "completed"),
    "ENR053": Enrollment("22f2097362", "DS101", 2, "active"),

    "ENR054": Enrollment("22f2017662", "DS101", 1, "completed"),
    "ENR055": Enrollment("22f2017662", "DS201", 2, "active"),

    "ENR056": Enrollment("22f2900062", "CS101", 1, "completed"),
    "ENR057": Enrollment("22f2900062", "CS201", 2, "dropped"),

    "ENR058": Enrollment("22f3004662", "MA101", 1, "completed"),
    "ENR059": Enrollment("22f3004662", "MA201", 2, "active"),

    "ENR060": Enrollment("22f5004662", "ES101", 1, "completed"),
    "ENR061": Enrollment("22f5004662", "MA101", 2, "active"),

    "ENR062": Enrollment("22f1100662", "CS101", 1, "completed"),
    "ENR063": Enrollment("22f1100662", "CS201", 2, "active"),

    "ENR064": Enrollment("22f7200662", "DS101", 1, "completed"),
    "ENR065": Enrollment("22f7200662", "DS201", 2, "active"),

    "ENR066": Enrollment("22f2305662", "MA101", 1, "completed"),
    "ENR067": Enrollment("22f2305662", "CS201", 2, "active"),

    "ENR068": Enrollment("22f1307662", "CS101", 1, "completed"),
    "ENR069": Enrollment("22f1307662", "CS201", 2, "active"),

    "ENR070": Enrollment("22f2343552", "ES101", 1, "completed"),
    "ENR071": Enrollment("22f2343552", "DS101", 2, "active"),

    "ENR072": Enrollment("22f4956662", "DS101", 1, "completed"),
    "ENR073": Enrollment("22f4956662", "DS201", 2, "active"),

    # Batch 2023 enrollments (all semester 1, active)
    "ENR074": Enrollment("23f1004662", "ES101", 1, "active"),
    "ENR075": Enrollment("23f1004662", "MA101", 1, "active"),

    "ENR076": Enrollment("23f2193662", "CS101", 1, "active"),
    "ENR077": Enrollment("23f2193662", "MA101", 1, "active"),

    "ENR078": Enrollment("23f2350862", "DS101", 1, "active"),
    "ENR079": Enrollment("23f2350862", "MA201", 1, "active"),

    "ENR080": Enrollment("23f2421422", "CS101", 1, "active"),
    "ENR081": Enrollment("23f2421422", "MA101", 1, "active"),

    "ENR082": Enrollment("23f2097362", "MA101", 1, "active"),
    "ENR083": Enrollment("23f2097362", "MA201", 1, "active"),

    "ENR084": Enrollment("23f2017662", "ES101", 1, "active"),
    "ENR085": Enrollment("23f2017662", "DS101", 1, "active"),

    "ENR086": Enrollment("23f2900062", "DS101", 1, "active"),
    "ENR087": Enrollment("23f2900062", "MA201", 1, "active"),

    "ENR088": Enrollment("23f3004662", "CS101", 1, "active"),
    "ENR089": Enrollment("23f3004662", "CS201", 1, "active"),

    "ENR090": Enrollment("23f5004662", "MA101", 1, "active"),
    "ENR091": Enrollment("23f5004662", "MA201", 1, "active"),

    "ENR092": Enrollment("23f1100662", "ES101", 1, "active"),
    "ENR093": Enrollment("23f1100662", "MA101", 1, "active"),

    "ENR094": Enrollment("23f7200662", "CS101", 1, "active"),
    "ENR095": Enrollment("23f7200662", "MA101", 1, "active"),

    "ENR096": Enrollment("23f2305662", "DS101", 1, "active"),
    "ENR097": Enrollment("23f2305662", "DS201", 1, "active"),

    "ENR098": Enrollment("23f1307662", "MA101", 1, "active"),
    "ENR099": Enrollment("23f1307662", "MA201", 1, "active"),

    "ENR100": Enrollment("23f2343552", "CS101", 1, "active"),
    "ENR101": Enrollment("23f2343552", "CS201", 1, "active"),

    "ENR102": Enrollment("23f4956662", "ES101", 1, "active"),
    "ENR103": Enrollment("23f4956662", "DS101", 1, "active"),
}

SUBMISSIONS = {
    # AS001 — CS101: Hello World in Python
    "SUB001": Submission("SUB001", "AS001", "21f2004662", "2024-02-09 22:10", 91),
    "SUB002": Submission("SUB002", "AS001", "21f2493662", "2024-02-10 11:00", 78),
    "SUB003": Submission("SUB003", "AS001", "21f2053862", "2024-02-10 23:55", 41),
    "SUB004": Submission("SUB004", "AS001", "21f2057662", "2024-02-09 18:30", 85),
    "SUB005": Submission("SUB005", "AS001", "21f7000662", "2024-02-08 10:00", 94),
    "SUB006": Submission("SUB006", "AS001", "21f4356662", "2024-02-10 20:45", 73),
    "SUB007": Submission("SUB007", "AS001", "22f1004662", "2024-02-09 15:00", 88),
    "SUB008": Submission("SUB008", "AS001", "22f2193662", "2024-02-10 09:30", 76),
    "SUB009": Submission("SUB009", "AS001", "22f1100662", "2024-02-09 21:00", 91),
    "SUB010": Submission("SUB010", "AS001", "22f1307662", "2024-02-10 14:20", 83),
    "SUB011": Submission("SUB011", "AS001", "23f2193662", "2024-02-09 17:45", 95),
    "SUB012": Submission("SUB012", "AS001", "23f2421422", "2024-02-10 08:00", 90),
    "SUB013": Submission("SUB013", "AS001", "23f3004662", "2024-02-09 23:00", 87),
    "SUB014": Submission("SUB014", "AS001", "23f7200662", "2024-02-10 11:30", 92),
    "SUB015": Submission("SUB015", "AS001", "23f2343552", "2024-02-09 19:15", 89),

    # AS002 — CS101: OOP Basics
    "SUB016": Submission("SUB016", "AS002", "21f2004662", "2024-02-28 18:45", 85),
    "SUB017": Submission("SUB017", "AS002", "21f2057662", "2024-03-01 00:30", 79),
    "SUB018": Submission("SUB018", "AS002", "21f7000662", "2024-02-27 14:00", 92),
    "SUB019": Submission("SUB019", "AS002", "21f4356662", "2024-02-28 22:10", 68),
    "SUB020": Submission("SUB020", "AS002", "22f1004662", "2024-02-28 16:00", 81),
    "SUB021": Submission("SUB021", "AS002", "22f2193662", "2024-03-01 09:00", 74),
    "SUB022": Submission("SUB022", "AS002", "22f1100662", "2024-02-28 20:30", 88),
    "SUB023": Submission("SUB023", "AS002", "22f1307662", "2024-02-27 11:00", 90),
    "SUB024": Submission("SUB024", "AS002", "23f2193662", "2024-02-28 13:45", 96),
    "SUB025": Submission("SUB025", "AS002", "23f2421422", "2024-02-28 17:00", 91),
    "SUB026": Submission("SUB026", "AS002", "23f3004662", "2024-03-01 07:30", 84),
    "SUB027": Submission("SUB027", "AS002", "23f7200662", "2024-02-27 22:00", 93),
    "SUB028": Submission("SUB028", "AS002", "23f2343552", "2024-02-28 15:20", 87),

    # AS003 — CS201: Linked List Implementation
    "SUB029": Submission("SUB029", "AS003", "21f2004662", "2024-03-14 23:59", 95),
    "SUB030": Submission("SUB030", "AS003", "21f2057662", "2024-03-13 18:00", 82),
    "SUB031": Submission("SUB031", "AS003", "21f1000662", "2024-03-14 20:30", 78),
    "SUB032": Submission("SUB032", "AS003", "21f7000662", "2024-03-12 10:00", 97),
    "SUB033": Submission("SUB033", "AS003", "21f1907662", "2024-03-14 22:45", 71),
    "SUB034": Submission("SUB034", "AS003", "22f1004662", "2024-03-14 17:30", 86),
    "SUB035": Submission("SUB035", "AS003", "22f2193662", "2024-03-15 00:10", 79),
    "SUB036": Submission("SUB036", "AS003", "22f1100662", "2024-03-13 14:00", 91),
    "SUB037": Submission("SUB037", "AS003", "22f1307662", "2024-03-14 19:00", 88),
    "SUB038": Submission("SUB038", "AS003", "22f2305662", "2024-03-14 21:30", 83),
    "SUB039": Submission("SUB039", "AS003", "23f2193662", "2024-03-13 16:45", 98),
    "SUB040": Submission("SUB040", "AS003", "23f3004662", "2024-03-14 11:00", 92),
    "SUB041": Submission("SUB041", "AS003", "23f2343552", "2024-03-14 23:00", 89),

    # AS004 — DS101: EDA on Dataset
    "SUB042": Submission("SUB042", "AS004", "21f2493662", "2024-02-19 15:30", 88),
    "SUB043": Submission("SUB043", "AS004", "21f2027362", "2024-02-18 12:00", 91),
    "SUB044": Submission("SUB044", "AS004", "21f3084662", "2024-02-19 20:00", 74),
    "SUB045": Submission("SUB045", "AS004", "21f2005662", "2024-02-20 08:30", 82),
    "SUB046": Submission("SUB046", "AS004", "22f2350862", "2024-02-19 11:00", 93),
    "SUB047": Submission("SUB047", "AS004", "22f2017662", "2024-02-18 16:45", 87),
    "SUB048": Submission("SUB048", "AS004", "22f7200662", "2024-02-19 22:00", 79),
    "SUB049": Submission("SUB049", "AS004", "22f4956662", "2024-02-20 09:15", 85),
    "SUB050": Submission("SUB050", "AS004", "23f2350862", "2024-02-19 14:30", 90),
    "SUB051": Submission("SUB051", "AS004", "23f2017662", "2024-02-18 19:00", 76),
    "SUB052": Submission("SUB052", "AS004", "23f2900062", "2024-02-19 17:30", 83),
    "SUB053": Submission("SUB053", "AS004", "23f2305662", "2024-02-20 10:00", 88),
    "SUB054": Submission("SUB054", "AS004", "23f1100662", "2024-02-19 13:00", 71),

    # AS005 — MA101: Matrix Operations
    "SUB055": Submission("SUB055", "AS005", "21f2004662", "2024-02-27 20:00", 88),
    "SUB056": Submission("SUB056", "AS005", "21f1000662", "2024-02-26 15:30", 92),
    "SUB057": Submission("SUB057", "AS005", "21f7000662", "2024-02-27 11:00", 96),
    "SUB058": Submission("SUB058", "AS005", "21f1907662", "2024-02-28 00:45", 74),
    "SUB059": Submission("SUB059", "AS005", "22f1004662", "2024-02-27 18:00", 85),
    "SUB060": Submission("SUB060", "AS005", "22f2421422", "2024-02-26 10:30", 89),
    "SUB061": Submission("SUB061", "AS005", "22f3004662", "2024-02-27 22:15", 78),
    "SUB062": Submission("SUB062", "AS005", "22f2305662", "2024-02-27 14:00", 91),
    "SUB063": Submission("SUB063", "AS005", "22f1307662", "2024-02-26 17:45", 94),
    "SUB064": Submission("SUB064", "AS005", "23f2193662", "2024-02-27 09:30", 97),
    "SUB065": Submission("SUB065", "AS005", "23f2421422", "2024-02-27 16:00", 93),
    "SUB066": Submission("SUB066", "AS005", "23f2097362", "2024-02-28 01:00", 61),
    "SUB067": Submission("SUB067", "AS005", "23f5004662", "2024-02-27 12:30", 80),
    "SUB068": Submission("SUB068", "AS005", "23f1100662", "2024-02-26 20:00", 75),
    "SUB069": Submission("SUB069", "AS005", "23f1307662", "2024-02-27 23:30", 83),
    "SUB070": Submission("SUB070", "AS005", "23f2343552", "2024-02-27 10:15", 95),
}

TABLES = {
    "students":    STUDENTS,
    "courses":     COURSES,
    "enrollments": ENROLLMENTS,
    "assignments": ASSIGNMENTS,
    "submissions": SUBMISSIONS,
}

def db_read(table: str, key: str) -> Any | None:
    """
    Generic DB read with simulated latency.
    Cache key convention: "{table}:{key}"
    """
    if table not in TABLES:
        raise ValueError(f"Unknown table: {table}")
    print(f"  [DB HIT] {table}:{key}")
    time.sleep(random.uniform(0.02, 0.1))
    if not TABLES[table].get(key, None):
        raise ValueError(f"Entry for {key} does not exist in DB")
    return str(TABLES[table].get(key, None))