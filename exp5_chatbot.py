"""
Experiment 5: Elementary Rule-Based Chatbot
Aim: Develop an elementary chatbot for student/customer interaction.
"""


def chatbot():
    print("Bot: Hello! Welcome to SPPU Student Helpdesk. Type 'bye' to exit.")

    rules = {
        "hello": "Hi there! How can I assist you today?",
        "hi": "Hello! Ask me about admissions, exams, syllabus, or fees.",
        "admission": "Admissions are open via the CAP portal. Visit cetcell.mahacet.org.",
        "exam": "TE End-Semester exams are scheduled in November/December.",
        "syllabus": "You can download the 2024 Pattern syllabus from unipune.ac.in.",
        "fees": "Fee details are available on your college ERP portal.",
        "contact": "You can reach the admin office at 020-25601000."
    }

    while True:
        user_input = input("You: ").lower().strip()
        if user_input == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        matched = False
        for keyword, response in rules.items():
            if keyword in user_input:
                print(f"Bot: {response}")
                matched = True
                break

        if not matched:
            print("Bot: Sorry, I didn't understand that. Try asking about 'admission', 'exam', 'syllabus', or 'fees'.")


if __name__ == "__main__":
    chatbot()
