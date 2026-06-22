# AI Practice - Agentic QA Assistant

An AI-powered backend application built using FastAPI, Gemini, LangChain, and Python as part of my transition from Software Engineering to Generative AI and Agentic AI Application Development.

The project demonstrates how Large Language Models can be orchestrated through specialized agents to automate software defect analysis, bug triage, and Jira ticket generation.

---

## Features 

Current Features
- Planner Workflow
- Classification
- Severity Analysis
- Jira Generation

Upcoming Features
- RAG
- ChromaDB
- Historical Bug Retrieval
- Root Cause Analysis
- Test Case Generation
- Docker Deployment

### Flutter Code Review API

Analyzes Flutter code and provides:

* Code quality feedback
* Architecture recommendations
* Performance improvements
* Best practice suggestions
* Maintainability insights

---

### AI Bug Report Generator

Generates structured bug reports from issue descriptions.

Outputs:

* Summary
* Severity
* Priority
* Root Cause Analysis
* Steps to Reproduce

---

### AI Jira Ticket Generator

Automatically converts issue descriptions into Jira-ready tickets.

Outputs:

* Title
* Description
* Severity
* Priority
* Labels

---

### Agentic QA Workflow

A multi-agent workflow that automates software defect triage.

Workflow:

Issue Description
→ Planner Agent
→ Classification Agent
→ Severity Agent
→ Jira Agent
→ Structured Response

The Planner Agent dynamically determines which downstream agents should execute based on user intent.

Example:

Input:

"Application crashes after login but do not create a Jira ticket."

Planner Output:

```json
{
  "run_classification": true,
  "run_severity": true,
  "run_jira": false
}
```

This enables dynamic workflow orchestration instead of a fixed execution sequence.

---

## Agent Architecture

### Planner Agent

Determines which agents should execute.

Responsibilities:

* Analyze user intent
* Create execution plan
* Control workflow routing

### Classification Agent

Classifies the issue into:

* Module
* Issue Type

Example:

```json
{
  "module": "Authentication",
  "issue_type": "Crash"
}
```

### Severity Agent

Determines:

* Severity
* Priority

Example:

```json
{
  "severity": "Critical",
  "priority": "P1"
}
```

### Jira Agent

Generates:

* Jira Title
* Jira Description
* Labels

---

## Workflow State Management

The workflow maintains a shared state object that is updated by each agent.

Example:

```python
state = {
    "issue": issue,
    "plan": plan,
    "classification": None,
    "severity": None,
    "jira_ticket": None,
    "error": None
}
```

This approach is conceptually similar to state-driven orchestration used in modern agent frameworks such as LangGraph.

---

## Tech Stack

* Python
* FastAPI
* Gemini 2.5 Flash
* LangChain
* Pydantic
* REST APIs
* JSON Structured Outputs

---

## Key Concepts Implemented

### Generative AI

* Prompt Engineering
* Structured Outputs
* JSON Parsing
* LLM-Powered Automation

### Backend Engineering

* FastAPI Routing
* Request Validation
* Response Validation
* Service Layer Architecture
* Exception Handling

### Agentic AI

* Multi-Agent Workflows
* Planner Agent
* Workflow State Management
* Conditional Agent Execution
* AI-Driven Decision Making

### LangChain

* PromptTemplate
* ChatGoogleGenerativeAI
* LLM Abstractions
* Agent-Oriented Architecture

---

## Project Structure

```text
app/
├── agents/
│   ├── planner_agent.py
│   ├── classifier_agent.py
│   ├── severity_agent.py
│   └── jira_agent.py
│
├── core/
│   ├── gemini_client.py
│   └── langchain_llm.py
│
├── workflows/
│   └── bug_workflow.py
│
├── models/
│   ├── flutter_review_model.py
│   ├── bug_report_model.py
│   ├── jira_ticket_model.py
│   └── agent_workflow_model.py
│
├── routes/
│   ├── flutter_review_route.py
│   ├── bug_report_route.py
│   ├── jira_ticket_route.py
│   └── agentic_bug_route.py
│
└── main.py
```

---

## Future Enhancements

* Test Case Generation Agent
* Root Cause Analysis Agent
* RAG (Retrieval Augmented Generation)
* Vector Database Integration (Chroma / Pinecone)
* LangGraph Workflows
* Tool Calling
* Function Calling
* Human-in-the-Loop Validation
* GitHub and Jira Integrations

---

## Learning Objectives

This project was created to gain hands-on experience with:

* Generative AI Application Development
* Agentic AI Systems
* LangChain
* Workflow Orchestration
* Structured LLM Outputs
* AI-Powered Automation
* Production-Oriented Backend Design

The long-term goal is to evolve this project into a fully agentic software quality platform capable of analyzing defects, generating test cases, performing root cause analysis, and integrating directly with engineering workflows.
