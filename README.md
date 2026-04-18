# Multi-Agent AI Research System

An end-to-end multi-agent system that automates research workflows by combining real-time web search, content extraction, and LLM-based report generation.

The system uses LangChain to orchestrate multiple specialized agents that collaboratively retrieve, process, and synthesize information into structured outputs.

---

## Overview

This project implements a modular multi-agent architecture where each agent is responsible for a specific stage in the research pipeline:

- `Search Agent`: Retrieves relevant web results using DuckDuckGo  
- `Reader Agent`: Extracts and cleans content from web pages  
- `Writer Agent`: Generates structured research reports  
- `Critic Agent`: Evaluates and refines the generated output  

Agents communicate through a shared state, enabling a scalable and extensible workflow.

---

## Tech Stack

- LangChain – Agent orchestration  
- DuckDuckGo (DDGS) – Web search  
- BeautifulSoup and Requests – Web scraping  
- Google Gemini API – Language model for generation and evaluation  
- Streamlit – User interface  

---

## Project Architecture
```bash
multi-agent-research-system/
│
├── app.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## System Architecture

User Query  
→ Search Agent  
→ Reader Agent  
→ Writer Agent  
→ Critic Agent  
→ Final Output  

---

## Features

- Multi-agent architecture for task decomposition  
- Real-time information retrieval using DuckDuckGo  
- Automated report generation using LLMs  
- Modular pipeline design for extensibility  
- Interactive Streamlit interface  

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/shrutisingh004/multi-agent-research-system.git
cd multi-agent-research-system
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Configure environment variables
Create a .env file:
```bash
GOOGLE_API_KEY=your_api_key_here
```
### 4. Run the application
```bash
streamlit run app.py
```

---

## Example Use Case

Input:
```bash
Latest advancements in artificial intelligence
```
Output:

- Aggregated insights from multiple sources
- Structured research summary
- Evaluated and refined response

---

## Key Highlights

- Processes multiple web sources per query
- Automates end-to-end research workflow
- Demonstrates agent-based system design
- Combines retrieval and reasoning in a unified pipeline

---

## Limitations

- Dependent on availability and quality of web sources
- LLM responses may vary based on prompt design
- Scraping may fail on certain websites

---

## Future Work

- Add result ranking and filtering mechanisms
- Introduce caching to reduce redundant API calls
- Optimize pipeline latency and parallel execution
- Enhance evaluation metrics for output quality
