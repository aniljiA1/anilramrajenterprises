# Gmail to Google Sheets Automation

This project is a small automation script that reads **unread Gmail messages** and stores
their basic details in a **Google Sheet**.

I built this mainly to understand how Gmail and Google Sheets APIs work together,
how OAuth behaves in real scenarios, and how to structure a simple but maintainable
Python utility.

---

## What the script does

- Reads unread emails from Gmail inbox
- Extracts:
  - Sender
  - Subject
  - Date
  - Readable email content
- Appends the data as a new row in Google Sheets
- Marks emails as **read** after processing
- Keeps track of processed emails to avoid duplicates

---

## Why this approach

- I used **Gmail `modify` scope** so emails can be marked as read after processing  
- A simple **JSON state file** is used instead of a database to keep the script lightweight  
- The project is run as a Python module (`python -m src.main`) to keep imports clean and scalable  
- No unnecessary abstractions — the goal was clarity and correctness

---

## Project Structure

gmail-to-sheets/
│
├── src/
│ ├── main.py
│ ├── gmail_service.py
│ ├── sheets_service.py
│ ├── email_parser.py
│ ├── config.py
│ └── init.py
│
├── credentials/
│ └── credentials.json 
├── requirements.txt
├── .gitignore
└── README.md


---

## Tech Stack

- Python 3
- Gmail API
- Google Sheets API
- OAuth 2.0

---

## How to Run

1. Create a virtual environment and install dependencies:

pip install -r requirements.txt
Place your Google OAuth credentials file here:

credentials/credentials.json

Run the script from the project root:

python -m src.main

## Demo

Screenshot1: https://drive.google.com/file/d/1Iz4NrUP35NqE_DwSOwXjOAVqCDPIlASa/view?usp=sharing 
Screenshot2: https://drive.google.com/file/d/1E8Ylm89Kxe-SwcgF7EtXni8J19c9iW5o/view?usp=sharing
Screenshot3: https://drive.google.com/file/d/1PAIUb1Yqu1PB_cQb1mZr0lCDDmBlg9ql/view?usp=sharing

Author
Anil Kumar
GitHub: https://github.com/aniljiA1



