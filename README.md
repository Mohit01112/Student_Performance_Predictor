

# 🎓 Student Performance Prediction System

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![AI Chatbot](https://img.shields.io/badge/AI-Chatbot-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

An **AI-powered educational analytics platform** that predicts student mathematics performance using **Machine Learning models and a scalable data science pipeline**.

The system also includes an **AI Tutor Chatbot** that helps students understand academic concepts interactively.

---

# 🚀 Live Demo

*(Add your deployed link here later)*

```
https://your-project-link.com
```

---

# 📊 Project Overview

The **Student Performance Prediction System** predicts a student's **mathematics score** based on academic and demographic factors.

### Input Factors

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

The system uses **machine learning models** to analyze these features and generate predictions.

A **Flask-based web application** allows users to enter student information and instantly receive predictions.

Additionally, the platform includes a **built-in AI Tutor chatbot** that helps students learn by answering questions and explaining concepts.

---

# 🧠 Key Features

### 📊 Student Score Prediction

Predicts mathematics scores using trained ML models.

### ⚡ Real-Time Predictions

Instant results through an interactive web interface.

### 🎓 Educational Insights

Helps identify students who may require academic support.

### 📈 Performance Classification

Students are categorized into:

* 🟢 **No Assistance Needed**
* 🟡 **Needs Support**
* 🔴 **Needs Significant Help**

### 🔧 Modular ML Pipeline

Includes:

* Data ingestion
* Data transformation
* Model training
* Prediction pipeline

### 🤖 AI Tutor Chatbot

Interactive chatbot that helps students learn.

Features:

* Floating chatbot interface
* Real-time AI responses
* Academic explanations
* Study assistance

---

# 🤖 AI Tutor Chatbot

The application includes an **AI Tutor Chatbot** that helps students understand topics such as:

* Mathematics concepts
* Data Science
* Machine Learning basics
* Academic questions

### How It Works

1️⃣ User sends a question through the chatbot
2️⃣ Request goes to backend API `/api/tutor`
3️⃣ Backend sends request to **Groq LLM API**
4️⃣ AI model generates response
5️⃣ Response appears in chatbot UI

### AI Model Used

```
llama-3.1-8b-instant
```

Powered by **Groq API**.

---

# 💻 Technology Stack

### Programming

* Python

### Machine Learning

* Scikit-learn
* XGBoost
* CatBoost
* Random Forest
* Gradient Boosting
* AdaBoost

### Data Processing

* Pandas
* NumPy

### Web Framework

* Flask

### Frontend

* HTML
* CSS
* Jinja2

### AI Chatbot

* Groq LLM API
* Llama 3.1 model

---

# 📸 Application Screenshots

*(Add screenshots of your project here)*

### Home Page

```
/screenshots/home.png
```

### Prediction Page

```
/screenshots/predict.png
```

### Result Page

```
/screenshots/result.png
```

### AI Chatbot

```
/screenshots/chatbot.png
```

---

# ⚙️ How the System Works

### 1️⃣ Data Collection

Student dataset includes:

* Demographic information
* Academic performance metrics

---

### 2️⃣ Data Preprocessing

Includes:

* Handling missing values
* Encoding categorical features
* Feature scaling

---

### 3️⃣ Model Training

Models tested:

* Random Forest Regressor
* Decision Tree Regressor
* Gradient Boosting Regressor
* Linear Regression
* XGBoost Regressor
* CatBoost Regressor
* AdaBoost Regressor

Best model selected using **R² score**.

---

### 4️⃣ Prediction Pipeline

Steps:

```
User Input
     ↓
Data Preprocessing
     ↓
Trained ML Model
     ↓
Math Score Prediction
     ↓
Performance Classification
```

---

### 5️⃣ AI Tutor Interaction

Students can ask questions to the chatbot and receive **real-time explanations**.

---

# 📈 Model Performance

| Metric              | Value     |
| ------------------- | --------- |
| R² Score            | 0.88      |
| Mean Absolute Error | 4.2       |
| RMSE                | 5.8       |
| Prediction Time     | < 0.1 sec |

---

# 📂 Project Structure

```
Student-Performance-Predictor
│
├── app.py
│
├── src
│   ├── components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   └── pipeline
│       └── predict_pipeline.py
│
├── artifacts
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── notebook
│   └── EDA.ipynb
│
├── templates
│
├── static
│
├── logs
│
├── requirements.txt
└── README.md
```

---

# 🛠 Installation

### Clone repository

```bash
git clone https://github.com/yourusername/student-performance-predictor.git
```

### Move into project

```bash
cd student-performance-predictor
```

### Install dependencies

```bash
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


```
http://localhost:5000
```

---

# 🚀 Future Improvements

* Deploy on cloud (AWS / Render / GCP)
* Docker containerization
* Model monitoring
* CI/CD pipeline
* Advanced student analytics dashboard

---

# 🌍 Project Impact

This system demonstrates how **AI and Data Science can improve education**.

Benefits include:

* Early detection of struggling students
* Data-driven educational decisions
* Academic support recommendations
* Personalized learning assistance

---

# 👨‍💻 Author

**Mohit Jadhav**

Aspiring **AI Engineer & Data Scientist**

GitHub
[https://github.com/Mohit01112](https://github.com/Mohit01112)

LinkedIn
[https://www.linkedin.com/in/mohit-jadhav-49734427b/](https://www.linkedin.com/in/mohit-jadhav-49734427b/)

