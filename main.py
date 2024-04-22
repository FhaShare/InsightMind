##Author: Teenie Flood, Pipatporn Chaluthong, Fhaungfha Suvannakajorn 

import csv
import sys
import matplotlib.pyplot as plt 
import numpy as np 


def main_menu():
    print("Welcome to the DASS Self-report Questionnaire.")
    print("1. DASS-21")
    print("2. DASS-42")
    choice = input("Please choose the questionnaire version (1 or 2): ")
    if choice == '1':
        filename = "dass21questionnaires.csv"
        version = 'DASS-21'
    elif choice == '2':
        filename = "dass42questionnaires.csv"
        version = 'DASS-42'
    else:
        print("Invalid choice. Exiting.")
        sys.exit()
    return filename, version

def read_file(filename):
    """
    Reads questions from a CSV file and returns them as a list.
    """
    try:
        questions_list = []
        with open(filename, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                questions_list.append(row) 
        return questions_list
    except FileNotFoundError:
        print("Could not find " + filename + " file.")
        sys.exit()

def display_questions_and_collect_responses(questions_list):
    if not questions_list:
        print("The question list is empty.")
        sys.exit()
        
    responses = []
    print("Please rate how much each statement applied to you over the past week:")
    
    for i, row in enumerate(questions_list, start=1):
        print(f"{i}. {row[0]}")
        print("\t3 - Applied to me very much, or most of the time - ALMOST ALWAYS")
        print("\t2 - Applied to me to a considerable degree, or a good part of time - OFTEN")
        print("\t1 - Applied to me to some degree, or some of the time - SOMETIMES")
        print("\t0 - Did not apply to me at all - NEVER")
        while True:
            response = input("Answer: ")
            print(" ")
            if response.isdigit() and 0 <= int(response) <= 3:
                responses.append(int(response))
                break
            else:
                print("Invalid input. Please enter a number between 0 and 3.")
    return responses

def calculate_dass_scores(responses, version):
    if version == 'DASS-21':
        # Indices for DASS-21
        depression_indices = [3, 5, 10, 13, 16, 17, 21]
        anxiety_indices = [2, 4, 7, 9, 15, 19, 20]
        stress_indices = [1, 6, 8, 11, 12, 14, 18]

        depression_score = sum([responses[i-1] for i in depression_indices]) * 2 
        anxiety_score = sum([responses[i-1] for i in anxiety_indices]) * 2
        stress_score = sum([responses[i-1] for i in stress_indices]) * 2
    elif version == 'DASS-42':
        # Indices for DASS-42 provided by the template
        depression_indices = [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]
        anxiety_indices = [2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41]
        stress_indices = [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]

        depression_score = sum([responses[i-1] for i in depression_indices]) 
        anxiety_score = sum([responses[i-1] for i in anxiety_indices])
        stress_score = sum([responses[i-1] for i in stress_indices])

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

def print_scores(scores, version):
    depression_score, anxiety_score, stress_score = scores
    print("\nYour Scores:")
    print(f"Depression: {depression_score} ({interpret_scores(depression_score, 'Depression')})")
    print(f"Anxiety: {anxiety_score} ({interpret_scores(anxiety_score, 'Anxiety')})")
    print(f"Stress: {stress_score} ({interpret_scores(stress_score, 'Stress')})")

def make_radar_chart(name, depression_score, anxiety_score, stress_score):
    # Define markers and attribute labels for the triangular radar chart
    markers = [1, 2, 3, 4, 5]
    attribute_labels = ["Normal", "Mild", "Moderate", "Severe", "Extremely Severe"]
    labels = np.array(attribute_labels)
    
    # Define angles for the triangular radar chart
    angles = [0, np.pi/2, 2 * np.pi/2]
    
    # Normalize scores to range [0, 1]
    depression_norm = depression_score / max(markers)
    anxiety_norm = anxiety_score / max(markers)
    stress_norm = stress_score / max(markers)
    
    # Create triangular radar chart data
    stats = [depression_norm, anxiety_norm, stress_norm, depression_norm]  # Close the triangular shape
    
    # Plot the triangular radar chart
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, stats[:3], 'o-', linewidth=2)  # Plot the first three points
    ax.plot([angles[0], angles[2]], [stats[0], stats[2]], 'o-', linewidth=2)  # Connect the first and last points
    ax.fill(angles, stats[:3], alpha=0.25)  # Fill the area
    
    # Set axis labels and markers
    ax.set_thetagrids([angle * 180 / np.pi for angle in angles], ["Depression", "Anxiety", "Stress"])
    
    plt.yticks(markers, labels)
    
    # Set title and grid
    ax.set_title(name)
    ax.grid(True)
    
    # Save and show the plot
    fig.savefig("static/images/%s.png" % name)
    plt.show()


def main():
    filename, version = main_menu()  # Collects the filename and version based on user input
    questions_list = read_file(filename)  # Reads the questions based on the chosen version
    responses = display_questions_and_collect_responses(questions_list)
    scores = calculate_dass_scores(responses, version)
    print_scores(scores, version)
    depression_score, anxiety_score, stress_score = calculate_dass_scores(responses, version)
    make_radar_chart("Results",depression_score, anxiety_score, stress_score)
    
    print("\nPlease remember, this tool is not a diagnostic tool. If you are concerned about your mental health, please seek professional advice.")

if __name__ == "__main__":
    main()