import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
from knowledge_base import build_knowledge_base, search_knowledge_base

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
kb = build_knowledge_base(".")

st.set_page_config(page_title="PulseCompanion", page_icon="❤️")
st.title("❤️ PulseCompanion")
st.subheader("AI-Powered Heart Rate Support")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.started = False

if not st.session_state.started:
    heart_rate = st.number_input("Enter your heart rate (BPM):", min_value=-500, max_value=500, value=80)
    
    if st.button("Check My Heart Rate"):
        if heart_rate <= 0:
            st.error("❌ Invalid value! Heart rate cannot be zero or negative.")
        elif heart_rate < 30:
            st.error("❌ Impossible value! No human heart beats below 30 BPM.")
        elif heart_rate > 300:
            st.error("❌ Impossible value! No human heart beats above 300 BPM.")
        elif heart_rate > 150:
            st.error("🚨 EMERGENCY! Heart rate above 150 BPM is extremely dangerous. Call emergency services immediately!")
        elif heart_rate > 100:
            st.warning(f"⚠️ Your heart rate is {heart_rate} BPM - higher than normal")
            st.session_state.started = True
            st.session_state.heart_rate = heart_rate
            st.session_state.condition = "high"
            initial_message = f"We noticed your heart rate is elevated at {heart_rate} BPM. Are you exercising, or how are you feeling right now?"
            st.session_state.messages.append({"role": "assistant", "content": initial_message})
            st.rerun()
        elif heart_rate < 40:
            st.error("🚨 EMERGENCY! Critically low heart rate! Call emergency services immediately!")
        elif heart_rate < 60:
            st.warning(f"⚠️ Your heart rate is {heart_rate} BPM - lower than normal (Bradycardia).")
            st.info("💡 Please rest and consult a doctor. If you feel dizzy or faint, call emergency services.")
            st.session_state.started = True
            st.session_state.heart_rate = heart_rate
            st.session_state.condition = "low"
            initial_message = f"We noticed your heart rate is low at {heart_rate} BPM. Are you feeling dizzy, tired, or experiencing any discomfort?"
            st.session_state.messages.append({"role": "assistant", "content": initial_message})
            st.rerun()
        else:
            st.success(f"✅ Your heart rate is {heart_rate} BPM - normal range. Keep it up!")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.started:
    prompt = st.chat_input("Type your response...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            kb_results = search_knowledge_base(prompt, kb)
            kb_context = ""
            if kb_results:
                kb_context = "\n\nRelevant information from Saudi AI policies:\n"
                for r in kb_results:
                    kb_context += f"- {r['excerpt'][:300]}\n"

            condition = st.session_state.get("condition", "high")
            if condition == "low":
                system_prompt = """You are PulseCompanion, a caring AI health assistant. 
                The user has a low heart rate (Bradycardia). 
                Ask about symptoms like dizziness, fatigue, or fainting.
                Provide immediate advice: rest, avoid sudden movements.
                If symptoms are severe, strongly recommend calling emergency services or visiting a doctor immediately.
                Be calm, caring and concise."""
            else:
                system_prompt = """You are PulseCompanion, a caring AI health assistant aligned with Saudi Arabia's AI Readiness framework. 
                The user has an elevated heart rate. Understand if it is exercise or stress, 
                and provide breathing exercises, emotional support, or recommend a doctor."""

            full_prompt = system_prompt + kb_context + "\n\nConversation:\n"
            for m in st.session_state.messages:
                full_prompt += f"{m['role']}: {m['content']}\n"

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=full_prompt
            )
            assistant_message = response.text
            st.markdown(assistant_message)
            st.session_state.messages.append({"role": "assistant", "content": assistant_message})