##Author: Fhaungfha Suvannakajorn 

import pygame
import buttons

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

def load_icons():
    icons = {
        "Depression": {
            "Normal": pygame.image.load("pygame/images/Depression/Depression_Normal.png").convert_alpha(),
            "Mild": pygame.image.load("pygame/images/Depression/Depression_Mild.png").convert_alpha(),
            "Moderate": pygame.image.load("pygame/images/Depression/Depression_Moderate.png").convert_alpha(),
            "Severe": pygame.image.load("pygame/images/Depression/Depression_Severe.png").convert_alpha(),
            "Extremely Severe": pygame.image.load("pygame/images/Depression/Depression_ExtremelySevere.png").convert_alpha()
        },
        "Anxiety": {
            "Normal": pygame.image.load("pygame/images/Anxiety/Anxiety_Normal.png").convert_alpha(),
            "Mild": pygame.image.load("pygame/images/Anxiety/Anxiety_Mild.png").convert_alpha(),
            "Moderate": pygame.image.load("pygame/images/Anxiety/Anxiety_Moderate.png").convert_alpha(),
            "Severe": pygame.image.load("pygame/images/Anxiety/Anxiety_Severe.png").convert_alpha(),
            "Extremely Severe": pygame.image.load("pygame/images/Anxiety/Anxiety_ExtremelySevere.png").convert_alpha()
        },
        "Stress": {
            "Normal": pygame.image.load("pygame/images/Stress/Stress_Normal.png").convert_alpha(),
            "Mild": pygame.image.load("pygame/images/Stress/Stress_Mild.png").convert_alpha(),
            "Moderate": pygame.image.load("pygame/images/Stress/Stress_Moderate.png").convert_alpha(),
            "Severe": pygame.image.load("pygame/images/Stress/Stress_Severe.png").convert_alpha(),
            "Extremely Severe": pygame.image.load("pygame/images/Stress/Stress_ExtremelySevere.png").convert_alpha()
        }
    }
    return icons

def display_icons(screen, scores, icons):
    depression_score, anxiety_score, stress_score = scores
    depression_label = interpret_scores(depression_score, 'Depression')
    anxiety_label = interpret_scores(anxiety_score, 'Anxiety')
    stress_label = interpret_scores(stress_score, 'Stress')

    depression_icon = icons['Depression'][depression_label]
    anxiety_icon = icons['Anxiety'][anxiety_label]
    stress_icon = icons['Stress'][stress_label]

    # Icon positions might need to be adjusted based on your layout
    screen.blit(depression_icon, (100, 400))
    screen.blit(anxiety_icon, (100, 500))
    screen.blit(stress_icon, (100, 600))

def load_result():
    result = {
        "Depression": {
            "Normal": pygame.image.load("pygame/images/Depression_results/Depression_results_normal.png").convert_alpha(),
            "Mild": pygame.image.load("pygame/images/Depression_results/Depression_results_mild.png").convert_alpha(),
            "Moderate": pygame.image.load("pygame/images/Depression_results/Depression_results_moderate.png").convert_alpha(),
            "Severe": pygame.image.load("pygame/images/Depression_results/Depression_results_severe.png").convert_alpha(),
            "Extremely Severe": pygame.image.load("pygame/images/Depression_results/Depression_results_extremely-severe.png").convert_alpha()
        },
        "Anxiety": {
            "Normal": pygame.image.load("pygame/images/Anxiety_results/Anxiety_results_normal.png").convert_alpha(),
            "Mild": pygame.image.load("pygame/images/Anxiety_results/Anxiety_results_mild.png").convert_alpha(),
            "Moderate": pygame.image.load("pygame/images/Anxiety_results/Anxiety_results_moderate.png").convert_alpha(),
            "Severe": pygame.image.load("pygame/images/Anxiety_results/Anxiety_results_severe.png").convert_alpha(),
            "Extremely Severe": pygame.image.load("pygame/images/Anxiety_results/Anxiety_results_extremely-servere.png").convert_alpha()
        },
        "Stress": {
            "Normal": pygame.image.load("pygame/images/Stress_results/Stress_results_normal.png").convert_alpha(),
            "Mild": pygame.image.load("pygame/images/Stress_results/Stress_results_mild.png").convert_alpha(),
            "Moderate": pygame.image.load("pygame/images/Stress_results/Stress_results_moderate.png").convert_alpha(),
            "Severe": pygame.image.load("pygame/images/Stress_results/Stress_results_severe.png").convert_alpha(),
            "Extremely Severe": pygame.image.load("pygame/images/Stress_results/Stress_results_extremely-severe.png").convert_alpha()
        }
    }
    return result

def load_advice():
    advice = {
        "Depression": {
            "Normal": pygame.image.load("pygame/images/Depression_advices/Depression_advices_normal.png").convert_alpha(),
            "Mild": pygame.image.load("pygame/images/Depression_advices/Depression_advices_mild.png").convert_alpha(),
            "Moderate": pygame.image.load("pygame/images/Depression_advices/Depression_advices_moderate.png").convert_alpha(),
            "Severe": pygame.image.load("pygame/images/Depression_advices/Depression_advices_severe.png").convert_alpha(),
            "Extremely Severe": pygame.image.load("pygame/images/Depression_advices/Depression_advices_extremely-severe.png").convert_alpha()
        },
        "Anxiety": {
            "Normal": pygame.image.load("pygame/images/Anxiety_advices/Anxiety_advices_normal.png").convert_alpha(),
            "Mild": pygame.image.load("pygame/images/Anxiety_advices/Anxiety_advices_mild.png").convert_alpha(),
            "Moderate": pygame.image.load("pygame/images/Anxiety_advices/Anxiety_advices_moderate.png").convert_alpha(),
            "Severe": pygame.image.load("pygame/images/Anxiety_advices/Anxiety_advices_severe.png").convert_alpha(),
            "Extremely Severe": pygame.image.load("pygame/images/Anxiety_advices/Anxiety_advices_extremly-severe.png").convert_alpha()
        },
        "Stress": {
            "Normal": pygame.image.load("pygame/images/Stress_advices/Stress_advices_normal.png").convert_alpha(),
            "Mild": pygame.image.load("pygame/images/Stress_advices/Stress_advices_mild.png").convert_alpha(),
            "Moderate": pygame.image.load("pygame/images/Stress_advices/Stress_advices_moderate.png").convert_alpha(),
            "Severe": pygame.image.load("pygame/images/Stress_advices/Stress_advices_severe.png").convert_alpha(),
            "Extremely Severe": pygame.image.load("pygame/images/Stress_advices/Stress_advices_extremely-severe.png").convert_alpha()
        }
    }
    return advice

def display_result(screen, scores, result):
    depression_score, anxiety_score, stress_score = scores
    depression_label = interpret_scores(depression_score, 'Depression')
    anxiety_label = interpret_scores(anxiety_score, 'Anxiety')
    stress_label = interpret_scores(stress_score, 'Stress')

    depression_result = result['Depression'][depression_label]
    anxiety_result = result['Anxiety'][anxiety_label]
    stress_result = result['Stress'][stress_label]

    screen.blit(depression_result, (0, 0))
    screen.blit(anxiety_result, (0, 0))
    screen.blit(stress_result, (0, 0))

def debug_print_scores(scores, version):
    depression_score, anxiety_score, stress_score = scores
    print(f"\nYour Scores:", version)
    print(f"Depression: {depression_score} ({interpret_scores(depression_score, 'Depression')})")
    print(f"Anxiety: {anxiety_score} ({interpret_scores(anxiety_score, 'Anxiety')})")
    print(f"Stress: {stress_score} ({interpret_scores(stress_score, 'Stress')})")

def print_scores(screen, scores, font):

    depression_score, anxiety_score, stress_score = scores
    
    # Use the interpret_scores function to get labels
    depression_label = interpret_scores(depression_score, 'Depression')
    anxiety_label = interpret_scores(anxiety_score, 'Anxiety')
    stress_label = interpret_scores(stress_score, 'Stress')
    
    # Render the score texts
    depression_text = f"{depression_score} ({depression_label})"
    anxiety_text = f"{anxiety_score} ({anxiety_label})"
    stress_text = f"{stress_score} ({stress_label})"
    
    # Create surfaces for each score
    depression_surf = font.render(depression_text, True, (117, 25, 25)) 
    anxiety_surf = font.render(anxiety_text, True, (117, 25, 25)) 
    stress_surf = font.render(stress_text, True, (117, 25, 25)) 
    
    # Position and draw these surfaces on the screen
    screen.blit(depression_surf, (205, 136))
    screen.blit(anxiety_surf, (165, 372))
    screen.blit(stress_surf, (151, 610))
    
    
    pygame.display.update()  # Ensure the display is updated to show changes

# def make_radar_chart(screen, name, scores, font):
    #Code for graph


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((534, 950))
    pygame.font.init()  # Initialize the font module
    font = pygame.font.Font(None, 20)  
    font2 = pygame.font.Font("pygame/font/LoveDays-2v7Oe.ttf", 22)
    font3 = pygame.font.Font("pygame/font/LoveDays-2v7Oe.ttf", 28)


    pygame.display.set_caption("InsightMind")

    #Image loading
    # image = pygame.image.load("images/filename.png")
        # Page1: Main Menu
    main_menu = pygame.image.load('pygame/images/MainMenu.png').convert()
        # Page2: Introduction DASS
    intro_page1 = pygame.image.load('pygame/images/Introduction_DASS.png').convert()
        # Page3: The DASS and Diagnosis
    intro_page2 = pygame.image.load('pygame/images/DASS_Diagnosis.png').convert()
        # Page4: DassMenu
    dass_menu = pygame.image.load('pygame/images/DassMenu.png').convert()
        # Page5: Dass21 introduction
    dass21_intro = pygame.image.load('pygame/images/dass21_intro.png').convert()
        # Page6: Dass42 introduction
    dass42_intro = pygame.image.load('pygame/images/dass42_intro.png').convert()
        # Page7: questionnaire (Use None for dynamic content page)
    questionnaire_page = pygame.image.load('pygame/images/clear_page.png').convert()
        # Page8: Result
    result_page = pygame.image.load('pygame/images/result.png').convert()
        # Page9: Advice
    advice_page = pygame.image.load('pygame/images/advice.png').convert()
        # Page10: graph
    graph_page = pygame.image.load('pygame/images/graph.png').convert()
        # List of pages 
    pages = [main_menu, intro_page1, intro_page2, dass_menu, dass21_intro, dass42_intro, questionnaire_page, result_page, advice_page]
    
    # Initialize buttons
        # Button on MainMenu page
    mainButton_img = pygame.image.load("pygame/images/MainButton.png").convert_alpha()
    main_button = buttons.Button(65, 474.8, mainButton_img, 1)
        # Button for navigating pages
    back_img = pygame.image.load("pygame/images/back.png").convert_alpha()
    back_intro_button = buttons.Button(350, 880, back_img, 1)
    back_button = buttons.Button(200, 850, back_img, 1)
    next_img = pygame.image.load("pygame/images/next.png").convert_alpha()
    next_intro_button = buttons.Button(430, 880, next_img, 1)
    next_button = buttons.Button(279, 850, next_img, 1)
    start_img = pygame.image.load("pygame/images/start_80px.png").convert_alpha()
    start_button = buttons.Button(206.3, 800, start_img, 1)
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

    icons = load_icons()
    result = load_result()
    advice = load_advice()
   
    # DASS21 pages
    dass21List = load_questionnaire_images("pygame/images/Dass21_questionnaires", "dass21", 21)
    dass21_responses = [-1] * len(dass21List)  # Initialize responses list

    # DASS42 Pages
    # Initialize questionnaire images
    dass42List = load_questionnaire_images("pygame/images/Dass42_questionnaires", "dass42", 42)
    dass42_responses = [-1] * len(dass42List)  # Initialize responses list

    current_page = 0
    current_question_index = 0
    
    question_printed = False
    questionnaire_finished = False
    results_printed = False
    show_error_message = False

    responses = None
    version = None
    error_message = None 

    running = True
    while running:
        # Clear the screen
        screen.fill((0,0,0))
        # Draw the current page
        screen.blit(pages[current_page], (0, 0))

        if current_page >= len(pages):
            print(f"Error: current_page {current_page} is out of range. Resetting to last available page.")
            current_page = len(pages) - 1  # Reset to the last valid page index
        elif current_page < 0:
            print(f"Error: current_page {current_page} is negative. Resetting to first page.")
            current_page = 0  # Reset to the first page index
        
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
                responses = dass21_responses
                version = 'DASS-21'
                current_page = 4
            if dass42_button.draw(screen):
                print("dass42_button clicked")
                responses = dass42_responses
                version = 'DASS-42'
                current_page = 5

        # DASS introduction
        elif current_page == 4:
            #screen.blit(dass21_intro, (0, 0))
            if start_button.draw(screen):
                print("DASS introduction - Button clicked")  # Debug print
                current_question_index = 0  # Reset the question index to start at the first question
                current_page = 6  # Move to questionnaire page

        # DASS21 questionnaire display
        if current_page == 6 and version == 'DASS-21': 
            if not questionnaire_finished:
                screen.blit(dass21List[current_question_index], (0, 0))
                handle_questionnaire(screen, current_question_index, dass21_responses, dass21List) 
                if not question_printed:
                    print(f"Displaying Question {current_question_index + 1}/{len(dass21List)}")
                    question_printed = True
                pass
            else:
                if not results_printed:
                    current_page = 7  # Transition to results page
                    results_printed = True
                    print("Transitioning to results page.")
            
            if respones0_button.draw(screen):
                dass21_responses[current_question_index] = 0
                if current_question_index < len(dass21List) - 1:
                    current_question_index += 1
                    show_error_message = False
                    question_printed = False  # Reset flag here
                    print("responses = 0")  # Debug print
                else:
                    questionnaire_finished = True

            if respones1_button.draw(screen):
                dass21_responses[current_question_index] = 1
                if current_question_index < len(dass21List) - 1:
                    current_question_index += 1
                    show_error_message = False
                    question_printed = False  # Reset flag here
                    print("responses = 1")  # Debug print
                else:
                    questionnaire_finished = True

            if respones2_button.draw(screen):
                dass21_responses[current_question_index] = 2               
                if current_question_index < len(dass21List) - 1:
                    current_question_index += 1
                    show_error_message = False
                    question_printed = False  # Reset flag here
                    print("responses = 2")  # Debug print
                else:
                    questionnaire_finished = True

            if respones3_button.draw(screen):
                dass21_responses[current_question_index] = 3
                if current_question_index < len(dass21List) - 1:
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
                if dass21_responses[current_question_index] == -1:
                    if not error_message:
                        error_message = font2.render("Please select an option to continue.", True, (255, 0, 0))
                    show_error_message = True
                else:
                    show_error_message = False
                    if current_question_index < len(dass42List) - 1:
                        current_question_index += 1
                        question_printed = False  # Ensuring we reset this to allow re-printing question display
                    else:
                        questionnaire_finished = True
            if show_error_message and error_message:
                screen.blit(error_message, (80, 240))
                

        elif current_page == 5:
            screen.blit(dass42_intro, (0, 0))
            if start_button.draw(screen):
                print("DASS introduction - Button clicked")  # Debug print
                current_question_index = 0  # Reset the question index to start at the first question
                current_page = 6  # Move to questionnaire page
        
        # DASS42 questionnaire display
        if current_page == 6 and version == 'DASS-42': 
            if not questionnaire_finished:
                screen.blit(dass42List[current_question_index], (0, 0))
                handle_questionnaire(screen, current_question_index, dass42_responses, dass42List) 
                if not question_printed:
                    print(f"Displaying Question {current_question_index + 1}/{len(dass42List)}")
                    question_printed = True
                pass
            else:
                if not results_printed:
                    current_page = 7  # Transition to results page
                    results_printed = True
                    print("Transitioning to results page.")
                
            if respones0_button.draw(screen):
                dass42_responses[current_question_index] = 0
                if current_question_index < len(dass42List) - 1:
                    current_question_index += 1
                    show_error_message = False
                    question_printed = False  # Reset flag here
                    print("responses = 0")  # Debug print
                else:
                    questionnaire_finished = True

            if respones1_button.draw(screen):
                dass42_responses[current_question_index] = 1
                if current_question_index < len(dass42List) - 1:
                    current_question_index += 1
                    show_error_message = False
                    question_printed = False  # Reset flag here
                    print("responses = 1")  # Debug print
                else:
                    questionnaire_finished = True

            if respones2_button.draw(screen):
                dass42_responses[current_question_index] = 2               
                if current_question_index < len(dass42List) - 1:
                    current_question_index += 1
                    show_error_message = False
                    question_printed = False  # Reset flag here
                    print("responses = 2")  # Debug print
                else:
                    questionnaire_finished = True

            if respones3_button.draw(screen):
                dass42_responses[current_question_index] = 3
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
                if dass42_responses[current_question_index] == -1:
                    if not error_message:
                        error_message = font2.render("Please select an option to continue.", True, (255, 0, 0))
                    show_error_message = True
                else:
                    show_error_message = False
                    if current_question_index < len(dass42List) - 1:
                        current_question_index += 1
                        question_printed = False  # Ensuring we reset this to allow re-printing question display
                    else:
                        questionnaire_finished = True
            if show_error_message and error_message:
                screen.blit(error_message, (80, 240))

        # Handling the results page
        if current_page == 7:
            screen.blit(result_page, (0, 0))
            textString = "Here are your results"
            header_text = font3.render(textString, True, (0, 0, 0))
            screen.blit(header_text, (130, 80))

            scores = calculate_dass_scores(responses, version)
            display_result(screen, scores, result)
            print_scores(screen, scores, font2)

            if results_printed:
                print("\nResponses: ", responses) 
                debug_print_scores(scores, version)
                results_printed = False  # Set this flag to prevent re-printing

            if next_intro_button.draw(screen):
                current_page += 1
                print("Navigating to advice page.")
            
        # Handling the advice page
        elif current_page == 8: 
            screen.blit(advice_page, (0, 0))
            textString = "General Advice"
            headle_text = font3.render(textString, True, (0, 0, 0))
            screen.blit(headle_text, (180, 80))

            display_result(screen, scores, advice)
            if back_intro_button.draw(screen):
                print("Back Button clicked")
                current_page = 7  # Move back to results page
            # if next_intro_button.draw(screen):
            #     print("Next Button clicked")
            #     current_page = 9  # Navigate to graph page
            #     print("Navigating to graph page.")
            

        # # Handling the graph results page
        # elif current_page == 9: 
        #     screen.blit(graph_page, (0, 0))
        #     textString = "Graph Results"
        #     headle_text = font3.render(textString, True, (0, 0, 0))
        #     screen.blit(headle_text, (190, 90))

        #     # make_radar_chart(screen, name, scores, font):

        #     if back_intro_button.draw(screen):
        #         print("Back Button clicked")
        #         current_page = 8  # Move back to advice page

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()