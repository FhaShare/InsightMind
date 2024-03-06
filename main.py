##Author: Teenie Flood, Marian Sankay, Pipatporn Chaluthong, Fhaungfha Suvannakajorn 

def phq9():
    """
    This 
    """
    print("Patient Health Questionnaire-9(PHQ-9)")
    print("How often have they been bothered by the following over the past 2 weeks?")

    # PHQ-9 questions
    questions = ["Little interest or pleasure in doing things?",
                 "Feeling down, depressed, or hopeless?",
                 "Trouble falling or staying asleep, or sleeping too much?",
                 "Feeling tired or having little energy?",
                 "Poor appetite or overeating?",
                 "Feeling bad about yourself - or that you are a failure or have let yourself or your family down?",
                 "Trouble concentrating on things, such as reading the newspaper or watching television?",
                 "Moving or speaking so slowly that other people could have noticed? Or so fidgety or restless that you have been moving a lot more than usual?",
                 "Thoughts that you would be better off dead, or thoughts of hurting yourself in some way?"]

    scores = []  # To store the scores of each question

    print("Please answer the following questions by entering the number corresponding to your response:")
    print("0: Not at all")
    print("1: Several days")
    print("2: More than half the days")
    print("3: Nearly every day")

    for question in questions:
        response = int(input(question + " "))
        if response in [0, 1, 2, 3]:
            scores.append(response)
        else:
            print("Invalid input. Please enter a number between 0 and 3.")

    total_score = sum(scores)

    print("\nYour PHQ-9 score is:", total_score)

    # Interpretation (This can vary; consult appropriate health care providers for a clinical interpretation)
    if total_score >= 20:
        print("Your score suggests severe depression.")
    elif total_score >= 15:
        print("Your score suggests moderately severe depression.")
    elif total_score >= 10:
        print("Your score suggests moderate depression.")
    elif total_score >= 5:
        print("Your score suggests mild depression.")
    else:
        print("Your score suggests minimal depression.")

    print("Please note that this tool is not a diagnostic tool. Consult a healthcare provider for a thorough assessment.")

if __name__ == "__main__":
    phq9()

