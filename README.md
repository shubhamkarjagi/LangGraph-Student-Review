# 🎓 LangGraph Student Assignment Review System

An AI-powered Student Assignment Review System built using **LangGraph, LangChain and Groq API**. This project automatically summarizes student assignments, evaluates their content and generates constructive feedback using a Large Language Model (LLM).

## 📌 Project Overview

The LangGraph Student Assignment Review System helps automate the assignment review process through a sequential AI workflow.

Students provide an assignment topic and assignment text. The system processes the content through three stages:

1. **Summarization:** Generates a concise summary of the assignment.
2. **Evaluation:** Evaluates the assignment and provides a score with an explanation.
3. **Feedback Generation:** Provides constructive feedback and suggestions for improvement.

## 🎯 Project Objectives

- Automate basic student assignment reviews.
- Generate meaningful assignment summaries.
- Evaluate assignment content using an LLM.
- Provide personalized and constructive feedback.
- Understand and implement LangGraph workflows.

## 🛠️ Technologies Used

- Python
- LangGraph
- LangChain
- Groq API
- Large Language Models (LLMs)
- python-dotenv

## 🔄 Workflow Architecture

```text
       START
         |
         v
  Student Assignment Input
         |
         v
  Summarization Node
         |
         v
   Evaluation Node
         |
         v
   Feedback Node
         |
         v
     Final Output
         |
         v
        END
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shubhamkarjagi/LangGraph-Student-Review.git
```

### 2. Navigate to the Project Folder

```bash
cd LangGraph-Student-Review
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Required Libraries

```bash
python -m pip install langgraph langchain-groq python-dotenv
```

### 6. Configure Groq API Key

Create a `.env` file in the project directory.

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from [Groq Console](https://console.groq.com/keys).

**Important:** Never upload your `.env` file or share your API key publicly.

## ▶️ Run the Project

Execute the following command:

```bash
python main.py
```

The application will process the assignment and display:

- Assignment Summary
- Assignment Evaluation
- Student Feedback

## 📂 Project Structure

```text
LangGraph-Student-Review/
│
├── main.py
├── .gitignore
├── README.md
├── .env
└── .venv/
```

Note: `.env` and `.venv/` are excluded from GitHub using `.gitignore`.

## 🚀 Future Enhancements

- Develop a web-based user interface.
- Support PDF and DOCX assignment uploads.
- Store assignment review history.
- Generate downloadable evaluation reports.
- Add multiple evaluation criteria.

## 👨‍💻 Author

**Shubham Karjagi**

MCA Student | Data Science

GitHub: [@shubhamkarjagi](https://github.com/shubhamkarjagi)

---

⭐ If you find this project useful, consider giving the repository a star!