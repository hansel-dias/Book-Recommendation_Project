import os
from pathlib import Path
import logging 


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'book_recommender'

list_of_files = [
    ".github/workflows/.gitkeep",  # GitHub Actions: Keep the directory structure for workflows
    'src/components/__init__.py',  # Source Code: Initialization file for components module
    'src/utilis/__init__.py',      # Source Code: Initialization file for utils module
    'src/config/__init__.py',      # Source Code: Initialization file for configuration module
    'src/config/configuration.py', # Source Code: Configuration module with settings
    'src/pipeline/__init__.py',    # Source Code: Initialization file for pipeline module
    'src/entity/__init__.py',      # Source Code: Initialization file for entity module
    'src/constants/__init__.py',   # Source Code: Initialization file for constants module
    'config/config.yaml',          # Configuration: YAML file for project settings
    'dvc.yaml',                    # Data Version Control: DVC configuration file
    'params.yaml',                 # Parameters: YAML file containing project parameters
    'requirements.txt',            # Requirements: File listing required Python packages
    'setup.py',                    # Project Setup: Python setup script for project installation
    'research/trials.ipynb',       # Research: Jupyter Notebook for experimentation and trials
    'test.py',                      # Test: Python script for testing purposes
    'templates/index.html',
    'src/__init__.py'
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating diretory:{filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creatile empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")