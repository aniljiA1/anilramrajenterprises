from .gmail_service import authenticate_gmail, fetch_unread_emails, mark_as_read
from .sheets_service import (
    authenticate_sheets,
    append_to_sheet,
    load_state,
    save_state
)
from .email_parser import extract_email_data
from config import STATE_FILE

def main():
    gmail_service = authenticate_gmail()
    sheets_service = authenticate_sheets()
    state = load_state(STATE_FILE)

    messages = fetch_unread_emails(gmail_service)

    for msg in messages:
        msg_id = msg["id"]

        if msg_id in state["processed_ids"]:
            continue

        email = extract_email_data(gmail_service, msg_id)

        append_to_sheet(
            sheets_service,
            [
                email["from"],
                email["subject"],
                email["date"],
                email["content"]
            ]
        )

        mark_as_read(gmail_service, msg_id)
        state["processed_ids"].append(msg_id)

    save_state(STATE_FILE, state)

if __name__ == "__main__":
    main()
