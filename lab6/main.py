import sqlite3

conn = sqlite3.connect('med_db.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS PATIENT (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    age INTEGER,
    sex TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS DOCTOR (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    age INTEGER,
    sex TEXT,
    specialization TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS APPOINTMENT (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER,
    date TEXT,
    FOREIGN KEY (patient_id) REFERENCES PATIENT(id),
    FOREIGN KEY (doctor_id) REFERENCES DOCTOR(id)
)
''')

conn.commit()

cursor.execute("INSERT INTO PATIENT (name, surname, age, sex) VALUES ('Иван', 'Иванов', 30, 'М')")
cursor.execute("INSERT INTO PATIENT (name, surname, age, sex) VALUES ('Ольга', 'Петрова', 25, 'Ж')")
cursor.execute("INSERT INTO PATIENT (name, surname, age, sex) VALUES ('Алексей', 'Сидоров', 40, 'М')")

cursor.execute("INSERT INTO DOCTOR (name, surname, age, sex, specialization) VALUES ('Смирнов', 'Иван', 45, 'М', 'Терапевт')")
cursor.execute("INSERT INTO DOCTOR (name, surname, age, sex, specialization) VALUES ('Кузнецова', 'Мария', 38, 'Ж', 'Хирург')")
cursor.execute("INSERT INTO DOCTOR (name, surname, age, sex, specialization) VALUES ('Ильина', 'Наталья', 42, 'Ж', 'Педиатр')")

cursor.execute("INSERT INTO APPOINTMENT (patient_id, doctor_id, date) VALUES (1, 1, '2024-11-29')")
cursor.execute("INSERT INTO APPOINTMENT (patient_id, doctor_id, date) VALUES (2, 2, '2024-11-28')")
cursor.execute("INSERT INTO APPOINTMENT (patient_id, doctor_id, date) VALUES (3, 3, '2024-11-27')")

conn.commit()

cursor.execute("SELECT COUNT(*) FROM APPOINTMENT WHERE date = '2024-11-29'")
print("Пациентов на 29 ноября:", cursor.fetchone()[0])

cursor.execute("""
SELECT DOCTOR.name, DOCTOR.surname, COUNT(APPOINTMENT.id)
FROM DOCTOR
LEFT JOIN APPOINTMENT ON DOCTOR.id = APPOINTMENT.doctor_id
GROUP BY DOCTOR.id
""")
for row in cursor.fetchall():
    print(f"Доктор {row[0]} {row[1]} принял {row[2]} пациентов")

cursor.execute("""
SELECT PATIENT.name, PATIENT.surname, DOCTOR.name, DOCTOR.surname, APPOINTMENT.date
FROM APPOINTMENT
JOIN PATIENT ON PATIENT.id = APPOINTMENT.patient_id
JOIN DOCTOR ON DOCTOR.id = APPOINTMENT.doctor_id
""")
for row in cursor.fetchall():
    print(f"Пациент {row[0]} {row[1]} был на приеме у {row[2]} {row[3]} в {row[4]}")

