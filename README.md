# 📄 PDF Resume Auto-Fill System  
Automatically extracts Name, Phone Number, Address, and Role from a PDF resume and auto-fills form fields using AI.  

---

## 🛠️ Features  
✔ **PDF Parsing**: Extracts text using `pdfplumber`.  
✔ **AI-Powered Extraction**: Uses `spaCy` for entity recognition (Name, Address, Phone).  
✔ **Frontend Auto-Fill**: React form auto-fills after PDF upload.  
✔ **Backend API**: Flask API handles file processing & AI extraction.  

---

## 📁 Project Structure  
pdf-data-extractor/ ├── backend/ # Flask backend │ ├── app.py # Main API file │ ├── requirements.txt # Backend dependencies │ ├── model/ # AI models (if needed) │ ├── ner_model.py # Custom AI models (optional) ├── frontend/ # React frontend │ ├── src/ │ │ ├── components/ │ │ │ ├── PdfUploader.js # PDF Upload Component │ │ ├── App.js # Main App Component │ │ ├── index.js # React Entry Point │ ├── package.json # Frontend dependencies └── README.md # Documentation



---

## Setup Instructions  

### 1️⃣ Backend Setup (Flask API)  
#### 📌 Step 1: Install Python & Create Virtual Environment  
cd backend
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate (Mac/Linux)
venv\Scripts\activate  # Activate (Windows)

📌 Step 2: Install Dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm
📌 Step 3: Run Backend Server
python app.py
✔ Runs Flask API on http://localhost:5000

2️⃣ Frontend Setup (React App)
📌 Step 1: Install Node.js & Create React App
cd frontend
npx create-react-app .
npm install axios

📌 Step 2: Start React App
npm start
✔ Runs React App on http://localhost:3000

📝 How the System Works
✅ Step 1: Upload any PDF Resume (e.g., resume.pdf).
✅ Step 2: The Flask API extracts text from the PDF.
✅ Step 3: AI-powered NLP model (spaCy) extracts Name, Phone, Address, Role.
✅ Step 4: The frontend automatically fills in the extracted details into form fields.

🔧 Technologies Used
Backend: Flask, Python, pdfplumber, spaCy (AI NLP)
Frontend: React, Axios
API Communication: Flask API with CORS
📜 API Endpoints
Endpoint	Method	Description
/extract	POST	Upload PDF & Extract Details
✔ Request Format (Multipart Form-Data):


Edit
{
  "file": "resume.pdf"
}

✔ Response Format:

{
  "name": "John Doe",
  "phone_number": "+1 (620) 130-7224",
  "address": "447 Sutter St 3rd Floor, San Francisco, CA 94108",
  "role": "Software Developer"
}
💡 Future Enhancements
🔥 Deploy Backend: Flask API on Heroku/Render.
🚀 Deploy Frontend: React app on Vercel/Netlify.
🤖 Improve AI: Use Hugging Face Transformers for better extraction.

