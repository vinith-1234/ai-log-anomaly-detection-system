# AI-Based Log & Network Anomaly Detection System

An intelligent cybersecurity project that analyzes system and network logs from a given URL, detects anomalies using AI-based rules, and generates a security risk score with visual insights.

## 🚀 Features
- 🔗 Input logs via URL
- 📄 Displays fetched log content
- 🧠 Detects anomalies (errors, warnings, failed logins, critical events)
- 📊 Calculates risk score and risk level
- 🖥️ Professional dashboard UI
- ⚡ Fast backend using FastAPI

## 🏗️ Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python (FastAPI)
- Data Fetching: Requests
- AI Logic: Rule-based anomaly detection (extendable to ML)

## 📂 Project Structure
ai-log-anomaly-detection-system/
│
├── backend/
│ ├── main.py
│ ├── log_analyzer.py
│ └── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
└── README.md
## ⚙️ Setup Instructions

### 1️⃣ Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
2️⃣ Frontend:
Open frontend/index.html in browser
(or use Live Server in VS Code)
🌐 Test URLs
Use these sample log URLs:
https://raw.githubusercontent.com/logpai/loghub/master/Apache/Apache_2k.log
https://raw.githubusercontent.com/logpai/loghub/master/Linux/Linux_2k.log
https://raw.githubusercontent.com/logpai/loghub/master/HDFS/HDFS_2k.log
