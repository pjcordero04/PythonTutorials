import random

quiz_data = {
    "Python Basics": [
        {
            "question": "What is the correct way to define a function in Python?",
            "choices": ["function myFunc():", "def myFunc():", "func myFunc()", "define myFunc()"],
            "answer": "def myFunc():"
        },
        {
            "question": "Which of these is a valid variable name?",
            "choices": ["2variable", "_variable", "var-name", "variable!"],
            "answer": "_variable"
        }
    ],
    "OOP Concepts": [
        {
            "question": "What is 'self' in a class method?",
            "choices": ["A keyword", "A reference to the instance", "The class name", "A static method"],
            "answer": "A reference to the instance"
        }
    ],
    "Word Problem Algebra": [
        {
            "question": "If 3x + 5 = 20, what is the value of x?",
            "choices": ["5", "10", "3", "15"],
            "answer": "5"
        },
        {
            "question": "A number increased by 7 is equal to 2 times the number. What is the number?",
            "choices": ["7", "14", "6", "13"],
            "answer": "7"
        },
        {
            "question": "Maria is twice as old as her sister. If the sum of their ages is 18, how old is Maria?",
            "choices": ["6", "12", "10", "9"],
            "answer": "12"
        }
    ],
    "Physics Concepts": [
        {
            "question": "What is Newton's First Law of Motion?",
            "choices": [
                "Force equals mass times acceleration.",
                "An object in motion stays in motion unless acted on by an external force.",
                "For every action, there is an equal and opposite reaction.",
                "The force between two objects is proportional to their masses."
            ],
            "answer": "An object in motion stays in motion unless acted on by an external force."
        },
        {
            "question": "What is the unit of force?",
            "choices": ["Joule", "Watt", "Newton", "Pascal"],
            "answer": "Newton"
        },
        {
            "question": "What happens to an object if the net force acting on it is zero?",
            "choices": [
                "It accelerates",
                "It moves in a circle",
                "Its motion does not change",
                "It gains energy"
            ],
            "answer": "Its motion does not change"
        }
    ]
}
highest_score = 0

def select_topic():
    print("Select a topic: ")
    topics = list(quiz_data.keys())
    for i, topic in enumerate(topics):
        print(f"{i+1}.{topic}")
    
    while True:
        try:
            choice = int(input("Enter the topic number: ")) - 1
            if 0<= choice <len(topics):
                return topics[choice]
            else:
                print("Invalid choice. Please enter again.\n")
        
        except ValueError:
            print("Please enter a valid number.\n")
    

def run_quiz(topic):
    questions = quiz_data[selected_topic]
    score = 0
    total = len(questions)

    print(f"\n--- Starting quiz on: {selected_topic} ---\n")

    for q in questions:
        print(q["question"])
        choices = q["choices"]
        random.shuffle(choices)

        for idx, choice in enumerate(choices):
            print(f"{idx+1}. {choice}")

        while True:  # Infinite loop
            try:
                user_input = int(input("Enter your answer (1-4): "))
                if 1 <= user_input <= 4:
                    user_choice = choices[user_input - 1]
                    if user_choice == q["answer"]:
                        print("✅ Correct!\n")
                        score += 1
                    else:
                        print(f"❌ Incorrect. The correct answer is: {q['answer']}\n")
                    break  # 💡 This stops the loop when input is valid
                else:
                    print("⚠️ Please enter a number between 1 and 4.\n")
            except ValueError:
                print("⚠️ Invalid input. Please enter a number.\n")

    print(f"Congratulations, your total score is {score}")

selected_topic = None
while selected_topic is None:
    selected_topic = select_topic()

run_quiz(selected_topic)
