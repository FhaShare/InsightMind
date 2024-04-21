import pygame
import buttons

def load_questionnaire_images(base_path, prefix, count):
    images = []

    for i in range(1, count + 1):
        filename = f"{base_path}/{prefix}_{i}.png"

        image = pygame.image.load(filename).convert_alpha()
        images.append(image)

    #for i in range(1, count + 1):
        #filename = f"{base_path}/{prefix}_{i}.png"

        #image = pygame.image.load(filename).convert_alpha()  # convert_alpha() for better performance with transparency
        #images.append(image)

    return images

def questionnaire_display(screen, current_question_index, responses, dass42List, response_buttons, last_responses, font, back_button, next_button):
    screen.blit(dass42List[current_question_index], (0, 0))
    response = None
    for i, button in enumerate(response_buttons):
        if button.draw(screen):
            responses[current_question_index] = i
            last_responses[current_question_index] = i
            response = i
        
        if last_responses[current_question_index] == i:
            pygame.draw.rect(screen, (192, 192, 192), button.rect.inflate(2, 2), 1)

    if back_button.draw(screen):
        if current_question_index > 0:
            return False, current_question_index - 1  # Return False and the new question index
        else:
            # Handle the case where there is no previous question (maybe go back to a menu)
            return False, current_question_index

    # Display error if no response and next button is pressed
    if next_button.draw(screen) and response is None:
        error_message = font.render("Please select an option to continue.", True, (255, 0, 0))
        screen.blit(error_message, (100, 900))
        return False

    return True, current_question_index 

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

def print_scores(screen, scores, version, font):
    depression_score, anxiety_score, stress_score = scores
    
    # Use the interpret_scores function to get labels
    depression_label = interpret_scores(depression_score, 'Depression')
    anxiety_label = interpret_scores(anxiety_score, 'Anxiety')
    stress_label = interpret_scores(stress_score, 'Stress')
    
    # Render the score texts
    depression_text = f"Depression: {depression_score} ({depression_label})"
    anxiety_text = f"Anxiety: {anxiety_score} ({anxiety_label})"
    stress_text = f"Stress: {stress_score} ({stress_label})"
    
    # Create surfaces for each score
    depression_surf = font.render(depression_text, True, (255, 255, 255))
    anxiety_surf = font.render(anxiety_text, True, (255, 255, 255))
    stress_surf = font.render(stress_text, True, (255, 255, 255))
    
    # Position and draw these surfaces on the screen
    screen.blit(depression_surf, (50, 200))
    screen.blit(anxiety_surf, (50, 250))
    screen.blit(stress_surf, (50, 300))

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
    main_menu = pygame.image.load('pygame\images\MainMenu.png')
        # Page2: Introduction DASS
    intro_page1 = pygame.image.load('pygame/images/Introduction_DASS.png').convert()
        # Page3: The DASS and Diagnosis
    intro_page2 = pygame.image.load('pygame/images/DASS_Diagnosis.png').convert()
        #Page4: DassMenu
    dass_menu = pygame.image.load('pygame/images/DassMenu.png').convert()
        #Page5: Dass21 introduction
    dass21_intro = pygame.image.load('pygame\images\dass21_intro.png').convert()
        #Page6: Dass42 introduction
    dass42_intro = pygame.image.load('pygame\images\dass42_intro.png').convert()
        #Page7: questionnaire (Use None for dynamic content page)
        #Page8: Result
    result_page = pygame.image.load('pygame/images/result.png').convert()
        # List of pages 
    pages = [main_menu, intro_page1, intro_page2, dass_menu, dass21_intro, dass42_intro, None, result_page]

    # Initialize buttons
        # Button on MainMenu page
    mainButton_img = pygame.image.load("pygame/images/MainButton.png").convert_alpha()
    main_button = buttons.Button(65, 474.8, mainButton_img, 1)
        # Button for navigating pages
    back_img = pygame.image.load("pygame/images/back.png").convert_alpha()
    back_intro_button = buttons.Button(291, 860, back_img, 1)
    back_button = buttons.Button(167, 812, back_img, 1)
    next_img = pygame.image.load("pygame/images/next.png").convert_alpha()
    next_intro_button = buttons.Button(395, 860, next_img, 1)
    next_button = buttons.Button(367, 812, next_img, 1)
    start_img = pygame.image.load("pygame/images/start_80px.png").convert_alpha()
    start_button = buttons.Button(206.3, 760, start_img, 1)
        # Button on DassMenu page
    dass21_img = pygame.image.load("pygame/images/dass21.png").convert_alpha()
    dass21_button = buttons.Button(140, 300, dass21_img, 1)
    dass42_img = pygame.image.load("pygame/images/dass42.png").convert_alpha()
    dass42_button = buttons.Button(140, 790, dass42_img, 1)
        # Button for Responses
    respones0_img = pygame.image.load("pygame/images/response0.png").convert_alpha()
    respones0_button = buttons.Button(124, 390, respones0_img, 1)
    respones1_img = pygame.image.load("pygame/images/response1.png").convert_alpha()
    respones1_button = buttons.Button(124, 490, respones1_img, 1)
    respones2_img = pygame.image.load("pygame/images/response2.png").convert_alpha()
    respones2_button = buttons.Button(124, 590, respones2_img, 1)
    respones3_img = pygame.image.load("pygame/images/response3.png").convert_alpha()
    respones3_button = buttons.Button(124, 690, respones3_img, 1)
    response_buttons = [respones0_button, respones1_button, respones2_button, respones3_button]

    # DASS21 pages

    # DASS42 Pages
    # Initialize responses and last_responses for DASS42 questionnaire
    dass42List = load_questionnaire_images("pygame/images/Dass42_questionnaires", "dass42", 42)
    responses = [-1] * len(dass42List)
    

    current_page = 0
    questionnair_finish = False

    running = True
    while running:
        # Clear the screen
        screen.fill((0,0,0))
        
        if current_page == 0:
            screen.blit(main_menu, (0, 0))

            # Draw the start button on the main menu
            if main_button.draw(screen):
                print("Button clicked")  # Debug print
                current_page = 1  # Move to the second page

        # DassMenu page logic
        elif current_page == 1:
            screen.blit(intro_page1, (0, 0))
            
            if back_intro_button.draw(screen):
                print("Back Button clicked")  # Debug print
                current_page -= 1  # Move back to the previous pages
            if next_intro_button.draw(screen):
                print("Next Button clicked")  # Debug print
                current_page += 1  # Move for to the previous pages

        elif current_page == 2:
            screen.blit(intro_page2, (0, 0))
            
            if back_intro_button.draw(screen):
                print("Back Button clicked")  # Debug print
                current_page -= 1  # Move back to the previous pages
            if next_intro_button.draw(screen):
                print("Next Button clicked")  # Debug print
                current_page += 1  # Move for to the previous pages

        # DassMenu page logic
        elif current_page == 3:
            screen.blit(dass_menu, (0, 0))

            if dass21_button.draw(screen):
                print("dass21_button clicked")
                #selectedList = dass21List
                current_page = 4
            if dass42_button.draw(screen):
                print("dass42_button clicked")
                selectedList = dass42List
                current_page = 5

        # DASS introduction
        elif current_page == 4:
            screen.blit(dass21_intro, (0, 0))

            if start_button.draw(screen):
                print("DASS introduction - Button clicked")  # Debug print
                current_question_index = 0  # Reset the question index to start at the first question
                current_page = 6  # Move to questionnaire page

        elif current_page == 5:
            screen.blit(dass42_intro, (0, 0))

            if start_button.draw(screen):
                print("DASS introduction - Button clicked")  # Debug print
                current_question_index = 0  # Reset the question index to start at the first question
                current_page = 6  # Move to questionnaire page      
                
        # DASS42 questionnaire display
        if current_page == 6:  # Assuming page 6 is the questionnaire

            screen.blit(selectedList[current_question_index], (0,0))

            if respones0_button.draw(screen):
                #logice here
                # respone 1
                if selectedList[current_question_index] == selectedList[-1]:
                    questionnair_finish = True
                else:
                    current_question_index += 1

            if respones1_button.draw(screen):
                #logice here
                #response 2
                if selectedList[current_question_index] == selectedList[-1]:
                    questionnair_finish = True
                else:
                    current_question_index += 1

            if respones2_button.draw(screen):
                #logice here
                if selectedList[current_question_index] == selectedList[-1]:
                    questionnair_finish = True
                else:
                    current_question_index += 1

            if respones3_button.draw(screen):
                #logice here
                if selectedList[current_question_index] == selectedList[-1]:
                    questionnair_finish = True
                else:
                    current_question_index += 1

        if questionnair_finish == True:
            screen.blit(result_page, (0, 0))

            # print result onto screen logic
            textString = "This is where my result would be"

            ending_text = font.render(textString, True, (0, 0, 0))
            
            screen.blit(ending_text, (250, 290))
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()