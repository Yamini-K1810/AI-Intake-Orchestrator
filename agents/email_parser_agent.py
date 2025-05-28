import re
from agents.classifier_agent import classify_input

def extract_email_metadata(email_body: str) -> dict:
    metadata = {}

    # Extract sender
    sender_match = re.search(r"From:\s*(.*?)(?:\n|$)", email_body, re.IGNORECASE)
    if sender_match:
        metadata["sender"] = sender_match.group(1).strip()

    # Extract urgency based on keywords
    urgency_keywords = {
        "high": ["urgent", "asap", "immediately", "important"],
        "low": ["no rush", "whenever", "not urgent"],
        "normal": []
    }
    urgency = "normal"
    for level, keywords in urgency_keywords.items():
        if any(k in email_body.lower() for k in keywords):
            urgency = level
            break
    metadata["urgency"] = urgency

    # Extract intent using the classifier
    _, intent = classify_input(email_body)
    metadata["intent"] = intent

    # Extract conversation ID (simple version)
    conv_match = re.search(r"Conversation-ID:\s*(\S+)", email_body, re.IGNORECASE)
    if conv_match:
        metadata["conversation_id"] = conv_match.group(1).strip()

    return metadata
