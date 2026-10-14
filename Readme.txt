# Patient Management System - OOP1 Assignment

**Course:** PROG211 Object-Oriented Programming 1
**University:** Limkokwing University, Sierra Leone
**Domain:** Health - Patient Management System (chosen from Health/Education/Government/Agriculture)
**Project Type:** Individual Assignment 10%
**Semester:** Sept 2026 - Feb 2027

## 1. Overview

This project is a Patient Management System built with Python Object-Oriented Programming. In many clinics in Sierra Leone, patient records are kept on paper which causes loss of records and difficulty in finding patient history. This system solves that by managing patients digitally.

The system is specifically a Patient Management System, not a full hospital system. It focuses on managing patients: registering them, updating their records, tracking their status (Registered, Waiting, Treated, Discharged), and linking them to their visits. This is simple, inclusive, and directly meets the brief requirement of "Patient Record System" under Health domain.

The program follows all tasks from Lecture 1 to Lecture 3 and follows Digital Public Goods (DPG) standards.

## 2. Classes and Design

### Class 1: Patient (Main Class)
Represents a patient in the clinic.

**Attributes:**
- ID: Unique number, used as dictionary key
- Name, Age, Gender: Basic info required by brief
- Contact: Basic phone number (not sensitive address to respect privacy)
- status: Tracks where patient is - Registered / Waiting / Treated / Discharged
- visits: List of medical notes for that patient

**Methods:**
- `register()` - instance method, registers one patient
- `update_record(note)` - instance method, adds medical note to one patient only. Required by brief naming.
- `rest()` and `discharge()` - instance methods to change status
- `display_info()` - instance method to show one patient in neat columns
- `get_total_patients()` - CLASS METHOD with @classmethod, returns total patients in whole system. Uses cls.total_patients.
- `get_hospital_name()` - CLASS METHOD, returns clinic name.

Why we need both: `update_record` works on self (one patient). No single patient knows total count, so we need class method for total.

### Class 2: Visit
Second class to satisfy "at least two classes" and to show object interaction in patient management.

**Attributes:**
- VisitID, Date, PatientID, DoctorName, Diagnosis, status

**Methods:**
- `update_record(new_status)` - changes visit from Scheduled to Completed
- `display_info(patients_dict)` - needs patients_dict to find patient name from PatientID. This shows interaction between Patient and Visit classes.

## 3. Data Structure - Dictionary (Task 2)

Brief says: "Integrate only one data structure (choose either a list or a dictionary)"

**Choice: Dictionary**

Reason: For patient management, you always search by Patient ID. Dictionary `{ID: object}` allows instant search `patients_dict[101]` without looping. List would require looping through all patients.

**Implementation from brief:**
```python
patients_dict = {101: <Patient object>, 102: <Patient object>}

***********this is the outcome******************
PS C:\Users\USER\OneDrive\Documents\oop assignment> & C:\Users\USER\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/USER/OneDrive/Documents/oop assignment/Patient_record_system.py"
=== Creating Patients ===

=== Interaction Between Patient and Visit ===
Record updated for sarah: Fever, prescribed paracetamol

================== PATIENT MANAGEMENT LEDGER ==================
| ID     | Name         | Age   | Gender     | Contact      | Status       |
|--------|--------------|-------|------------|--------------|----------------|
| 101    | sarah        | 20    | female     | 075-465837   | Treated      |
| 102    | rah          | 20    | male       | 076-654321   | Waiting      |
| 103    | saah         | 21    | female     | 077-111222   | Registered   |
| 104    | Trevor       | 29    | male       | 078-333444   | Registered   |
| 105    | lah          | 20    | male       | 076-555666   | Registered   |
|--------|--------------|-------|------------|--------------|----------------|

======================= VISIT LEDGER =======================
| VisitID  | Date         | PatID      | Patient      | Doctor       | Diagnosis    | Status     |
|----------|--------------|------------|--------------|--------------|--------------|------------|
| 301      | 2026-10-04   | 101        | sarah        | Dr. Smith    | Fever        | Completed  |
| 302      | 2026-10-05   | 102        | rah          | Dr. Aisha    | Cough        | Confirmed  |
| 303      | 2026-10-06   | 103        | saah         | Dr. Smith    | Checkup      | Scheduled  |
|----------|--------------|------------|--------------|--------------|--------------|------------|

=== Class Method Demo ===
Hospital: Limkokwing Clinic
Total Patients in System: 5
PS C:\Users\USER\OneDrive\Documents\oop assignment> 