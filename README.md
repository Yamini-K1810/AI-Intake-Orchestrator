# AI Agent Development Internship Project

## Overview

This project implements a **Multi-Format Intake Agent with Intelligent Routing & Context Memory**.

The system accepts inputs in **PDF, JSON, or Email** formats, classifies the format and intent, routes the data to specialized agents for extraction, and maintains context in a shared memory for downstream use.

---

## Features

- **Classifier Agent**: Detects input format (PDF, JSON, Email) and intent (Invoice, RFQ, Complaint, etc.).
- **JSON Agent**: Validates JSON payloads, extracts fields, and detects anomalies.
- **Email Parser Agent**: Extracts sender info, urgency, intent, and conversation metadata from emails.
- **Shared Memory Module**: Stores metadata and extracted data accessible across agents.
- **Orchestrator (MCP)**: Central controller to coordinate classification, routing, and memory updates.

---

## Tech Stack

- Python 3.8+
- Libraries: `re`, `json`, `uuid`, `time`
- Optional: Docker (not implemented in this version)
  
---

## Folder Structure

/agents
├── classifier_agent.py
├── email_parser_agent.py
└── json_agent.py
/mcp
└── orchestrator.py
/memory
└── memory_store.py
/data
├── sample_email.txt
└── sample_json.json
/app.py
README.md


---

## How to Run

1. Clone the repo
2. Install Python 3.8+ if not already installed
3. Run the main app:

```bash
python app.py
