import base64
from bs4 import BeautifulSoup
from dateutil import parser


def decode_payload(encoded_data: str) -> str:
    """
    Gmail API returns message bodies as urlsafe base64.
    This helper decodes it safely and ignores bad characters.
    """
    if not encoded_data:
        return ""

    try:
        return base64.urlsafe_b64decode(encoded_data).decode(
            "utf-8", errors="ignore"
        )
    except Exception:
        # In rare cases decoding fails (malformed payload)
        return ""


def extract_email_data(service, message_id: str) -> dict:
    """
    Fetches a single Gmail message and extracts
    from, subject, date and readable content.
    """

    message = service.users().messages().get(
        userId="me",
        id=message_id,
        format="full"
    ).execute()

    payload = message.get("payload", {})
    headers = payload.get("headers", [])

    email_data = {
        "from": "",
        "subject": "",
        "date": "",
        "content": ""
    }

    # Read standard email headers
    for header in headers:
        name = header.get("name")
        value = header.get("value", "")

        if name == "From":
            email_data["from"] = value
        elif name == "Subject":
            email_data["subject"] = value
        elif name == "Date":
            try:
                email_data["date"] = parser.parse(value).isoformat()
            except Exception:
                email_data["date"] = value

    def extract_body(parts: list) -> str:
        """
        Gmail messages can be deeply nested.
        Prefer plain text, fallback to HTML if needed.
        """
        for part in parts:
            mime_type = part.get("mimeType")
            body = part.get("body", {})

            if mime_type == "text/plain":
                return decode_payload(body.get("data"))

            if mime_type == "text/html":
                html = decode_payload(body.get("data"))
                return BeautifulSoup(html, "html.parser").get_text()

            # Some parts contain further nested parts
            if "parts" in part:
                content = extract_body(part["parts"])
                if content:
                    return content

        return ""

    # Handle multipart and single-part messages
    if "parts" in payload:
        email_data["content"] = extract_body(payload["parts"])
    else:
        email_data["content"] = decode_payload(
            payload.get("body", {}).get("data")
        )

    return email_data

