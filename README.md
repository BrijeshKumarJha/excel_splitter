# 📊 Smart Excel Data Splitter

An advanced, interactive Python automation tool that intelligently reads a master Excel file, dynamically extracts its columns, and splits the massive dataset into multiple smaller Excel files based on the user's chosen criteria.

##  The Problem it Solves
In corporate environments (HR, Finance, Sales), managers often have massive "Master Sheets" containing thousands of rows of data. Manually filtering and copy-pasting data to send department-specific or region-specific reports takes hours and is prone to human error. This tool automates the entire workflow in seconds.

##  Features
* **Universal Compatibility:** Does not rely on hardcoded column names. It dynamically reads any `.xlsx` file and generates an interactive menu of available filters.
* **Smart Data Filtering:** Utilizes `pandas` Boolean Indexing to rapidly parse and segment data without missing rows.
* **Automated Directory Management:** Automatically creates clean output folders (e.g., `Split_Files_Department`) to prevent cluttering the main directory.
* **Safe Naming Conventions:** Automatically sanitizes output file names by replacing spaces and slashes to prevent OS-level saving errors.

##  Example Workflow

**Before (One Massive File):**
```text
project_folder/
└── master_data.xlsx 
```

**After Running the Script (Automatically Segmented):**
```text
project_folder/
├── master_data.xlsx
└── Split_Files_Department/
    ├── Department_IT.xlsx
    ├── Department_HR.xlsx
    ├── Department_Sales.xlsx
    └── Department_Finance.xlsx
```

## How to Use
* Clone this repository to your local machine:
**Bash**
git clone [https://github.com/BrijeshKumarJha/smart-excel-splitter.git](https://github.com/BrijeshKumarJha/smart-excel-splitter.git)

* Navigate to the project directory:
**Bash**
cd smart-excel-splitter

* Install the required data science libraries (pandas and openpyxl):
**Bash**
pip install pandas openpyxl

* Run the script:
**Bash**
python splitter.py
Enter the name of your Excel file when prompted, and choose your dynamic filter from the generated menu!

💻 Tech Stack
Language: Python 3

Core Data Engine: pandas (For DataFrame manipulation and Boolean indexing)

Excel Engine: openpyxl (For reading/writing .xlsx binaries)

Path Management: pathlib
