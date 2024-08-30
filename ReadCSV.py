import os
import pandas as pd
import logging

logging.basicConfig(level=logging.ERROR , format='%(asctime)s - %(levelname)s - %(message)s')

# This function reads a CSV file and prints the numeric columns, the number of numeric columns and rows, the average and the standard deviation of the numeric columns
def read_csv(path, file_name):
    file_path = os.path.join(path, file_name)

    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        numeric_cols = df.select_dtypes(include='number').columns
        numeric_rows = df.select_dtypes(include='number').index
        print("The numeric columns are: ")
        
        # Print the numeric columns
        for col in numeric_cols:
            print(col)
        print("Number of numeric columns: ", len(numeric_cols))
        print("Number of numeric rows: ", len(numeric_rows))

        # Print the average and the standard deviation of the numeric columns
        print("The average of the numeric columns is: ")
        for col in numeric_cols:
            print(col, ": ", df[col].mean())

        # Print the standard deviation of the numeric columns
        print("The standard deviation of the numeric columns is: ")
        for col in numeric_cols:
            print(col, ": ", df[col].std())

    except FileNotFoundError:
        logging.error("The file does not exist.")
    except PermissionError:
        logging.error("The file is not accessible.")
    except pd.errors.EmptyDataError:
        logging.error("The file is empty.")
    except pd.errors.ParserError:
        logging.error("The file is not a CSV.")
    except Exception as e:
        logging.error("An error occurred: ", e)



path = "D:/Documentos/pruebas/Test_Imexhs"
file_name = "sample-01-csv.csv"
read_csv(path, file_name)