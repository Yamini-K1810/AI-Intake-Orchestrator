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

flowbit-ai-intake-system/
├── agents/
│ ├── classifier_agent.py # Classifies input format and intent
│ ├── email_parser_agent.py # Parses email text for metadata
│ └── json_agent.py # Validates and extracts fields from JSON
│
├── memory/
│ └── memory_store.py # Lightweight shared memory for context
│
├── mcp/
│ └── orchestrator.py # Orchestrates end-to-end flow between agents
│
├── data/
│ ├── sample_email.txt # Sample email input
│ └── sample_json.json # Sample JSON input
│
├── app.py # Entry point for testing the full pipeline
├── README.md # Project documentation and setup instructions

---

## How to Run

1. Clone the repo
2. Install Python 3.8+ if not already installed
3. Run the main app:

```bash
python app.py
