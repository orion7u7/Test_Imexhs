# IMEXHS Developer Test
This repository contains the implementation of the IMEXHS Developer Test for a Python Developer I position. The test is designed to evaluate various aspects of Python programming skills, including file handling, object-oriented programming, multithreading, API development, and system architecture design.


## Repository Structure
The repository is organized into the following branches, each corresponding to a specific section of the test:
- ### main: 
    Contains this README and general project information.
- ### 1.File&Array: 
    Implementation of file handling and array operations.
- ### 2.OOP: 
    Object-oriented programming implementation for patient and study records.
- ### 3.Multithreading: 
    Multithreading and concurrency tasks.
- ### 4.APIRestful: 
    Django-based RESTful API for managing medical image processing results.
- ### 5.Design&Architecture: 
    Design document for a distributed DICOM processing system.

## Test Sections
1. File Handling and Array Operations
    - List folder contents
    - Read and analyze CSV files
    - Read and extract information from DICOM files

2. Object-Oriented Programming (OOP)
    - Implementation of PatientRecord class
    - Implementation of StudyRecord class (inherits from PatientRecord)
    - DICOM file integration

3. Multithreading and Concurrency
    - Even and odd number printing with separate threads
    - JSON file processing with multiple threads

4. API Restful Design
    - Django-based RESTful API for CRUD operations
    - PostgreSQL database integration
    - Input validation and error handling

5. Distributed DICOM Processing System (Design and Architecture)
    - System architecture design for processing large batches of medical images
    - Considerations for scalability, fault tolerance, and security

## Getting Started
To review the implementations for each section, please check out the corresponding branch. Each branch contains the necessary code, documentation, and any additional resources required for that specific part of the test.

## Requirements
- Python 3.x
- Django (for the API section)
- PostgreSQL (for the API section)
- Additional libraries as specified in each section