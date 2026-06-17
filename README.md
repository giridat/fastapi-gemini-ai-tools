# AI Practice - FastAPI + Gemini

A collection of AI-powered backend services built using FastAPI, Gemini, and Python as part of my transition from Software Engineering to Generative AI Application Development.

## Features

### Flutter Code Review API

Analyzes Flutter code and provides:

* Code quality feedback
* Architecture suggestions
* Performance improvements
* Best practice recommendations

### AI Bug Report Generator

Generates structured bug reports from issue descriptions.

Outputs:

* Summary
* Severity
* Priority
* Root Cause Analysis
* Steps to Reproduce

### AI Jira Ticket Generator

Automatically converts issue descriptions into Jira-ready tickets.

Outputs:

* Title
* Description
* Severity
* Priority
* Labels

## Tech Stack

* Python
* FastAPI
* Gemini 2.5 Flash
* Pydantic
* JSON Structured Outputs
* REST APIs

## Project Structure

```text
app/
├── core/
│   └── gemini_client.py
│
├── models/
│   ├── flutter_review_model.py
│   ├── bug_report_model.py
│   └── jira_ticket_model.py
│
├── services/
│   ├── flutter_review_service.py
│   ├── bug_report_service.py
│   └── jira_ticket_service.py
│
├── routes/
│   ├── flutter_review_route.py
│   ├── bug_report_route.py
│   └── jira_ticket_route.py
│
└── main.py
```

## Key Concepts Implemented

* Prompt Engineering
* Structured LLM Outputs
* Response Validation
* Enum-Based Validation
* FastAPI Routing
* Service Layer Architecture
* JSON Parsing
* AI-Powered Workflow Automation

## Future Enhancements

* Test Case Generator
* RAG (Retrieval Augmented Generation)
* Vector Database Integration
* LangChain
* LangGraph
* Agentic AI Workflows

## Learning Goal

To build production-oriented GenAI applications by combining software engineering principles with Large Language Models and AI-driven automation.
