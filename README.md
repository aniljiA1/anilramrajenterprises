# Gmail to Google Sheets

A Python script that automatically reads emails from your Gmail account and appends data to a Google Sheet. Built with **Google Sheets API** and **OAuth2 authentication**.

---

## Features

- Connects to Gmail (or any email source you configure).  
- Appends email data (sender, subject, date, etc.) to Google Sheets.  
- Keeps track of processed emails to avoid duplicates.  
- Easy setup using OAuth 2.0 credentials.  
- Fully configurable spreadsheet and sheet name.

---

## Demo

Screenshot1: https://drive.google.com/file/d/1Iz4NrUP35NqE_DwSOwXjOAVqCDPIlASa/view?usp=sharing 
Screenshot2: https://drive.google.com/file/d/1E8Ylm89Kxe-SwcgF7EtXni8J19c9iW5o/view?usp=sharing
Screenshot3: https://drive.google.com/file/d/1PAIUb1Yqu1PB_cQb1mZr0lCDDmBlg9ql/view?usp=sharing

---

## Prerequisites

- Python 3.10+  
- Google account  
- Google Cloud project with **Google Sheets API** enabled  
- `pip` for Python dependencies

---

## Installation


# Windows PowerShell
python -m venv venv
& .\venv\Scripts\Activate.ps1

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
Install dependencies:


pip install -r requirements.txt
Add credentials:

Create OAuth 2.0 credentials in Google Cloud Console.

Download the JSON and place it in gmail-to-sheets/credentials/credentials.json.

Update config.py:

python

SPREADSHEET_ID = "YOUR_GOOGLE_SHEET_ID"
SHEET_NAME = "Emails"
Usage
Activate your virtual environment (if not already active):

powershell

& .\venv\Scripts\Activate.ps1
Run the script:

python -m src.main

On first run, a browser window will open asking you to log in to your Google account.

After authentication, a token.json file will be created for future runs.

The script will append email data to your Google Sheet.

Project Structure

gmail-to-sheets/
├─ credentials/         # OAuth credentials file goes here
├─ src/                 # Python source code
│  ├─ main.py           # Main script
│  └─ sheets_service.py # Google Sheets API helper
├─ venv/                # Python virtual environment
├─ config.py            # Configuration (spreadsheet ID, sheet name, etc.)
├─ requirements.txt     # Python dependencies
└─ README.md
Dependencies
google-api-python-client

google-auth-httplib2

google-auth-oauthlib

Install with:

pip install -r requirements.txt

Author
Anil Kumar
