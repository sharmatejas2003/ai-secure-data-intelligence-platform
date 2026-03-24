# AI Secure Data Intelligence Platform

A powerful security analysis platform that scans logs and text data to detect sensitive information, identify vulnerabilities, and generate intelligent insights.

---

## Overview
The **AI Secure Data Intelligence Platform** is designed as a real-world security layer that acts like:

- Data Scanner  
- Log Analyzer  
- Risk Engine  
- Insight Generator  

It helps developers and security teams detect **data leaks, misconfigurations, and security threats** early.

---

## Key Capabilities

### Smart Detection Engine
Detects sensitive data such as:
- Emails  
- API Keys  
- Passwords  
- IP Addresses  

---

### Security Risk Detection
Identifies:
- Exposed credentials  
- Stack trace leaks  
- Debug information exposure  
- Brute-force login attempts  
- Suspicious IP activity  

---

### AI-like Insights Engine
Generates human-readable insights like:
- “Sensitive credentials exposed in logs”
- “Multiple failed login attempts detected”
- “Internal system details leaked via stack trace”

---

### Risk Evaluation System
- Calculates **risk score**
- Assigns **risk levels**:
  - Low  
  - Medium  
  - High  
  - Critical  

---

### Data Masking
Automatically masks sensitive data:
- `password=****`
- `api_key=****`

---

## Multi-Input Support

The system supports:
- Text input  
- Log files (`.log`, `.txt`)  
- Chat-style input  
- SQL queries  

---

## Architecture Flow
Input → Parser → Detection Engine → Log Analyzer → Risk Engine → Policy Engine → Insights → Response



---

## Tech Stack

| Layer | Technology |
|------|----------|
| Backend | FastAPI (Python) |
| Frontend | HTML, CSS, JavaScript |
| API Testing | Swagger UI / Postman |

---

## Project Structure
AI_SECURE_PLATFORM/
│
├── backend/
│ ├── routes/
│ ├── services/
│ ├── models/
│ └── main.py
│
├── frontend/
│ ├── index.html
│ ├── script.js
│ └── style.css
│
├── sample_logs/
├── requirements.txt
└── README.md

---

---

## ⚙️ Setup & Run

### 1 Install Dependencies
pip install -r requirements.txt

** 2 Run Backend Server**
cd backend
uvicorn main:app --reload


** 3 Open API Docs**
http://127.0.0.1:8000/docs


**How to Test**
1. -- Manual Input
Use /analyze endpoint:

2. -- Select input_type
Provide text/log input

3. --File Upload
Use /upload endpoint:

Upload .log or .txt file
Example Use Case

Input:  email=admin@gmail.com password=admin123 api_key=sk-xyz ERROR failed login 192.168.1.1


**Output:**
1>. Sensitive data detected 
2>. Risk score calculated 
3>. Insights generated 
4>. Data masked 


**Use Cases**
i. Application log monitoring
ii. Security audits
iii. Debugging sensitive leaks
iv. Pre-deployment security checks

**Future Enhancements**
i. Real AI/LLM integration
ii. Real-time log streaming
iii. Dashboard with charts & analytics
iv.  Cross-log correlation analysis

**Author**
Tejas Sharma
Email: tejasoffical786@gmail.com
