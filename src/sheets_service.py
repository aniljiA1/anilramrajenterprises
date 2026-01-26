import os
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

from config import (
    SHEETS_SCOPES,
    CREDENTIALS_FILE,
    TOKEN_FILE,
    SPREADSHEET_ID,
    SHEET_NAME
)


def authenticate_sheets():
    """
    Authenticates Google Sheets API using OAuth.
    """
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(
            TOKEN_FILE, SHEETS_SCOPES
        )

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SHEETS_SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return build("sheets", "v4", credentials=creds)


def load_state(state_file: str) -> dict:
    """
    Keeps track of processed message IDs
    to avoid duplicate sheet entries.
    """
    if os.path.exists(state_file):
        with open(state_file, "r") as f:
            return json.load(f)

    return {"processed_ids": []}


def save_state(state_file: str, state: dict):
    with open(state_file, "w") as f:
        json.dump(state, f)


def append_to_sheet(service, row: list):
    """
    Appends a single row to the target sheet.
    """
    body = {"values": [row]}

    return service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=f"{SHEET_NAME}!A:D",
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()
