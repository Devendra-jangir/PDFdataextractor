from flask import Flask, request, jsonify
from flask_cors import CORS
import pdfplumber
import spacy
import re

app = Flask(__name__)
CORS(app)

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    """Extract raw text from PDF using pdfplumber."""
    text = ''
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + '\n'
    return text.strip()

def extract_details(text):
    """Use NLP to classify Name, Phone, Address, and Role."""
    details = {"name": None, "phone_number": None, "address": None, "role": None}
    
    doc = nlp(text)

    # Extract Name (Assuming Person Entity)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            details["name"] = ent.text
            break

    # Extract Phone using Regex
    phone_pattern = re.compile(r'\+?\d[\d\s\-\(\)]{9,}\d')
    phone_match = phone_pattern.search(text)
    if phone_match:
        details["phone_number"] = phone_match.group(0)

    # Extract Address (GPE, LOC)
    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC"]:
            details["address"] = ent.text
            break

    # Extract Role (Custom Approach - First "Role" keyword in text)
    role_pattern = re.compile(r'Role\s*:\s*(.+)')
    role_match = role_pattern.search(text)
    if role_match:
        details["role"] = role_match.group(1).strip()

    return details

@app.route('/extract', methods=['POST'])
def extract():
    """API endpoint to extract structured details from uploaded PDF."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    text = extract_text_from_pdf(file)
    details = extract_details(text)
    return jsonify(details)

if __name__ == '__main__':
    app.run(debug=True)
