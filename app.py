import streamlit as st
from components.editor import code_editor
from components.agent_builder import agent_builder
from templates.chatbot import Chatbot

def main():
    st.set_page_config(page_title="AI Agent Learning & Development App", layout="wide")
    
    st.sidebar.title("🔍 Navigation")
    page = st.sidebar.radio("Go to", ["Home", "AI Agent Playground", "Templates"])
    
    if page == "Home":
        st.title("🤖 AI Agent Learning & Development App")
        st.write("Learn, build, test, and deploy AI Agents effortlessly!")
    
    elif page == "AI Agent Playground":
        st.title("🛠️ AI Agent Playground")
        st.write("Drag & Drop Agent Builder and Python Code Editor")
        agent_builder()
        code_editor()
    
    elif page == "Templates":
        st.title("📜 Pre-built AI Agent Templates")
        chatbot = Chatbot()
        chatbot.run()

if __name__ == "__main__":
    main()

