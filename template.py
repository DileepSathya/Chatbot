import os,sys
from pathlib import Path
import logging
while True:
    project_name=input("Enter your project name")
    if project_name !='':
        break
list_of_files=[
    f"{project_name}/__init__.py",#src/__init__.py
    f"{project_name}/component/__init__py",#src/component/__init__.py
    f"{project_name}/config/__init__py",
    f"{project_name}/constants/__init__py",
    f"{project_name}/entity/__init__py",
    f"{project_name}/exception/__init__py",
    f"{project_name}/logger/__init__py",
    f"{project_name}/pipeline/__init__py",
    f"{project_name}/utils/__init__py",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"
]
for file in list_of_files:
    filepath=Path(file)
    filedr,filename=os.path.split(filepath)

    if filedr!="":
        os.makedirs(filedr,exist_ok=True)
    
    if(not os.path.exists(filepath)or(os.path.getsize(filepath))==0):
        with open(filepath,'w') as f:
            pass
    
    else:
        logging.info("file is already present at: {fielpath}")