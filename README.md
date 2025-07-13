1. Project Overview – Smart Assistant for Research Summarization
A lightweight AI-powered web app

Allows users to upload PDF documents

Automatically summarizes the uploaded content

Supports asking questions based on document context

Offers logic-driven challenge questions for interactive learning

Combines FastAPI (backend) with Streamlit (frontend)

2. Setup Instructions – Step by Step
📁 Step 1: Clone the GitHub repository

git clone https://github.com/<your-username>/smart-assistant.git
cd smart-assistant
🧱 Step 2: Create and activate a virtual environment
Windows:
python -m venv venv
venv\Scripts\activate
python3 -m venv venv
source venv/bin/activate
📦 Step 3: Install all required Python packages
If you have a requirements.txt:
pip install -r requirements.txt
Or install them manually:

Step 4: Run the backend server (FastAPI)

cd backend
uvicorn main:app --reload --port 7860
💻 Step 5: Launch the frontend interface (Streamlit)

cd frontend
streamlit run app.py 

Step 6: Open the app in your browser
Frontend: http://localhost:8501

Backend API Docs: http://127.0.0.1:7860/docs

🧠 3. Architecture & Workflow – How It Works
User uploads a PDF file from the frontend

Frontend sends the file to the backend FastAPI server

Backend extracts text using pdfplumber

Summarization model generates a short version of the content

Q&A model answers user questions from the text

Challenge questions are also generated

All outputs are displayed in the Streamlit UI
