import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="MOM Employment Pass Assistant",
    page_icon="🇸🇬"
)

# ---------------------
# Login
# ---------------------

USERNAME = "admin"
PASSWORD = "ep123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("Login")

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
# Load OpenAI API Key
# ----------------------------------

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# ----------------------------------
# Load Knowledge Base
# ----------------------------------

with open(
    "knowledge_base/employment_pass.txt",
    "r",
    encoding="utf-8"
) as file:
    knowledge_base = file.read()

# ----------------------------------
# UI
# ----------------------------------

st.title("MOM Employment Pass Assistant")

if st.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

with st.expander("⚠️ Important Notice", expanded=False):
    st.markdown("""
**IMPORTANT NOTICE:**

This web application is a prototype developed for educational purposes only.

The information provided here is **NOT intended for real-world usage** and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

Furthermore, please be aware that the Large Language Model (LLM) may generate inaccurate or incorrect information.

You assume full responsibility for how you use any generated output.

Always consult with qualified professionals for accurate and personalised advice.
""")

st.write("""
Ask questions about:

- Employment Pass Eligibility
- COMPASS Framework
- Family Passes
- Application Process
- Renewal Process
- Appeals
""")

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

    # Greetings
    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
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
• Application, renewal and appeals

Try asking:

• What is COMPASS?
• How do I qualify for an EP?
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

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Build conversation history
    conversation = ""

    for msg in st.session_state.messages:
        conversation += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    # Prompt
    prompt = f"""
You are a MOM Employment Pass Assistant.

Use ONLY the Employment Pass knowledge base provided.

IMPORTANT:

- Give concise and user-friendly answers.
- Do not output HTML tags.
- Convert any HTML content into normal readable text.
- Summarise information instead of copying large sections.
- Use bullet points when helpful.
- Keep answers under 200 words unless the user asks for more detail.
- If the user asks a broad question, provide a short summary first.
- Answer based only on the Employment Pass knowledge base.
- Do not make up information.

If the answer cannot be found in the knowledge base, reply exactly:

I could not find this information in the MOM Employment Pass knowledge base.

Conversation History:
{conversation}

Knowledge Base:
{knowledge_base}

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

    answer = response.choices[0].message.content

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()