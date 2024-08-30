# File Handling and Array Operations

This branch contains Python scripts designed to handle various file operations, including listing folder contents, reading CSV files, and reading DICOM files. The provided scripts allow you to perform these tasks efficiently while logging any errors that may occur during the process.

## File Structure

- `FolderContents.py`: Script for counting the contents of a specified folder.
- `ReadCSV.py`: Script for reading a CSV file, providing information about its columns, rows, and basic statistics (average and standard deviation) for numeric columns.
- `ReadDICOM.py`: Script for reading a DICOM file and extracting patient information, study details, and specific DICOM tags.
- `sample-01-csv.csv`: Sample CSV file used for testing the `ReadCSV.py` script.
- `sample-01-dicom.dcm`: Sample DICOM file used for testing the `ReadDICOM.py` script.

## Requirements

- Python 3.x
- `pandas` library for handling CSV files
- `numpy` library for numerical operations
- `pydicom` library for reading DICOM files
