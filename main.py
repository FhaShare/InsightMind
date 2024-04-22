import csv
import sys
import matplotlib.pyplot as plt 
import numpy as np 

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
def get_stress_score(responses, version):
     if version == 'DASS-21':
        # Indices for DASS-21
     
        stress_indices = [1, 6, 8, 11, 12, 14, 18]

        stress_score = sum([responses[i-1] for i in stress_indices]) * 2
        return stress_score
     elif version == 'DASS-42':
        # Indices for DASS-42 provided by the template
     
        stress_indices = [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]
        stress_score = sum([responses[i-1] for i in stress_indices])
        return stress_score
    
def get_anxiety_score(responses, version):
    if version == 'DASS-21':
        # Indices for DASS-21
        
        anxiety_indices = [2, 4, 7, 9, 15, 19, 20]
       

        
        anxiety_score = sum([responses[i-1] for i in anxiety_indices]) * 2
        return anxiety_score
    elif version == 'DASS-42':
        # Indices for DASS-42 provided by the template
        
        anxiety_indices = [2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41]
        

         
        anxiety_score = sum([responses[i-1] for i in anxiety_indices])
        return anxiety_score
def get_depression_score(responses, version):
    if version == 'DASS-21':
        # Indices for DASS-21
        depression_indices = [3, 5, 10, 13, 16, 17, 21]
        

        depression_score = sum([responses[i-1] for i in depression_indices]) * 2 
        return depression_score
    elif version == 'DASS-42':
        # Indices for DASS-42 provided by the template
        depression_indices = [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]
       

        depression_score = sum([responses[i-1] for i in depression_indices]) 
        return depression_score

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
<<<<<<< Updated upstream

def main():
    print("Welcome to the DASS-21 Self-report Questionnaire.")
    questions_filename = "dass21questionnaires.csv"
    dass21_list = read_file(questions_filename)
    
    responses = display_questions_and_collect_responses(questions_filename)
    
    depression_score, anxiety_score, stress_score = calculate_dass_scores(responses)
    
=======
def make_radar_chart(depression_score, anxiety_score, stress_score):
    # Define markers and attribute labels for the triangular radar chart
    name= "results"
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
def print_scores(scores, version):
    depression_score, anxiety_score, stress_score = scores
>>>>>>> Stashed changes
    print("\nYour Scores:")
    print(f"Depression: {depression_score} ({interpret_scores(depression_score, 'Depression')})")
    print(f"Anxiety: {anxiety_score} ({interpret_scores(anxiety_score, 'Anxiety')})")
    print(f"Stress: {stress_score} ({interpret_scores(stress_score, 'Stress')})")
<<<<<<< Updated upstream
    
=======


def main():
    filename, version = main_menu()  # Collects the filename and version based on user input
    questions_list = read_file(filename)  # Reads the questions based on the chosen version
    responses = display_questions_and_collect_responses(questions_list)
    scores = calculate_dass_scores(responses, version)
    print_scores(scores, version)
    make_radar_chart(get_depression_score(responses, version),get_anxiety_score(responses, version),get_stress_score(responses, version)  )
>>>>>>> Stashed changes
    print("\nPlease remember, this tool is not a diagnostic tool. If you are concerned about your mental health, please seek professional advice.")

if __name__ == "__main__":
    main()

