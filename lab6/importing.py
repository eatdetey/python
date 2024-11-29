import json
import sqlite3
from xml.dom.minidom import Document

def import_to_json():
    conn = sqlite3.connect('med_db.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT PATIENT.name, PATIENT.surname, DOCTOR.name, DOCTOR.surname, APPOINTMENT.date
    FROM APPOINTMENT
    JOIN PATIENT ON PATIENT.id = APPOINTMENT.patient_id
    JOIN DOCTOR ON DOCTOR.id = APPOINTMENT.doctor_id
    """)
    appointments = cursor.fetchall()

    with open('appointments.json', 'w', encoding='utf-8') as f:
        json.dump(appointments, f, ensure_ascii=False)

    conn.close()

def import_to_xml():
    conn = sqlite3.connect('med_db.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT PATIENT.name, PATIENT.surname, DOCTOR.name, DOCTOR.surname, APPOINTMENT.date
    FROM APPOINTMENT
    JOIN PATIENT ON PATIENT.id = APPOINTMENT.patient_id
    JOIN DOCTOR ON DOCTOR.id = APPOINTMENT.doctor_id
    """)
    appointments = cursor.fetchall()

    doc = Document()
    root = doc.createElement("appointments")
    doc.appendChild(root)

    for appointment in appointments:
        appointment_element = doc.createElement("appointment")
        root.appendChild(appointment_element)

        patient_element = doc.createElement("patient")
        appointment_element.appendChild(patient_element)

        name_element = doc.createElement("name")
        name_text = doc.createTextNode(appointment[0])
        name_element.appendChild(name_text)
        patient_element.appendChild(name_element)

        surname_element = doc.createElement("surname")
        surname_text = doc.createTextNode(appointment[1])
        surname_element.appendChild(surname_text)
        patient_element.appendChild(surname_element)

        # Элемент для доктора
        doctor_element = doc.createElement("doctor")
        appointment_element.appendChild(doctor_element)

        doctor_name_element = doc.createElement("name")
        doctor_name_text = doc.createTextNode(appointment[2])
        doctor_name_element.appendChild(doctor_name_text)
        doctor_element.appendChild(doctor_name_element)

        doctor_surname_element = doc.createElement("surname")
        doctor_surname_text = doc.createTextNode(appointment[3])
        doctor_surname_element.appendChild(doctor_surname_text)
        doctor_element.appendChild(doctor_surname_element)

        date_element = doc.createElement("date")
        date_text = doc.createTextNode(appointment[4])
        date_element.appendChild(date_text)
        appointment_element.appendChild(date_element)

    with open("appointments.xml", "w", encoding="utf-8") as f:
        f.write(doc.toprettyxml(indent="  "))

    conn.close()
