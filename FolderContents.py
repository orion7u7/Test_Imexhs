import os

def count_folder_contents(path):
    try:
        return len(os.listdir(path))
    except FileNotFoundError:
        print("The specified path does not exist.")
    except NotADirectoryError:
        print("The specified path is not a directory.")

path = "D:/Documentos/pruebas/Test_Imexhs"
print("The folder contains ", count_folder_contents(path), " elements")