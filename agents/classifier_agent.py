import re
import json
from typing import Tuple

def classify_input(input_data: str) -> Tuple[str, str]:
    """
    Classify the format and intent of the input.

    Returns:
        format_type: 'PDF', 'JSON', 'Email'
        intent: 'Invoice', 'RFQ', 'Complaint', etc.
    """
    # Format detection
    if input_data.strip().endswith(".pdf"):
        format_type = "PDF"
    elif input_data.strip().startswith("{") and input_data.strip().endswith("}"):
        format_type = "JSON"
    elif "From:" in input_data or re.search(r"@.*\.\w+", input_data):
        format_type = "Email"
    else:
        format_type = "Unknown"

    # Intent classification (simple rule-based for now)
    intent_keywords = {
        "Invoice": ["invoice", "billing"],
        "RFQ": ["quote", "rfq", "request for quotation"],
        "Complaint": ["complaint", "issue", "problem"],
        "Regulation": ["compliance", "regulation", "policy"]
    }

    intent = "Unknown"
    for key, keywords in intent_keywords.items():
        if any(word in input_data.lower() for word in keywords):
            intent = key
            break

    return format_type, intent
