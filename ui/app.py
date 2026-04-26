import streamlit as st
import requests
import os

# Set backend URL
raw_host = os.getenv("BACKEND_URL", "backend:8000")
backend_url = f"http://{raw_host}" if not raw_host.startswith("http") else raw_host

st.set_page_config(page_title="AI Assistant", page_icon="🤖")
st.title("Personal AI Assistant")
st.caption("Powered by Llama 3.2 + LangChain — asks the web, does math, checks weather")

# ── Session state ─────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Render chat history ───────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Chat input ────────────────────────────────────────────
if prompt := st.chat_input("Ask me anything — weather, math, news..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.get(f"{backend_url}/ask_agent?query={prompt}")
                data = response.json()
                reply = data["answer"]
            except Exception as e:
                reply = f"Sorry, I ran into an error: {e}"
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
