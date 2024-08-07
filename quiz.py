def display_question(question, options):
    print("--------------------------------------------------------")
    print(question)
    for option in options:
        print(option)

def get_user_input():
    return input("Enter your answer: ").upper()

def check_answer(user_input, correct_answer):
    if user_input == correct_answer:
        print("Correct Answer!! \n")
        return True
    else:
        print("Incorrect Answer!!")
        print(f"Correct answer: {correct_answer} \n")
        return False

def main():
    questions = [
        "What is the smallest country in the world by land area?",
        "Who developed the theory of general relativity?",
        "What is the main component of the Sun?",
        "What is the longest river in the world?",
        "Which is the hardest known natural material?"
    ]
    
    options = [
        ("A. Monaco", "B. Vatican City", "C. India", "D. China"),
        ("A. Isaac Newton", "B. Nikola Tesla", "C. Albert Einstein", "D. J. Robert Oppenheimer"),
        ("A. Oxygen", "B. Helium", "C. Carbon", "D. Hydrogen"),
        ("A. Amazon River", "B. Nile River", "C. Ganga River", "D. Yamuna River"),
        ("A. Gold", "B. Diamond", "C. Ruby", "D. Silver")
    ]
    
    solutions = ["B", "C", "D", "B", "B"]

    user_inputs = []
    score = 0

    for qn in range(len(questions)):
        display_question(questions[qn], options[qn])
        user_input = get_user_input()
        user_inputs.append(user_input)
        if check_answer(user_input, solutions[qn]):
            score += 1

    print("\n--------------------------------------------------------")
    print(f"Your score is {score}/{len(questions)}")

if __name__ == "__main__":
    main()
