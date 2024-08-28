import logging
import pydicom
from datetime import datetime

import pydicom.tag

logging.basicConfig(filename='patientRecord.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class PatientRecord:
    def __init__(self, name, age, birth_date, sex, weight, patient_id, id_type):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.sex = sex
        self.weight = weight
        self.patient_id = patient_id
        self.id_type = id_type
        self.diagnosis = None

    # Setters
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def set_sex(self, sex):
        self.sex = sex

    def set_weight(self, weight):
        self.weight = weight

    def set_patient_id(self, patient_id):
        self.patient_id = patient_id

    def set_id_type(self, id_type):
        self.id_type = id_type

    # Getters
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_birth_date(self):
        return self.birth_date

    def get_sex(self):
        return self.sex

    def get_weight(self):
        return self.weight

    def get_patient_id(self):
        return self.patient_id

    def get_id_type(self):
        return self.id_type

    def get_diagnosis(self):
        return self.diagnosis

    # Method to update diagnosis with logging
    def update_diagnosis(self, new_diagnosis):
        logging.info(f"Updating diagnosis for patient {self.patient_id} from {self.diagnosis} to {new_diagnosis}")
        self.diagnosis = new_diagnosis

    def __str__(self):
        return (f"Patient Record:\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Birth Date: {self.birth_date}\n"
                f"Sex: {self.sex}\n"
                f"Weight: {self.weight}\n"
                f"Patient ID: {self.patient_id} ({self.id_type})\n"
                f"Diagnosis: {self.diagnosis}")
    

class StudyRecord(PatientRecord):
    def __init__(self, name, age, birth_date, sex, weight, patient_id, id_type, modality=None, study_date=None, study_time=None, study_instance_uid=None, series_number=None, number_of_frames=None):
        super().__init__(name, age, birth_date, sex, weight, patient_id, id_type)
        self.modality = modality
        self.study_date = study_date
        self.study_time = study_time
        self.study_instance_uid = study_instance_uid
        self.series_number = series_number
        self.number_of_frames = number_of_frames
        
    def set_modality(self, modality):
        self.modality = modality
        
    def set_study_date(self, study_date):
        self.study_date = study_date
        
    def set_study_time(self, study_time):
        self.study_time = study_time
        
    def set_study_instance_uid(self, study_instance_uid):
        self.study_instance_uid = study_instance_uid
        
    def set_series_number(self, series_number):
        self.series_number = series_number
        
    def set_number_of_frames(self, number_of_frames):
        self.number_of_frames = number_of_frames
        
    def get_modality(self):
        return self.modality
    
    def get_study_date(self):
        return self.study_date
    
    def get_study_time(self):
        return self.study_time
    
    def get_study_instance_uid(self):
        return self.study_instance_uid
    
    def get_series_number(self):
        return self.series_number
    
    def get_number_of_frames(self):
        return self.number_of_frames
    
    def load_from_dicom(self, dicom_file):
        ds = pydicom.dcmread(dicom_file)
        self.set_modality(ds.Modality)
        self.set_study_date(ds.StudyDate)
        self.set_study_time(ds.StudyTime)
        self.set_study_instance_uid(ds.StudyInstanceUID)
        self.set_series_number(ds.SeriesNumber)
        self.set_number_of_frames(getattr(ds, 'NumberOfFrames', None))

        # Assuming patient information is also stored in the DICOM file
        self.set_name(ds.PatientName)
        self.set_age(ds.get('PatientAge', None))
        self.set_birth_date(ds.PatientBirthDate)
        self.set_sex(ds.PatientSex)
        self.set_weight(ds.get('PatientWeight', None))
        self.set_patient_id(ds.PatientID)
        self.set_id_type('DICOM')
        
def __str__(self):
        return (super().__str__() + "\n"
                f"Study Record:\n"
                f"Modality: {self.modality}\n"
                f"Study Date: {self.study_date}\n"
                f"Study Time: {self.study_time}\n"
                f"Study Instance UID: {self.study_instance_uid}\n"
                f"Series Number: {self.series_number}\n"
                f"Number of Frames: {self.number_of_frames}")
        
        
study_instance = StudyRecord(name="Orion Guevara", age=23, birth_date="2001-02-13", sex="M", weight=65, patient_id="1193142789", id_type="CC")
print(study_instance)

study_instance.update_diagnosis("Hello World")

study_instance.load_from_dicom('./sample-02-dicom.dcm')

print(study_instance)
