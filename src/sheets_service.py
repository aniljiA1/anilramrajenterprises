import os
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request  # Needed for refresh

# ---------------- CONFIG ----------------
TOKEN_FILE = "token.json"  # will store your credentials after first login
# Use this path if your credentials are inside a folder called 'credentials'
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), "..", "credentials", "credentials.json")

SPREADSHEET_ID = "<PASTE_YOUR_SPREADSHEET_ID_HERE>"  # replace with your actual sheet ID
SHEET_NAME = "Emails"  # your sheet/tab name
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]  # full access
# ----------------------------------------

def authenticate_sheets():
    creds = None
    # Load token if it exists
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    # If no valid creds, login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save token for next run
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
    return build("sheets", "v4", credentials=creds)

def load_state(state_file):
    if os.path.exists(state_file):
        with open(state_file, "r") as f:
            return json.load(f)
    return {"processed_ids": []}

def save_state(state_file, state):
    with open(state_file, "w") as f:
        json.dump(state, f)

def append_to_sheet(service, row):
    
    body = {"values": [row]}
    result = service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=f"{SHEET_NAME}!A:D",
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()
    return result
