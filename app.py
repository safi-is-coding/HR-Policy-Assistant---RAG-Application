from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from rag_chain import ask_hr_bot

st.set_page_config(
    page_title="HR Policy Assistant",
    page_icon="🏢",
    layout="wide"
)

st.title("🏢 IIMA HR Policy Assistant")

st.markdown(
"""
Ask questions about:

- Leave Policy
- Notice Period
- Insurance
- Work From Home
- Travel Policy
- Employee Handbook
"""
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

query = st.chat_input(
    "Ask your HR question..."
)

if query:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":query
        }
    )

    with st.chat_message("user"):
        st.write(query)

    with st.spinner("Searching policies..."):

        answer = ask_hr_bot(query)

    with st.chat_message("assistant"):

        st.write(answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )