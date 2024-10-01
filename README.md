# Python Automation and API Project

This project demonstrates Python automation scripts and a simple REST API.

## Requirements

- Python 3.x
- Flask
- psutil

## Installation

```bash
pip install -r requirements.txt
```

## Running Automation

Run the file operations automation:
```bash
python automation/file_operations.py
```

Check system monitoring:
```bash
python automation/system_monitoring.py
```

## Running the API

```bash
python api/app.py

```
# Using powershell
    $env:FLASK_APP="api/app.py"
    flask run


API Endpoints:
- `/api/status`: Check API status
- `/api/health`: Check system health
