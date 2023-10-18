import yaml
import os, sys
import pandas as pd

def write_Schema_yaml(csv_file):
    df = pd.read_csv(csv_file)

    num_cols = len(df.columns)

    columns_names = df.columns.tolist()

    column_dtypes = df.dtypes.astype(str).tolist() # | . int

    # Create Schem Dictinoary

    schema = {

        "Filename": os.path.basename(csv_file),
        "NumberofColumns": num_cols,
        "ColumnNames": dict(zip(columns_names, column_dtypes))
    }

    # Write schema to schema.yaml file

    ROOT_DIR = os.getcwd()
    SCHEMA_PATH = os.path.join(ROOT_DIR, 'config', 'schema.yaml')

    with open(SCHEMA_PATH, "w") as file:
        yaml.dump(schema, file)


