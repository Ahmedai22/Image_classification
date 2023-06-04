import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
                    # everything in the brackets is just a personal format style

project_name = "cnnClasifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",# initialize the file so that modules in it can be imported directly
    f"src/{project_name}/components/__init__.py", # making a local package folder as explained in the above comment
    f"src/{project_name}/utils/__init__.py", # __init__.py is called constructor file
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configration",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml", # ML DevOps tool
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"


]


for filepath in list_of_files:
    filepath = Path(filepath) # using this Path funciton as windows uses "/", --> this will convert it into "\"
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Crating directory: {filedir}, for the file:{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")
    else:
        logging.info("file already exists")