import pygame
import buttons

def load_questionnaire_images(base_path, prefix, count):
    images = []
    for i in range(1, count + 1):
        filename = f"{base_path}/{prefix}_{i}.png"
        try:
            image = pygame.image.load(filename).convert_alpha()  # convert_alpha() for better performance with transparency
            images.append(image)
        except pygame.error as e:
            print(f"Failed to load image {filename}: {str(e)}")
    return images

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((534, 950))
    pygame.display.set_caption("InsightMind")

    #Image loading
    # image = pygame.image.load("images/filename.png")
    # Page1: Main Menu
    main_menu = pygame.image.load("pygame/images/MainMenu.png")
    # Page2: Introduction DASS
    intro_page1 = pygame.image.load("pygame/images/Introduction_DASS.png")
    # Page3: The DASS and Diagnosis
    intro_page2 = pygame.image.load("pygame/images/DASS_Diagnosis.png")
    #Page4: DassMenu
    dass_menu = pygame.image.load("pygame/images/DassMenu.png")
    #Page5: Dass21 introduction

    #Page6: Dass42 introduction

    # List of pages
    pages = [main_menu, intro_page1, intro_page2, dass_menu]

    # Button on MainMenu page
    start_img = pygame.image.load('pygame/images/MainButton.png').convert_alpha()
    start_button = buttons.Button(65, 474.8, start_img, 1)

    # Button for navigating pages
    back_img = pygame.image.load("pygame/images/back.png")
    back_intro_button = buttons.Button(291, 860, back_img, 1)
    next_img = pygame.image.load("pygame/images/next.png")
    next_intro_button = buttons.Button(395, 860, next_img, 1)
    start_img = pygame.image.load("pygame/images/back.png")

    # Button on DassMenu page
    dass21_img = pygame.image.load('pygame/images/dass21.png').convert_alpha()
    dass21_button = buttons.Button(140, 300, dass21_img, 1)
    dass42_img = pygame.image.load('pygame/images/dass42.png').convert_alpha()
    dass42_button = buttons.Button(140, 790, dass42_img, 1)

    # DASS21 pages

    # DASS42 Pages
    dass42List = load_questionnaire_images("pygame/images", "dass42", 42)
    current_question_index = 0
    

    # slide_list = [main_menu, second_page]
    # questionair1 = [...]
    # questionair2 = [...]

    current_page = 0

    running = True
    while running:
        screen.fill((0,0,0))

        # Draw the current page
        screen.blit(pages[current_page], (0, 0))

        # Draw the start button on the main menu
        if current_page == 0:
            if start_button.draw(screen):
                print("Button clicked")  # Debug print
                current_page = 1  # Move to the second page

        # DassMenu page logic
        elif current_page in [1, 2]:
            if back_intro_button.draw(screen):
                print("Button clicked")  # Debug print
                current_page -= 1  # Move back to the previous pages
            if next_intro_button.draw(screen):
                print("Button clicked")  # Debug print
                current_page += 1  # Move back to the previous pages
        
        # DassMenu page logic
        elif current_page == 3:
            if dass21_button.draw(screen):
                print("dass21_button clicked") 
                # current_question = dass21List[0]
            if dass42_button.draw(screen):
                print("dass42_button clicked")
                # current_question = dass42List[0]

        #for question in dass42List:
            #screenblitz(currrent_question)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()