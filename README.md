# 🎓 Student Performance Prediction System

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![AI Chatbot](https://img.shields.io/badge/AI-Chatbot-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

An **AI-powered educational analytics platform** that predicts student mathematics performance using **machine learning models** and provides **real-time learning support via an AI Tutor Chatbot**.

---

# 🚀 Live Demo

🔗 **Try the app here:**
👉 https://student-performance-predictor-4dvr.onrender.com/

---

# 📊 Project Overview

This system predicts a student's **mathematics score** based on key academic and demographic factors such as:

* Gender
* Race/Ethnicity
* Parental Education Level
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

Users can input these details through a **Flask-based web interface** and instantly receive predictions along with performance insights.

---

# 🧠 Key Features

* ⚡ **Real-Time Predictions** – Instant score prediction
* 📊 **Performance Classification** – Categorizes students into support levels
* 🎓 **Educational Insights** – Helps identify students needing assistance
* 🔧 **Modular ML Pipeline** – End-to-end ML workflow
* 🤖 **AI Tutor Chatbot** – Interactive learning assistant

---

# 🎓 Performance Classification

* 🟢 **≥ 60** → No Assistance Needed
* 🟡 **40–59** → Needs Support
* 🔴 **< 40** → Needs Significant Help

---

# 🤖 AI Tutor Chatbot

The system includes an **AI-powered chatbot** that helps students understand concepts and solve doubts.

### How it works:

1. User asks a question
2. Request sent to `/api/tutor`
3. Processed using **Groq LLM API**
4. Response displayed instantly

### Model Used:

```
llama-3.1-8b-instant
```

---

# 💻 Technology Stack

### Programming

* Python

### Machine Learning

* Scikit-learn
* XGBoost


### Data Processing

* Pandas
* NumPy

### Web

* Flask
* HTML, CSS, Jinja2

### AI Integration

* Groq API

---

# ⚙️ System Workflow

```
User Input
   ↓
Data Preprocessing
   ↓
ML Model Prediction
   ↓
Score Output
   ↓
Performance Classification
```

---

# 📈 Model Performance

| Metric          | Value    |
| --------------- | -------- |
| R² Score        | 0.88     |
| MAE             | 4.2      |
| RMSE            | 5.8      |
| Prediction Time | <0.1 sec |

---

# 📂 Project Structure

```
Student-Performance-Predictor
│
├── app.py
├── src/
│   ├── components/
│   └── pipeline/
├── artifacts/
├── notebook/
├── templates/
├── static/
├── logs/
├── requirements.txt
└── README.md
```

---

# 🛠 Installation

```bash
git clone https://github.com/Mohit01112/Student_Performance_Predictor.git
cd Student_Performance_Predictor
pip install -r requirements.txt
```

### Create `.env`

```
GROQ_API_KEY=your_api_key
```

### Run the app

```bash
python app.py
```

---

# 🚀 Future Improvements

* Docker deployment
* CI/CD pipeline
* Model monitoring
* Advanced dashboards

---

# 🌍 Project Impact

* Identifies students needing support
* Enables data-driven education decisions
* Supports early intervention strategies
* Provides interactive learning assistance

---

# 👨‍💻 Author

**Mohit Jadhav**

🔗 GitHub: https://github.com/Mohit01112
🔗 LinkedIn: https://www.linkedin.com/in/mohit-jadhav-49734427b/
