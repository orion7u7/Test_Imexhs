import os
import pydicom as dicom
import logging 

logging.basicConfig(level=logging.ERROR , format='%(asctime)s - %(levelname)s - %(message)s')

# This function reads a DICOM file and prints the Patient's Name, Study Date and Modality
def read_dicom(path, file_name):
    file_path = os.path.join(path, file_name)

    try:
        # Read the DICOM file
        ds = dicom.dcmread(file_path)
        
        # Print the Patient's Name, Study Date and Modality
        print(f"Patient's Name: {ds.PatientName}")
        print(f"Study Date: {ds.StudyDate}")
        print(f"Modality: {ds.Modality}")
            
    except FileNotFoundError:
        logging.error("The file does not exist.")
    except PermissionError:
        logging.error("The file is not accessible.")
    except dicom.errors.InvalidDicomError:
        logging.error("The file is not a DICOM.")
    except Exception as e:
        logging.error("An error occurred: ", e)
        
# This function reads a DICOM file and prints the value of a tag given its number and element
def read_by_tagNumber(path, file_name, tag_number, tag_element):
    file_path = os.path.join(path, file_name)

    # Read the DICOM file
    try:
        ds = dicom.dcmread(file_path)
        tag = dicom.tag.Tag(tag_number, tag_element)
        print(ds[tag])
            
    except FileNotFoundError:
        logging.error("The file does not exist.")
    except PermissionError:
        logging.error("The file is not accessible.")
    except dicom.errors.InvalidDicomError:
        logging.error("The file is not a DICOM.")
    except Exception as e:
        logging.error("An error occurred: ", e)


path = "D:/Documentos/pruebas/Test_Imexhs"
file_name = "sample-01-dicom.dcm"
read_dicom(path, file_name)
read_by_tagNumber(path, file_name, 0x0008, 0x0016)

