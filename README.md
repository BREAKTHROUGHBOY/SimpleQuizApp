
# 🧠 QuizApp - Terminal Based Question Bank & Quiz System

Welcome to **QuizApp**, a powerful and simple Python-based terminal quiz system designed for adding, managing, and performing quizzes right from the command line.

---

## 📁 Project Structure

```

📦 QuizApp/
├── learning\_python.py      # 🔧 Core logic: QuizApp class (add, remove, quiz, save/load)
├── quiz\_executor.py        # 🎮 Terminal UI for running the app
├── quiz\_paper.json         # 🗂️ Saved quiz data (auto-generated)
└── README.md               # 📘 Project documentation

````

---

## 🚀 Features

- ✅ Add questions and answers (max 8 words per question)
- 🗑️ Remove questions by unique ID
- 📋 Display all question IDs
- 🎯 Take a quiz with real-time scoring
- 💾 Auto-save questions to JSON
- 📂 Persistent data even after restarts

---

## ⚙️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/quizapp.git
cd quizapp
````

### 2. Run the Application

```bash
python quiz_executor.py
```

---

## 🧠 How It Works

* The `learning_python.py` file contains the `QuizApp` class that handles logic for question management, quiz execution, and file operations.
* The `quiz_executor.py` file provides a clean terminal-based menu for users to interact with the app.
* All data is saved inside a file named `quiz_paper.json` so you can load or update it anytime.

---

## 💡 Example

```text
📌 Main Menu:
1️⃣  Add a Question
2️⃣  Remove a Question
3️⃣  Start the Quiz
4️⃣  View All Question IDs
5️⃣  Quit
```

---

## 🔐 Data Format

Stored inside `quiz_paper.json`:

```json
{
  ">1718669514.85784<": {
    "What is AI?": "Artificial Intelligence"
  },
  ">1718669521.73489<": {
    "Capital of France?": "Paris"
  }
}
```

Each question is uniquely identified by a timestamp ID.

---

## 👑 Author

**King Trillionare** — Visionary of Next-Gen Humanity | Code, Systems & AI for a Future Beyond Boundaries.

---

## 📜 License

This project is licensed under the **MIT License** — you are free to use, modify, and share it!

---

## 🌟 What's Next?

* 🔄 Shuffle/randomize questions
* ⏱️ Add time limits per question
* 🧪 Difficulty tagging
* 🌐 Convert to Streamlit or Flask WebApp
* 🧠 Multi-user score tracking system

---

## ⭐️ Star This Repo

If this project helped you or inspired you, please consider giving it a ⭐ on [GitHub](https://github.com/BREAKTHROUGHBOY/quizapp)!

Let's build for the future — one line at a time.

```
