##Author: Teenie Flood, Pipatporn Chaluthong, Fhaungfha Suvannakajorn 

import csv
import sys

def read_file(questions_filename):
    """
    Reads questions from a CSV file and returns them as a list.
    """
    try:
        dass21_list = []
        with open(questions_filename, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                dass21_list.append(row[0])  # Assuming each question is in the first column of each row
        return dass21_list
    except FileNotFoundError:
        print("Could not find " + questions_filename + " file.")
        sys.exit()

def display_questions_and_collect_responses(questions):
    responses = []
    print("Please rate how much each statement applied to you over the past week:")
    
    for question in questions:
        while True:
            response = input(question + " ")  
            if response.isdigit() and 0 <= int(response) <= 3:
                responses.append(int(response))
                break
            else:
                print("Invalid input. Please enter a number between 0 and 3.")
    return responses

def calculate_dass_scores(responses):
    depression_indices = [3, 5, 10, 13, 16, 17, 20]
    anxiety_indices = [2, 4, 7, 9, 15, 18, 21]
    stress_indices = [0, 6, 8, 11, 12, 14, 19]

    depression_score = sum([responses[i] for i in depression_indices]) * 2
    anxiety_score = sum([responses[i] for i in anxiety_indices]) * 2
    stress_score = sum([responses[i] for i in stress_indices]) * 2

    return depression_score, anxiety_score, stress_score

def interpret_scores(score, category):
    cutoffs = {
        'Depression': [9, 13, 20, 27],
        'Anxiety': [7, 9, 14, 19],
        'Stress': [14, 18, 25, 33]
    }
    labels = ['Normal', 'Mild', 'Moderate', 'Severe', 'Extremely Severe']
    
    for i, cutoff in enumerate(cutoffs[category]):
        if score <= cutoff:
            return labels[i]
    return labels[-1]

def main():
    print("Welcome to the DASS-21 Self-report Questionnaire.")
    questions_filename = "dass21questionnaires.csv"
    dass21_list = read_file(questions_filename)
    
    responses = display_questions_and_collect_responses(questions_filename)
    
    depression_score, anxiety_score, stress_score = calculate_dass_scores(responses)
    
    print("\nYour Scores:")
    print(f"Depression: {depression_score} ({interpret_scores(depression_score, 'Depression')})")
    print(f"Anxiety: {anxiety_score} ({interpret_scores(anxiety_score, 'Anxiety')})")
    print(f"Stress: {stress_score} ({interpret_scores(stress_score, 'Stress')})")
    
    print("\nPlease remember, this tool is not a diagnostic tool. If you are concerned about your mental health, please seek professional advice.")

if __name__ == "__main__":
    main()
