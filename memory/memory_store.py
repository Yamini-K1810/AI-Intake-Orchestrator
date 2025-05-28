import time
import uuid

class SharedMemory:
    def __init__(self):
        self.memory = {}

    def create_record(self, source_type, original_input, format_type, intent):
        record_id = str(uuid.uuid4())
        self.memory[record_id] = {
            "id": record_id,
            "source_type": source_type,
            "timestamp": time.time(),
            "format": format_type,
            "intent": intent,
            "original_input": original_input,
            "extracted_data": {},
            "conversation_id": None
        }
        return record_id

    def update_record(self, record_id, data: dict):
        if record_id in self.memory:
            self.memory[record_id]["extracted_data"].update(data)
        else:
            raise KeyError(f"Record {record_id} not found")

    def set_conversation_id(self, record_id, conversation_id):
        if record_id in self.memory:
            self.memory[record_id]["conversation_id"] = conversation_id

    def get_record(self, record_id):
        return self.memory.get(record_id, None)

    def all_records(self):
        return self.memory
