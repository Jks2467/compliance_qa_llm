import os
from pathlib import Path # For handling file paths robustly
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = 'backend'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/data/__init__.py",
    f"{project_name}/scripts/__init__.py",
    f"{project_name}/src/__init__.py",
    f"{project_name}/tests/__init__.py",
    f"{project_name}/src/api/__init__.py",
    f"{project_name}/src/graph/__init__.py",
    f"{project_name}/src/services/__init__.py",
    f"{project_name}/src/api/server.py",
    f"{project_name}/src/api/telemetry.py",
    f"{project_name}/src/graph/nodes.py",
    f"{project_name}/src/graph/state.py",
    f"{project_name}/src/graph/workflow.py",
    f"{project_name}/src/services/video_indexer.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py"
]


# Loop through the list of files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    # Create directory if it does not exist
    if filedir !="":
        os.makedirs (filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    # Create empty file if it does not exist
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f" {filename} is already exists")