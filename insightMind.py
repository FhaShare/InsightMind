import pygame
import buttons
import numpy as np
def load_questionnaire_images(base_path, prefix, count):
    images = []

    for i in range(1, count + 1):
        filename = f"{base_path}/{prefix}_{i}.png"

        image = pygame.image.load(filename).convert_alpha()
        images.append(image)

    return images

def handle_questionnaire(screen, current_question_index, responses, dass42List):
    # Handle questionnaire interactions (similar to your existing logic)
    pass

def display_results(screen, responses, font):
    # Calculate scores and display results
    pass

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

def make_radar_chart(screen,depression_score, anxiety_score, stress_score):
    # Define markers and attribute labels for the triangular radar chart
    name= "results"
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
    color = (255, 255, 255)  # White color for lines and area fill
    thickness = 2
    alpha = 128  # Transparency for the area fill
    
    # Calculate points for the radar chart
    points = []
    for angle, stat in zip(angles, stats):
        x = 250 * stat * np.cos(angle) + 300
        y = 250 * stat * np.sin(angle) + 300
        points.append((x, y))
    
    # Draw the radar chart lines
    for i in range(len(points) - 1):
        pygame.draw.line(screen, color, points[i], points[i+1], thickness)
    pygame.draw.line(screen, color, points[-1], points[0], thickness)
    
    # Fill the area of the radar chart
    pygame.draw.polygon(screen, (color[0], color[1], color[2], alpha), points)
    
    # Set axis labels and markers
    font = pygame.font.SysFont(None, 24)
    for angle, label in zip(angles, ["Depression", "Anxiety", "Stress"]):
        text = font.render(label, True, color)
        text_rect = text.get_rect(center=(300 + 250 * np.cos(angle), 300 + 250 * np.sin(angle)))
        screen.blit(text, text_rect)
    
    # Set title
    title_font = pygame.font.SysFont(None, 36)
    title_text = title_font.render(name, True, color)
    screen.blit(title_text, (250, 30))
    
    # Update the display
    pygame.display.flip()
    
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

def debug_print_scores(scores, version):
    depression_score, anxiety_score, stress_score = scores
    print("\nYour Scores:")
    print(f"Depression: {depression_score} ({interpret_scores(depression_score, 'Depression')})")
    print(f"Anxiety: {anxiety_score} ({interpret_scores(anxiety_score, 'Anxiety')})")
    print(f"Stress: {stress_score} ({interpret_scores(stress_score, 'Stress')})")

def print_scores(screen, scores, version, font):
    depression_score, anxiety_score, stress_score = scores
    print("Printing Scores:")  # Debug statement
    print(f"Depression: {depression_score}, Anxiety: {anxiety_score}, Stress: {stress_score}")
    
    # Use the interpret_scores function to get labels
    depression_label = interpret_scores(depression_score, 'Depression')
    anxiety_label = interpret_scores(anxiety_score, 'Anxiety')
    stress_label = interpret_scores(stress_score, 'Stress')
    
    print(f"Labels - Depression: {depression_label}, Anxiety: {anxiety_label}, Stress: {stress_label}")  # Debug

    # Render the score texts
    depression_text = f"Depression: {depression_score} ({depression_label})"
    anxiety_text = f"Anxiety: {anxiety_score} ({anxiety_label})"
    stress_text = f"Stress: {stress_score} ({stress_label})"
    
    # Create surfaces for each score
    depression_surf = font.render(depression_text, True, (255, 0, 0))  # Changed color to red for visibility
    anxiety_surf = font.render(anxiety_text, True, (0, 255, 0))  # Changed color to green for visibility
    stress_surf = font.render(stress_text, True, (0, 0, 255))  # Changed color to blue for visibility
    
    # Position and draw these surfaces on the screen
    screen.blit(depression_surf, (50, 200))
    screen.blit(anxiety_surf, (50, 250))
    screen.blit(stress_surf, (50, 300))
    
    pygame.display.update()  # Ensure the display is updated to show changes


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((534, 950))
    pygame.font.init()  # Initialize the font module
    font = pygame.font.Font(None, 36)  # Global font object

    pygame.display.set_caption("InsightMind")

    #Image loading
    # image = pygame.image.load("images/filename.png")
        # Page1: Main Menu
    main_menu = pygame.image.load('pygame/images/MainMenu.png').convert()
        # Page2: Introduction DASS
    intro_page1 = pygame.image.load('pygame/images/Introduction_DASS.png').convert()
        # Page3: The DASS and Diagnosis
    intro_page2 = pygame.image.load('pygame/images/DASS_Diagnosis.png').convert()
        #Page4: DassMenu
    dass_menu = pygame.image.load('pygame/images/DassMenu.png').convert()
        #Page5: Dass21 introduction
    dass21_intro = pygame.image.load('pygame/images/dass21_intro.png').convert()
        #Page6: Dass42 introduction
    dass42_intro = pygame.image.load('pygame/images/dass42_intro.png').convert()
        #Page7: questionnaire (Use None for dynamic content page)
        #Page8: Result
    result_page = pygame.image.load('pygame/images/result.png').convert()
        # List of pages 
    pages = [main_menu, intro_page1, intro_page2, dass_menu, dass21_intro, dass42_intro, result_page]

    # Initialize buttons
        # Button on MainMenu page
    mainButton_img = pygame.image.load("pygame/images/MainButton.png").convert_alpha()
    main_button = buttons.Button(65, 474.8, mainButton_img, 1)
        # Button for navigating pages
    back_img = pygame.image.load("pygame/images/back.png").convert_alpha()
    back_intro_button = buttons.Button(291, 870, back_img, 1)
    back_button = buttons.Button(200, 850, back_img, 1)
    next_img = pygame.image.load("pygame/images/next.png").convert_alpha()
    next_intro_button = buttons.Button(395, 870, next_img, 1)
    next_button = buttons.Button(279, 850, next_img, 1)
    start_img = pygame.image.load("pygame/images/start_80px.png").convert_alpha()
    start_button = buttons.Button(206.3, 760, start_img, 1)
        # Button on DassMenu page
    dass21_img = pygame.image.load("pygame/images/dass21.png").convert_alpha()
    dass21_button = buttons.Button(140, 300, dass21_img, 1)
    dass42_img = pygame.image.load("pygame/images/dass42.png").convert_alpha()
    dass42_button = buttons.Button(140, 790, dass42_img, 1)
        # Button for Responses
    respones0_img = pygame.image.load("pygame/images/response0.png").convert_alpha()
    respones0_button = buttons.Button(124, 420, respones0_img, 1)
    respones1_img = pygame.image.load("pygame/images/response1.png").convert_alpha()
    respones1_button = buttons.Button(124, 520, respones1_img, 1)
    respones2_img = pygame.image.load("pygame/images/response2.png").convert_alpha()
    respones2_button = buttons.Button(124, 620, respones2_img, 1)
    respones3_img = pygame.image.load("pygame/images/response3.png").convert_alpha()
    respones3_button = buttons.Button(124, 720, respones3_img, 1)

    # Icons
    
    
    # DASS21 pages

    # DASS42 Pages
    # Initialize questionnaire images
    dass42List = load_questionnaire_images("pygame/images/Dass42_questionnaires", "dass42", 42)
    responses = [-1] * len(dass42List)  # Initialize responses list
    current_question_index = 0

    current_page = 0
    question_printed = False
    questionnaire_finished = False
    results_printed = False
    show_error_message = False
    error_message = None 

    running = True
    while running:
        # Clear the screen
        screen.fill((0,0,0))
        # Draw the current page
        screen.blit(pages[current_page], (0, 0))
        
        if current_page == 0:
            # screen.blit(main_menu, (0, 0))

            # Draw the start button on the main menu
            if main_button.draw(screen):
                print("Button clicked")  # Debug print
                current_page = 1  # Move to the second page

        # DassMenu page logic
        elif current_page == 1:
            # screen.blit(intro_page1, (0, 0))
            if back_intro_button.draw(screen):
                print("Back Button clicked")  # Debug print
                current_page -= 1  # Move back to the previous pages
            if next_intro_button.draw(screen):
                print("Next Button clicked")  # Debug print
                current_page += 1  # Move for to the previous pages

        elif current_page == 2:
            # screen.blit(intro_page2, (0, 0))
            if back_intro_button.draw(screen):
                print("Back Button clicked")  # Debug print
                current_page -= 1  # Move back to the previous pages
            if next_intro_button.draw(screen):
                print("Next Button clicked")  # Debug print
                current_page += 1  # Move for to the previous pages

        # DassMenu page logic
        elif current_page == 3:
            # screen.blit(dass_menu, (0, 0))
            if dass21_button.draw(screen):
                print("dass21_button clicked")
                #selectedList = dass21List
                #version = 'DASS-42'
                current_page = 4
            if dass42_button.draw(screen):
                print("dass42_button clicked")
                selectedList = dass42List
                #version = 'DASS-42'
                current_page = 5

        # DASS introduction
        elif current_page == 4:
            #screen.blit(dass21_intro, (0, 0))
            if start_button.draw(screen):
                print("DASS introduction - Button clicked")  # Debug print
                current_question_index = 0  # Reset the question index to start at the first question
                current_page = 6  # Move to questionnaire page

        elif current_page == 5:
            # screen.blit(dass42_intro, (0, 0))
            if start_button.draw(screen):
                print("DASS introduction - Button clicked")  # Debug print
                current_question_index = 0  # Reset the question index to start at the first question
                current_page = 6  # Move to questionnaire page      
                
        # DASS42 questionnaire display
        if current_page == 6: 
            if not questionnaire_finished:
                screen.blit(dass42List[current_question_index], (0, 0))
                handle_questionnaire(screen, current_question_index, responses, dass42List) 
                if not question_printed:
                    print(f"Displaying Question {current_question_index + 1}/{len(dass42List)}")
                    question_printed = True
        
            if respones0_button.draw(screen):
                responses[current_question_index] = 0
                if current_question_index < len(dass42List) - 1:
                    current_question_index += 1
                    show_error_message = False
                    question_printed = False  # Reset flag here
                    print("responses = 0")  # Debug print
                else:
                    questionnaire_finished = True

            if respones1_button.draw(screen):
                responses[current_question_index] = 1
                if current_question_index < len(dass42List) - 1:
                    current_question_index += 1
                    show_error_message = False
                    question_printed = False  # Reset flag here
                    print("responses = 1")  # Debug print
                else:
                    questionnaire_finished = True

            if respones2_button.draw(screen):
                responses[current_question_index] = 2               
                if current_question_index < len(dass42List) - 1:
                    current_question_index += 1
                    show_error_message = False
                    question_printed = False  # Reset flag here
                    print("responses = 2")  # Debug print
                else:
                    questionnaire_finished = True

            if respones3_button.draw(screen):
                responses[current_question_index] = 3
                if current_question_index < len(dass42List) - 1:
                    current_question_index += 1
                    show_error_message = False
                    question_printed = False  # Reset flag here
                    print("responses = 3")  # Debug print
                else:
                    questionnaire_finished = True

            # Button for navigating pages
            if back_button.draw(screen):
                if current_question_index > 0:
                    current_question_index -= 1  # Move back to the previous question
                    question_printed = False  # Reset flag here
                    print("Back Button clicked")  # Debug print
            if next_button.draw(screen):
                print("Next Button clicked")  # Debug print
                if responses[current_question_index] == -1:
                    if not error_message:
                        error_message = font.render("Please select an option to continue.", True, (255, 0, 0))
                    show_error_message = True
                else:
                    show_error_message = False
                    if current_question_index < len(dass42List) - 1:
                        current_question_index += 1
                        question_printed = False  # Ensuring we reset this to allow re-printing question display
                    else:
                        questionnaire_finished = True
            if show_error_message and error_message:
                screen.blit(error_message, (55, 250))

        if questionnaire_finished == True:
            screen.blit(result_page, (0, 0))
            
            # Display a static text on the result screen
            textString = "Here are your results:"
            make_radar_chart(screen,*scores )
            ending_text = font.render(textString, True, (0, 0, 0))
            screen.blit(ending_text, (50, 100))
            
            if not results_printed:
                # Calculate and display the scores
                scores = calculate_dass_scores(responses, 'DASS-42')
                print_scores(screen, scores, 'DASS-42', font)  # Correctly call print_scores
                debug_print_scores(scores, 'DASS-42')  # Optionally print scores to console for debugging
                results_printed = True

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
