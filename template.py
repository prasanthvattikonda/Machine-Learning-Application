import os, sys
from pathlib import Path
import logging

while True:
    Project_name = input("Enter your project name: ")
    if Project_name != "":
        break


#src/__init__.py
#src/components/__init__.py
#


list_of_files = [
    f"{Project_name}/__init__.py",
    f"{Project_name}/components/__init__.py",
    f"{Project_name}/config/__init__.py",
    f"{Project_name}/logger/__init__.py",
    f"{Project_name}/exception/__init__.py",
    f"{Project_name}/constant/__init__.py",
    f"{Project_name}/pipeline/__init__.py",
    f"{Project_name}/utils/__init__.py",
    f"{Project_name}/entity/__init__.py",
    f"config/config.yaml",
    f"config/schema.yaml",
    "schema.yaml",
    "setup.py",
    "main.py",
    "app.py",
    "logs.py",
    "exception.py",
    "requirements.txt",
    "dvc.yaml"

]
# Folder & Files

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
# 

    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, "w") as f:
            pass
    else:
        logging.info(f"file is already present at {filepath}")