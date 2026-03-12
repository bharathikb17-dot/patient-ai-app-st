Patient Data AI Assistant

A simple AI-powered healthcare application that reads patient information from a JSON file and provides AI-generated recommendations based on patient conditions.

This project demonstrates how to build a Python + AI + Streamlit application that integrates patient data with a lightweight AI model.

🚀 Features

Select a Patient ID from a dropdown

Display patient details

Ask AI-based medical questions

Get AI recommendations in 3 steps

Works without external API keys

Simple Streamlit web interface

🧰 Tech Stack

Python

Streamlit

Transformers (Hugging Face)

Flan-T5 AI Model

JSON for patient data

📂 Project Structure
patient-ai-app
│
├── app.py              # Main Streamlit application
├── patients.json       # Patient dataset
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
📊 Sample Patient Data

Example structure inside patients.json:

{
  "patients": [
    {
      "id": "P001",
      "name": "John Doe",
      "age": 45,
      "condition": "Diabetes",
      "medication": "Metformin"
    },
    {
      "id": "P002",
      "name": "Jane Smith",
      "age": 50,
      "condition": "Hypertension",
      "medication": "Amlodipine"
    }
  ]
}
⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/patient-ai-app.git
cd patient-ai-app

Install dependencies:

pip install -r requirements.txt
▶️ Run the Application

Start the Streamlit app:

streamlit run app.py

Open in browser:

http://localhost:8501
💬 Example AI Question

You can ask questions such as:

Patient has diabetes. What lifestyle changes are recommended?

The AI will generate step-by-step suggestions based on the patient data.

⚠️ Note

This application is intended only for learning and demonstration purposes.
It does not provide real medical advice.

🌟 Future Improvements

Patient search functionality

Patient analytics dashboard

Risk prediction using ML

Integration with healthcare datasets

Secure database storage

📜 License

This project is open-source and available for educational use.

👨‍💻 Author

Developed as a Python + AI learning project demonstrating integration of patient data with AI-powered insights.
