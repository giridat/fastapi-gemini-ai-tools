# AI QA Copilot

AI QA Copilot is an AI-powered bug analysis and workflow automation platform designed to streamline software quality assurance processes. The application leverages Large Language Models (LLMs), workflow orchestration, and Retrieval-Augmented Generation (RAG) principles to assist engineering teams in bug triaging, classification, severity assessment, and knowledge retrieval.

## Features

### Current Features

* Bug Management CRUD APIs
* FastAPI Backend
* SQLite Persistence Layer
* SQLAlchemy ORM
* Workflow-Based Architecture
* AI-Powered Issue Classification
* AI-Powered Severity Assessment
* AI-Generated Jira Ticket Drafts
* Planner Agent for Dynamic Workflow Execution

### In Progress

* Retrieval-Augmented Generation (RAG)
* ChromaDB Vector Store Integration
* Similar Bug Search
* Historical Bug Knowledge Base
* Root Cause Retrieval
* Embedding-Based Semantic Search

## Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite

### AI & LLM

* Google Gemini
* LangChain

### Vector Database

* ChromaDB (Planned)

## Architecture

Bug Report

↓

Planner Agent

↓

Classification Agent

↓

Severity Agent

↓

Jira Ticket Generation

↓

Workflow Response

Future Architecture:

SQLite

↓

Embedding Pipeline

↓

ChromaDB

↓

Retrieval Service

↓

Workflow Context

## Project Goals

The long-term vision is to build a production-ready AI QA Intelligence Platform capable of:

* Automated bug triaging
* Historical issue retrieval
* Root cause recommendations
* Test case generation
* Jira integration
* Knowledge base search
* AI-assisted software quality workflows

## Roadmap

### Phase 1

* CRUD APIs
* Database Layer
* Workflow Engine

### Phase 2

* ChromaDB Integration
* Embedding Generation
* Similar Bug Search

### Phase 3

* Jira Integration
* Frontend Dashboard
* Knowledge Base Management

### Phase 4

* Multi-Agent Workflow System
* Root Cause Analysis
* AI Test Case Generation
* Production Deployment
