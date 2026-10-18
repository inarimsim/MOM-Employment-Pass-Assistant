import streamlit as st

st.set_page_config(
    page_title="MOM Employment Pass Assistant"
)

st.title("Methodology")

st.markdown("""
# System Architecture

The MOM Employment Pass Assistant uses a Retrieval-Augmented Generation (RAG) architecture with a Chroma Vector Database to improve the relevance and accuracy of responses.

---

## Knowledge Base Initialisation (One-Time Process After Login)

When the application starts:

1. The Employment Pass knowledge base is loaded from `employment_pass.txt`.
2. The document is split into smaller text chunks.
3. OpenAI Embeddings are generated for each chunk.
4. The embeddings are stored in a Chroma Vector Database.
5. The vector database is cached and reused for future queries.

This process occurs only once during application initialisation.

## Knowledge Base Initialisation Flowchart
""")

st.code("""
    Successful Login
            ↓
 Employment Pass Document
            ↓
      Load Document
            ↓
    Split Into Chunks
            ↓
    Generate Embeddings
            ↓
  Chroma Vector Database
            ↓
      Ready for Use

""")

st.markdown("""
---

## Question Answering Workflow

When a user submits a question:

1. The user's question is received through the Streamlit interface.
2. Previous conversation history is retained to provide context.
3. The user's question is converted into an embedding.
4. The Chroma Vector Database performs semantic similarity search.
5. The most relevant document chunks are retrieved.
6. Retrieved content and conversation history are supplied to GPT-4o-mini.
7. GPT-4o-mini generates a response based on the retrieved context.
8. The final answer is displayed to the user.

## Question Answering Flowchart
""")

st.code("""
User Question
        ↓
Conversation History
        ↓
Generate Question Embedding
        ↓
Similarity Search
        ↓
Retrieve Relevant Chunks
        ↓
Send Context to GPT-4o-mini
        ↓
Generate Response
        ↓
Display Answer
""")

st.markdown("""

---

## Use Case

### Employment Pass Information Assistant

The user asks Employment Pass-related questions and receives responses generated using information retrieved from the Employment Pass knowledge base.

---

## Technologies Used

- Streamlit
- OpenAI GPT-4o-mini
- OpenAI Embeddings (`text-embedding-3-small`)
- Chroma Vector Database
- LangChain
- Retrieval-Augmented Generation (RAG)

---

## Implementation Details

The application uses a locally stored Employment Pass knowledge base derived from official Ministry of Manpower (MOM) resources.

During application initialisation, the Employment Pass document is loaded, split into smaller chunks and converted into vector embeddings using OpenAI Embeddings.

The generated embeddings are stored in a Chroma Vector Database and cached for reuse throughout the application's lifetime.

When a user submits a question, the Chroma Vector Database performs semantic similarity search to identify the most relevant document chunks.

The retrieved information, together with the conversation history, is provided to GPT-4o-mini to generate a concise and contextually relevant response.

This Retrieval-Augmented Generation (RAG) approach enables the application to retrieve relevant Employment Pass information before generating an answer.
""")