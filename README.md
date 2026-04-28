# climate-challenge-week0.
## KAIM Cohort 9 Week 0 Challenge African Climate Trend Analysis
---
# KAI M Week O Challenge Environment Setup
MoonLight Energy Solutions Solar Challenge Week 1 Version Control using Git


##  How to Reproduce the Environment

Follow these steps to set up the same development environment locally:

### 1. Clone the repository
```bash
git clone https://github.com/Helina-Yilma/solar-challenge-week1.git
cd yourLocalFolderPath
```
### 2. Create and activate a virtual environment
For windows
```bash
python -m venv venv 
venv\Scripts\activate or  ./venv/Scripts/Activate.ps1 
```
### 3. Install dependencies

Make sure you have pip up to date, then install all required libraries:
``` bash
pip install --upgrade pip
pip install -r requirements.txt
```
### 4. Verify installation

You can test the setup by checking Python and installed packages:
``` bash
python --version
pip list
```
### 5. Run CI Workflow

This repository includes a GitHub Actions workflow (.github/workflows/ci.yml) that automatically installs dependencies and verifies the Python environment on each push or pull request.

Folder Structure
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md

### Installed Dependencies

The current environment includes:

* pandas
* numpy
* seaborn
* matplotlib
* scipy