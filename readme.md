## AI Secure Data Intelligence Platform 
A lightweight security analysis tool that scans logs and text data to detect sensitive information, identify risks, and generate actionable insights.

---
#### What is this?
This project is built to simulate a real-world security analysis system.
-It takes logs or text input and:
-Detects sensitive data (like passwords, API keys, emails)
-Identifies security risks (like exposed credentials or error leaks)
-Assigns a risk score
-Generates meaningful insights for developers or security teams

---

In real systems, logs often accidentally contain sensitive information.
This tool helps in:
i). Detecting data leaks early
ii). Identifying vulnerabilities
iii). Improving application security

---

### Key Features
1>. Smart Detection :-
Emails
Passwords
API Keys
IP Addresses

2>. Security Analysis :-
Credential exposure
Stack trace leaks
Brute-force login attempts

3>. Risk Evaluation :-
Risk scoring system with level count
Risk levels: Low/Medium/High

### Insight Generation
Human-readable security warnings
Clear explanation of risks

### Data Masking
Sensitive data is automatically hidden in output

---

## How it Works
Input → Parsing → Detection → Log Analysis → Risk Engine → Insights → Output

---

## Tech Stack
Backend :FastAPI with Python
Frontend: HTML, CSS, JavaScript
API Testing: Swagger UI / Postman

---

## Project Structure

AI_SECURE_PLATFORM/
│
├── backend/        
├── frontend/       
├── sample_logs/    
├── requirements.txt
└── README.md

---


### Dependencies Required ->
1.Install dependencies
[pip install -r requirements.txt]

2.Run the backend
cd backend
uvicorn main:app --reload

3.Open API Docs
http://127.0.0.1:8000/docs

---


## Use Cases :-
-Application log monitoring
-Security audits
-Debugging sensitive data leaks
-Pre-deployment checks


## Future Improvements :-
-Real AI integration like LLMs to get deeper insights
-Advanced anomaly detection
-Real-time log streaming
-Better UI dashboard

---

## Author
Tejas Sharma
E-mail : tejassharma939@gmail.com