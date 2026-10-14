"""
Patient Management System
Name: Jane Sarah Bangura
ID : 905005883
Domain: Health - Patient Record System
Project: Manages patients in a clinic/hospital
Student: Limkokwing University - PROG211 OOP1
"""

# ============================================================
# CLASS 1: PATIENT - Main class of Patient Management System
# ============================================================
class Patient:
    
    total_patients = 0 #counter 
    hospital_name = "Limkokwing Clinic"

    def __init__(self, ID, Name, Age, Gender, Contact):
        # ATTRIBUTES 
        self.ID = ID # Unique ID - used as dictionary key
        self.Name = Name
        self.Age = Age
        self.Gender = Gender
        self.Contact = Contact # basic contact, not sensitive address

        # Domain-specific data for patient management
        self.status = "Registered" # Registered, Waiting, Treated, Discharged
        self.visits = [] # list of visit notes

        # Increase total count
        Patient.total_patients += 1

    # ---------------- INSTANCE METHODS ----------------
    # Instance method = works on ONE patient only (needs self)

    def register(self):
        """Patient comes to hospital for first time"""
        self.status = "Registered"
        print(f"{self.Name} registered.")

    def update_record(self, note):
        """Update patient medical note - brief requires this name"""
        self.visits.append(note)
        self.status = "Treated"
        print(f"Record updated for {self.Name}: {note}")

    def rest(self):
        """Patient is waiting/resting"""
        self.status = "Waiting"

    def discharge(self):
        """Patient leaves hospital"""
        self.status = "Discharged"

    def display_info(self):
        """Display in neat columns - for ledger +10 marks"""
        print(f"| {self.ID:<6} | {self.Name:<12} | {self.Age:<5} | {self.Gender:<10} | {self.Contact:<12} | {self.status:<12} |")

    # ---------------- CLASS METHODS ----------------
    # Class method = works on whole class, not one patient
    # Needs @classmethod and cls

    @classmethod
    def get_total_patients(cls):
        """Returns total patients created - class level info"""
        return cls.total_patients

    @classmethod
    def get_hospital_name(cls):
        """Returns hospital name - belongs to all patients"""
        return cls.hospital_name

# ============================================================
# CLASS 2: VISIT / APPOINTMENT - Second class for patient management
# This is needed to meet "at least two classes" and to show interaction
# ============================================================
class Visit:
    def __init__(self, VisitID, Date, PatientID, DoctorName, Diagnosis):
        self.VisitID = VisitID
        self.Date = Date
        self.PatientID = PatientID # links to Patient ID
        self.DoctorName = DoctorName
        self.Diagnosis = Diagnosis
        self.status = "Scheduled"

    def update_record(self, new_status):
        """Update visit status"""
        self.status = new_status

    def display_info(self, patients_dict):
        """Display visit with patient name - shows interaction"""
        # Get patient name from patients_dict using PatientID
        if self.PatientID in patients_dict:
            p_name = patients_dict[self.PatientID].Name
        else:
            p_name = "Unknown"
        print(f"| {self.VisitID:<8} | {self.Date:<12} | {self.PatientID:<10} | {p_name:<12} | {self.DoctorName:<12} | {self.Diagnosis:<12} | {self.status:<10} |")

# ============================================================
# TASK 2: ONE DATA STRUCTURE - DICTIONARY
# Brief: {ID: object} - store objects with unique ID as key
# ============================================================

# Dictionary is best for patient management - search by ID is fast
patients_dict = {} # Key: Patient ID, Value: Patient object
visits_dict = {} # Key: Visit ID, Value: Visit object

# Function to ADD records - required by brief
def add_patient(ID, Name, Age, Gender, Contact):
    patient = Patient(ID, Name, Age, Gender, Contact)
    patients_dict[ID] = patient
    return patient

def add_visit(VisitID, Date, PatientID, DoctorName, Diagnosis):
    visit = Visit(VisitID, Date, PatientID, DoctorName, Diagnosis)
    visits_dict[VisitID] = visit
    return visit

# Function to DISPLAY records - required + neat columns
def display_all_patients():
    print("\n================== PATIENT MANAGEMENT LEDGER ==================")
    print(f"| {'ID':<6} | {'Name':<12} | {'Age':<5} | {'Gender':<10} | {'Contact':<12} | {'Status':<12} |")
    print("|--------|--------------|-------|------------|--------------|----------------|")
    for patient in patients_dict.values():
        patient.display_info()
    print("|--------|--------------|-------|------------|--------------|----------------|")

def display_all_visits():
    print("\n======================= VISIT LEDGER =======================")
    print(f"| {'VisitID':<8} | {'Date':<12} | {'PatID':<10} | {'Patient':<12} | {'Doctor':<12} | {'Diagnosis':<12} | {'Status':<10} |")
    print("|----------|--------------|------------|--------------|--------------|--------------|------------|")
    for visit in visits_dict.values():
        visit.display_info(patients_dict)
    print("|----------|--------------|------------|--------------|--------------|--------------|------------|")

# ============================================================
# OBJECT CREATION AND INTERACTION DEMO
# ============================================================

# Create patients - using function that adds to dictionary
print("=== Creating Patients ===")
p1 = add_patient(101, "sarah", 20, "female", "075-465837")
p2 = add_patient(102, "rah", 20, "male", "076-654321")
p3 = add_patient(103, "saah", 21, "female", "077-111222")
p4 = add_patient(104, "Trevor", 29, "male", "078-333444")
p5 = add_patient(105, "lah", 20, "male", "076-555666")

# Create visits - each visit links to a patient
v1 = add_visit(301, "2026-10-04", 101, "Dr. Smith", "Fever")
v2 = add_visit(302, "2026-10-05", 102, "Dr. Aisha", "Cough")
v3 = add_visit(303, "2026-10-06", 103, "Dr. Smith", "Checkup")

print("\n=== Interaction Between Patient and Visit ===")
# Instance methods - affect one patient
p1.update_record("Fever, prescribed paracetamol")
p2.rest()
v1.update_record("Completed")
v2.update_record("Confirmed")

# Display ledgers
display_all_patients()
display_all_visits()

# Class methods - affects whole class
print("\nS=== Class Method Demo ===")
print(f"Hospital: {Patient.get_hospital_name()}")
print(f"Total Patients in System: {Patient.get_total_patients()}")