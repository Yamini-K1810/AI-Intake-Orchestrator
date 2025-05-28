from typing import Tuple, Dict

REQUIRED_FIELDS = ["customer_name", "product_id", "quantity", "delivery_date"]

def validate_and_extract_json(input_json: dict) -> Tuple[Dict, Dict]:
    """
    Validates JSON input and extracts required fields.
    
    Returns:
        - extracted data
        - anomalies (missing/invalid fields)
    """
    extracted = {}
    anomalies = {}

    for field in REQUIRED_FIELDS:
        value = input_json.get(field)
        if value is None:
            anomalies[field] = "Missing"
        else:
            if field == "quantity" and not isinstance(value, int):
                anomalies[field] = f"Expected int, got {type(value).__name__}"
            else:
                extracted[field] = value

    return extracted, anomalies
