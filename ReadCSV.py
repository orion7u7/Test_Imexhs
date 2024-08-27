import os
import pandas as pd
import logging

logging.basicConfig(level=logging.ERROR , format='%(asctime)s - %(levelname)s - %(message)s')

def read_csv(path, file_name):
    file_path = os.path.join(path, file_name)

    try:
        df = pd.read_csv(file_path)
        numeric_cols = df.select_dtypes(include='number').columns
        numeric_rows = df.select_dtypes(include='number').index
        print("The numeric columns are: ")
        for col in numeric_cols:
            print(col)
        print("Number of numeric columns: ", len(numeric_cols))
        print("Number of numeric rows: ", len(numeric_rows))

        print("The average of the numeric columns is: ")
        for col in numeric_cols:
            print(col, ": ", df[col].mean())

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