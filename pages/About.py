import streamlit as st

st.set_page_config(
    page_title="MOM Employment Pass Assistant",
    page_icon="🇸🇬"
)

st.title("About Us")

st.markdown("""
## Project Scope

The MOM Employment Pass Assistant is a Retrieval-Augmented Generation (RAG) chatbot designed to help users obtain information about Singapore Employment Pass requirements using official Ministry of Manpower (MOM) resources.

The application focuses on Employment Pass-related topics including eligibility requirements, COMPASS assessment criteria, family pass eligibility, application procedures, renewal requirements, and appeal processes.

---

## Project Objectives

The objectives of this project are:

1. Simplify access to Employment Pass information.
2. Reduce time spent searching across multiple MOM webpages.
3. Provide a conversational interface for answering Employment Pass questions.
4. Demonstrate the use of Retrieval-Augmented Generation (RAG) in a government information assistant.

---

## Data Source

The knowledge base is built using information obtained from:

Ministry of Manpower (MOM)
https://www.mom.gov.sg/passes-and-permits/employment-pass

The knowledge base includes:

- Employment Pass Overview
- Eligibility Requirements
- COMPASS Framework
- Family Passes
- Documents Required
- Application Process
- Renewal Process
- Appeals Process
- Cancellation Process
- Pass Replacement Procedures

---

## Features

### Employment Pass Q&A Assistant

Users can ask questions such as:

- What is an Employment Pass?
- What is COMPASS?
- How many points are required?
- Can I bring my spouse?
- How do I renew my Employment Pass?

The chatbot retrieves relevant information from the Employment Pass knowledge base before generating a response.
""")