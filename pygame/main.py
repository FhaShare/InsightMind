import pygame
import buttons

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((534, 950))

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
    dass21_intro = pygame.image.load('pygame/images/dass21_intro.png').convert()
        #Page6: Dass42 introduction
    dass42_intro = pygame.image.load('pygame/images/dass42_intro.png').convert()
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

    current_page = 0

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
                current_page = 4
            if dass42_button.draw(screen):
                print("dass42_button clicked")
                current_page = 5

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()