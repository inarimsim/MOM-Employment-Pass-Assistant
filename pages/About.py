import streamlit as st

st.set_page_config(
    page_title="MOM Employment Pass Assistant"
)

st.title("About Us")

st.markdown("""
## Project Overview

The MOM Employment Pass Assistant is a Retrieval-Augmented Generation (RAG) chatbot that helps users obtain information about Singapore Employment Pass (EP) requirements.

The application uses official Ministry of Manpower (MOM) Employment Pass information as its knowledge base and provides answers through a conversational chat interface.

---

## Project Scope

This project focuses on Employment Pass-related information, including:

- Employment Pass eligibility requirements
- COMPASS framework
- Family pass eligibility
- Required documents
- Application procedures
- Renewal requirements
- Appeals and cancellations

---

## Project Objectives

The objectives of this project are:

1. Simplify access to Employment Pass information.
2. Reduce time spent searching through multiple MOM webpages.
3. Provide a user-friendly chatbot interface.
4. Demonstrate the use of Retrieval-Augmented Generation (RAG).

---

## Data Source

Knowledge base source:

**Ministry of Manpower (MOM)**

https://www.mom.gov.sg/passes-and-permits/employment-pass

The knowledge base contains information about:

- EP Eligibility
- COMPASS Framework
- Family Passes
- Application Process
- Renewal Process
- Appeals Process
- Cancellation Process

---

## Features

### Employment Pass Q&A

Users can ask questions such as:

- What is COMPASS?
- How do I qualify for an Employment Pass?
- Can I bring my spouse to Singapore?
- How do I renew my Employment Pass?

### Conversational Memory

The chatbot maintains conversation context and can answer follow-up questions.

### Login Protection

A simple hardcoded login is implemented to restrict access to authorised users.

### RAG-Based Document Retrieval

Relevant Employment Pass information is retrieved from the knowledge base before generating responses.

---

## Technologies Used

- Python
- Streamlit
- OpenAI GPT-4o-mini
- OpenAI Embeddings (text-embedding-3-small)
- LangChain
- Chroma Vector Database
- Retrieval-Augmented Generation (RAG)

---
""")

st.info(
    "This application was developed as part of an AI Bootcamp educational project."
)