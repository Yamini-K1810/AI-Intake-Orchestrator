import json
from agents.classifier_agent import classify_input
from agents.json_agent import validate_and_extract_json
from agents.email_parser_agent import extract_email_metadata
from memory.memory_store import SharedMemory

class Orchestrator:
    def __init__(self):
        self.memory = SharedMemory()

    def handle_input(self, input_data, input_type="text"):
        # Step 1: Format + Intent Detection
        input_str = input_data if isinstance(input_data, str) else json.dumps(input_data)
        format_type, intent = classify_input(input_str)

        # Step 2: Create memory record
        record_id = self.memory.create_record(
            source_type=input_type,
            original_input=input_data,
            format_type=format_type,
            intent=intent
        )

        # Step 3: Route to Agent
        if format_type == "Email":
            parsed_data = extract_email_metadata(input_str)
            conversation_id = parsed_data.pop("conversation_id", None)
            if conversation_id:
                self.memory.set_conversation_id(record_id, conversation_id)
            self.memory.update_record(record_id, parsed_data)

        elif format_type == "JSON":
            try:
                parsed_json = input_data if isinstance(input_data, dict) else json.loads(input_data)
                extracted, anomalies = validate_and_extract_json(parsed_json)
                self.memory.update_record(record_id, extracted)
                self.memory.update_record(record_id, {"anomalies": anomalies})
            except Exception as e:
                self.memory.update_record(record_id, {"error": str(e)})

        elif format_type == "PDF":
            # Placeholder (not implemented in this version)
            self.memory.update_record(record_id, {"note": "PDF parsing not implemented yet."})

        else:
            self.memory.update_record(record_id, {"error": "Unsupported input format"})

        # Step 4: Return full structured memory record
        return self.memory.get_record(record_id)
