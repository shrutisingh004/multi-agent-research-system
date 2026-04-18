import os
import streamlit as st
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    google_api_key=api_key
)

# Agent 1: Search Agent
def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )

# Agent 2: Reader Agent
def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )

# Writer Chain
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report based on the below topic.

Topic: {topic}
     
Research Gathered:
{research}
     
Structure the report as:
1. Introduction
2. Key Findings (minimum 3 well-explained points)
3. Conclusion
4. Sources (list all URLs found in the research)
     
Be detailed, factual and ensure the report is comprehensive and well-structured.""")
])

writer_chain = writer_prompt | llm | StrOutputParser()

# Critic Chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()
