import streamlit as st

st.set_page_config(
    page_title="MOM Employment Pass Assistant",
    page_icon="🇸🇬"
)

st.title("Methodology")

st.markdown("""
## System Architecture

This application uses a Retrieval-Augmented Generation (RAG) approach.

### Data Flow

1. Employment Pass information is stored in a local knowledge base.
2. User submits a question through the Streamlit interface.
3. Relevant content is retrieved from the knowledge base.
4. Retrieved information is sent to GPT-4o-mini.
5. GPT-4o-mini generates a response based on the retrieved information.
6. The response is displayed to the user.

---

## Use Case

### Employment Pass Information Assistant

The user requests Employment Pass-related information and receives responses generated from the Employment Pass knowledge base.

---

## Flowchart
""")

st.code("""
+----------------------+
| User Enters Question |
+----------+-----------+
           |
           v
+----------------------+
| Load Knowledge Base  |
| employment_pass.txt  |
+----------+-----------+
           |
           v
+----------------------+
| Retrieve Relevant    |
| Employment Pass      |
| Information          |
+----------+-----------+
           |
           v
+----------------------+
| Send Retrieved       |
| Context to GPT-4o    |
+----------+-----------+
           |
           v
+----------------------+
| Generate Response    |
+----------+-----------+
           |
           v
+----------------------+
| Display Answer       |
+----------------------+
""")

st.markdown("""
## Implementation Details

### Front-End
- Streamlit

### Large Language Model
- OpenAI GPT-4o-mini

### Knowledge Base
- employment_pass.txt

### Retrieval Method
The application retrieves relevant Employment Pass content by matching user question keywords with sections in the knowledge base before sending the context to GPT-4o-mini.

### Generation Method
GPT-4o-mini generates responses grounded on the retrieved Employment Pass information.
""")