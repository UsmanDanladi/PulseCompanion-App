import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-flash-latest")

st.set_page_config(page_title="PulseCompanion", page_icon="❤️")
st.title("❤️ PulseCompanion")
st.subheader("AI-Powered Heart Rate Support")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.started = False

if not st.session_state.started:
    heart_rate = st.number_input("Enter your heart rate (BPM):", min_value=-500, max_value=500, value=80)
    
    if st.button("Check My Heart Rate"):
        if heart_rate <= 0:
            st.error("❌ Invalid value! A heart rate cannot be zero or negative. Please enter a real heart rate value.")
        elif heart_rate < 30:
            st.error("❌ Impossible value! No human heart beats below 30 BPM. Please enter a valid heart rate.")
        elif heart_rate > 300:
            st.error("❌ Impossible value! No human heart beats above 300 BPM. Please enter a valid heart rate.")
        elif heart_rate > 150:
            st.error("🚨 EMERGENCY! A heart rate above 150 BPM is extremely dangerous. Please call emergency services immediately!")
        elif heart_rate > 100:
            st.warning(f"⚠️ Your heart rate is {heart_rate} BPM - higher than normal")
            st.session_state.started = True
            st.session_state.heart_rate = heart_rate
            initial_message = f"We noticed your heart rate is elevated at {heart_rate} BPM. Are you exercising, or how are you feeling right now?"
            st.session_state.messages.append({"role": "assistant", "content": initial_message})
            st.rerun()
        elif heart_rate < 60:
            st.warning(f"⚠️ Your heart rate is {heart_rate} BPM - lower than normal (Bradycardia). Consider consulting a doctor.")
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
            system_prompt = "You are PulseCompanion, a caring AI health assistant. The user has an elevated heart rate. Understand if it is exercise or stress, and provide breathing exercises, emotional support, or recommend a doctor."
            full_prompt = system_prompt + "\n\nConversation:\n"
            for m in st.session_state.messages:
                full_prompt += f"{m['role']}: {m['content']}\n"
            response = model.generate_content(full_prompt)
            assistant_message = response.text
            st.markdown(assistant_message)
            st.session_state.messages.append({"role": "assistant", "content": assistant_message})