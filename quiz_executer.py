from learning_python import QuizApp  # Replace with actual filename

quiz_logic = QuizApp()

def main():
    print("\n✨ Welcome to the Ultimate Quiz Creator ✨\n")
    print("      +++<<<   🧠  QUIZ APP  🧠   >>>+++\n")

    while True:
        print("📌 Main Menu:")
        print("1️⃣  Add a Question")
        print("2️⃣  Remove a Question")
        print("3️⃣  Start the Quiz")
        print("4️⃣  View All Question IDs")
        print("5️⃣  Quit\n")

        choice = input("👉 Enter your choice (1-5): ").strip()

        if choice == "1":
            question = input("📝 Enter Question: ")
            answer = input("✅ Enter Answer: ")
            quiz_logic.add_question_answer(question, answer)

        elif choice == "2":
            quiz_logic.display_ids()
            qid = input("❌ Enter the Question ID to remove: ").strip()
            quiz_logic.remove_question(qid)

        elif choice == "3":
            quiz_logic.start_quiz()

        elif choice == "4":
            quiz_logic.display_ids()

        elif choice == "5":
            print("\n👋 Thanks for using the Quiz App. Keep learning, King!\n")
            break

        else:
            print("⚠️ Invalid option. Please choose from 1 to 5.\n")
        print("-" * 50)

if __name__ == "__main__":
    main()
