##Author: Teenie Flood, Pipatporn Chaluthong, Fhaungfha Suvannakajorn 

import csv
import sys

FILENAME = "dass21questionnaires.csv"

def read_file():
    """
    Reads questions from a CSV file and returns them as a list.
    """
    try:
        dass21_list = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                dass21_list.append(row) 
        return dass21_list
    except FileNotFoundError:
        print("Could not find " + FILENAME + " file.")
        sys.exit()

def display_questions_and_collect_responses(dass21_list):
    
    if len(dass21_list) == 0:
        print("There is no contact in the list.")
        
    responses = []
    print("Please rate how much each statement applied to you over the past week:")
    
    
    i = 1
    for row in dass21_list:
        print(str(i) + ". " + row[0])
        i += 1 
        print("\t3 - Applied to me very much, or most of the time - ALMOST ALWAYS")
        print("\t2 - Applied to me to a considerable degree, or a good part of time - OFTEN")
        print("\t1 - Applied to me to some degree, or some of the time - SOMETIMES")
        print("\t0 - Did not apply to me at all - NEVER")
        while True:
            response = input("Answer:")
            print(" ")
            if response.isdigit() and 0 <= int(response) <= 3:
                responses.append(int(response))
                break  # This should be inside the if condition
            else:
                print("Invalid input. Please enter a number between 0 and 3.")
            
    return responses

def calculate_dass_scores(responses):
    depression_indices = [2, 4, 9, 12, 15, 16, 20]
    anxiety_indices = [1, 3, 6, 8, 14, 18, 19]
    stress_indices = [0, 5, 7, 10, 11, 13, 17]

    depression_score = sum([responses[i] for i in depression_indices])
    anxiety_score = sum([responses[i] for i in anxiety_indices])
    stress_score = sum([responses[i] for i in stress_indices])

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
    
    dass21_list = read_file()
    
    responses = display_questions_and_collect_responses(dass21_list)
    
    depression_score, anxiety_score, stress_score = calculate_dass_scores(responses)
    
    print("\nYour Scores:")
    print(f"Depression: {depression_score} ({interpret_scores(depression_score, 'Depression')})")
    print(f"Anxiety: {anxiety_score} ({interpret_scores(anxiety_score, 'Anxiety')})")
    print(f"Stress: {stress_score} ({interpret_scores(stress_score, 'Stress')})")
    
    print("\nPlease remember, this tool is not a diagnostic tool. If you are concerned about your mental health, please seek professional advice.")

if __name__ == "__main__":
    main()