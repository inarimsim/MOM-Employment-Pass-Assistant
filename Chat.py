import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="MOM Employment Pass Assistant"
)

# ----------------------------------
# Login
# ----------------------------------

USERNAME = "admin"
PASSWORD = "ep123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("MOM Employment Pass Assistant")
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if (
            username == USERNAME
            and password == PASSWORD
        ):
            st.session_state.logged_in = True
            st.rerun()

        else:
            st.error(
                "Invalid username or password."
            )

    st.stop()

# ----------------------------------
# OpenAI Configuration
# ----------------------------------

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    api_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)

# ----------------------------------
# Build Chroma Vector Database
# ----------------------------------

@st.cache_resource
def build_vector_db():

    loader = TextLoader(
        "knowledge_base/employment_pass.txt",
        encoding="utf-8"
    )

    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    chunks = text_splitter.split_documents(
        documents
    )

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=api_key
    )

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="employment_pass",
        persist_directory="./vector_db"
    )

    return vectordb


vectordb = build_vector_db()

retriever = vectordb.as_retriever(
    search_kwargs={"k": 5}
)

# ----------------------------------
# UI
# ----------------------------------

with st.sidebar:

    st.header("MOM Employment Pass Assistant")

    st.caption(
        "RAG-powered chatbot using official Ministry of Manpower (MOM) Employment Pass information."
    )

    st.markdown("---")

    st.markdown("""
    **Features**

    - Employment Pass Eligibility
    - COMPASS Framework
    - Family Passes
    - Application Process
    - Renewal & Appeals
    """)

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.markdown("---")

    st.caption(
        "This application was developed as part of an AI Bootcamp educational project."
    )

with st.expander(
    "⚠️ Important Notice",
    expanded=False
):
    st.markdown("""
**IMPORTANT NOTICE**

This web application is a prototype developed for educational purposes only.

The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

Furthermore, please be aware that the Large Language Model (LLM) may generate inaccurate or incorrect information.

You assume full responsibility for how you use any generated output.

Always consult with qualified professionals for accurate and personalised advice.
""")

st.info(
    "Ask Employment Pass questions based on official Ministry of Manpower (MOM) information from https://www.mom.gov.sg/passes-and-permits/employment-pass."
)

# ----------------------------------
# Chat History
# ----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ----------------------------------
# User Input
# ----------------------------------

question = st.chat_input(
    "Ask a question about Employment Pass"
)

if question:

    greetings = [
    "hi",
    "hello",
    "hey",
    "good morning",
    "good afternoon",
    "good evening",
    "hi!",
    "hello!",
    "hey!"
]

    if question.lower().strip() in greetings:

        answer = """
Hello! 👋

I am the MOM Employment Pass Assistant.

I can help with:

• Employment Pass eligibility
• COMPASS requirements
• Family passes
• Required documents
• Application procedures
• Renewals and appeals

Try asking:

• What is COMPASS?
• How do I qualify for an Employment Pass?
• Can I bring my spouse?
• How do I renew my Employment Pass?
"""

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.rerun()

    # ----------------------------------
    # Save User Message
    # ----------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # ----------------------------------
    # Build Conversation History
    # ----------------------------------

    conversation = ""

    for msg in st.session_state.messages:
        conversation += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    # ----------------------------------
    # Retrieve Relevant Chunks
    # ----------------------------------

    retrieved_docs = retriever.invoke(
        question
    )

    retrieved_context = "\n\n".join(
        [
            doc.page_content
            for doc in retrieved_docs
        ]
    )

    # Optional:
    # Uncomment if you want to show retrieved chunks
    #
    # with st.expander("Show Retrieved Context"):
    #     st.write(retrieved_context)

    # ----------------------------------
    # Prompt
    # ----------------------------------

    prompt = f"""
You are a MOM Employment Pass Assistant.

Use ONLY the retrieved information provided below.

IMPORTANT:

- Give concise and user-friendly answers.
- Summarise information instead of copying large sections.
- Use bullet points where appropriate.
- Keep answers under 120 words.
- Provide a short summary first.
- Only provide detailed explanations if the user asks for more information.
- Answer only using the retrieved information.
- Do not make up information.
- Never output HTML code.
- Convert all HTML lists into normal bullet points.
- Convert any HTML formatting into plain readable text.

If the answer cannot be found, reply exactly:

I could not find this information in the MOM Employment Pass knowledge base.

Conversation History:
{conversation}

Retrieved Information:
{retrieved_context}

Current Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = (
        response
        .choices[0]
        .message
        .content
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()