import json
import os
import time

class QuizApp:
    def __init__(self):
        self.questions = {}  # { qid: {question: answer} }
        self.score = 0
        self.file_name = "quiz_paper.json"
    
    def add_question_answer(self, question, answer):
        if len(question.strip().split()) > 8:
            print("❌ Question is too long. Keep it under 8 words.\n")
            return
        
        qid = f">{time.time():.5f}<"
        self.questions[qid] = {question.strip(): answer.strip()}
        self.save_to_file()
        print("✅ Question & Answer added to Quiz paper!\n")

    def display_ids(self):
        if not self.load_data():
            return
        print("\n📋 Available Questions in Quiz Paper:\n")
        for idx, (qid, pair) in enumerate(self.questions.items(), start=1):
            question = list(pair.keys())[0]
            print(f"{idx}. 🆔 {qid} | ❓ Q: {question}")
        print()

    def remove_question(self, qid):
        if not self.load_data():
            return

        if qid in self.questions:
            del self.questions[qid]
            with open(self.file_name, 'w') as f:
                json.dump(self.questions, f, indent=4)
            print(f"✅ Question with ID {qid} removed successfully!\n")
        else:
            print(f"❌ Question ID {qid} not found in the database.\n")

    def save_to_file(self):
        existing_data = {}
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    existing_data = {}

        # Merge new questions with old
        existing_data.update(self.questions)

        with open(self.file_name, 'w') as f:
            json.dump(existing_data, f, indent=4)
        print("📁 Quiz data saved successfully!\n")
        self.questions = {}  # Clear temp buffer
    
    def load_data(self):
        if not os.path.exists(self.file_name):
            print("❗ No quiz file found. Add some questions first.\n")
            return False

        with open(self.file_name, 'r') as f:
            try:
                self.questions = json.load(f)
            except json.JSONDecodeError:
                print("⚠️ Quiz file is corrupted or empty.\n")
                return False
        return True

    def start_quiz(self):
        if not self.load_data() or not self.questions:
            print("❗ No questions available to start the quiz.\n")
            return

        print("\n🎯 Starting Your Quiz Now!\n")
        self.score = 0

        for idx, (qid, pair) in enumerate(self.questions.items(), start=1):
            for question, answer in pair.items():
                print(f"{idx}. ❓ {question}")
                user_answer = input("Your Answer: ").strip()
                if user_answer.lower() == answer.lower():
                    print("✅ Correct!\n")
                    self.score += 1
                else:
                    print(f"❌ Incorrect. Correct Answer: {answer}\n")

        print("🏁 Quiz Finished!")
        print(f"📊 Final Score: {self.score}/{len(self.questions)}\n")
