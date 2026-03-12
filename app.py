import streamlit as st
import json
from transformers import pipeline

# Load AI model
generator = pipeline("text2text-generation", model="google/flan-t5-small")

# Load patient data
with open("patients.json") as f:
    data = json.load(f)

patients = data["patients"]

st.title("🧠 Patient Data AI Assistant")

# Patient dropdown
patient_ids = [p["id"] for p in patients]

selected_id = st.selectbox("Select Patient ID", patient_ids)

# Get selected patient
patient = next(p for p in patients if p["id"] == selected_id)

st.subheader("Patient Details")

st.write("Name:", patient["name"])
st.write("Age:", patient["age"])
st.write("Condition:", patient["condition"])
st.write("Medication:", patient["medication"])

st.subheader("Ask AI")

question = st.text_input("Ask medical question")

if st.button("Ask AI"):

    prompt = f"""
    Patient details:
    Name: {patient['name']}
    Age: {patient['age']}
    Condition: {patient['condition']}
    Medication: {patient['medication']}

    Question: {question}

    Answer in 3 steps.
    """

    response = generator(prompt, max_length=120)

    st.write("### AI Recommendation")
    st.write(response[0]["generated_text"])
