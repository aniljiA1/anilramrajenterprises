import base64
from bs4 import BeautifulSoup
from dateutil import parser

def _decode_payload(data):
    decoded = base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")
    return decoded

def extract_email_data(service, message_id):
    message = service.users().messages().get(
        userId="me", id=message_id, format="full"
    ).execute()

    headers = message["payload"]["headers"]
    payload = message["payload"]

    email_data = {
        "from": "",
        "subject": "",
        "date": "",
        "content": ""
    }

    for header in headers:
        if header["name"] == "From":
            email_data["from"] = header["value"]
        elif header["name"] == "Subject":
            email_data["subject"] = header["value"]
        elif header["name"] == "Date":
            email_data["date"] = parser.parse(header["value"]).isoformat()

    def get_body(parts):
        for part in parts:
            if part.get("mimeType") == "text/plain":
                return _decode_payload(part["body"]["data"])
            if part.get("mimeType") == "text/html":
                html = _decode_payload(part["body"]["data"])
                return BeautifulSoup(html, "html.parser").get_text()
            if "parts" in part:
                result = get_body(part["parts"])
                if result:
                    return result
        return ""

    if "parts" in payload:
        email_data["content"] = get_body(payload["parts"])
    else:
        email_data["content"] = _decode_payload(payload["body"]["data"])

    return email_data
