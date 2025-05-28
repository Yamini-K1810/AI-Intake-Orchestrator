import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mcp.orchestrator import Orchestrator
import json

if __name__ == "__main__":
    orchestrator = Orchestrator()

    # Email input test
    with open("data/sample_email.txt", "r") as f:
        email_text = f.read()
    email_output = orchestrator.handle_input(email_text, input_type="email")
    print("📧 Email Result:\n", json.dumps(email_output, indent=2))

    # JSON input test
    with open("data/sample_json.json", "r") as f:
        json_input = json.load(f)
    json_output = orchestrator.handle_input(json_input, input_type="json")
    print("\n📦 JSON Result:\n", json.dumps(json_output, indent=2))
