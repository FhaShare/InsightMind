import pygame
import buttons



def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((534, 950))
    pygame.display.set_caption("InsightMind")

    #Image loading
    # image1 = pygame.image.load("images/filename.png")
    main_menu = pygame.image.load("pygame/images/MainMenu.png")
    # second_page = pygame.image.load()
    dass_menu = pygame.image.load("pygame/images/DassMenu.png")

    # List of pages
    pages = [main_menu, dass_menu]

    # Button on MainMenu page
    start_img = pygame.image.load('pygame/images/MainButton.png').convert_alpha()
    start_button = buttons.Button(65, 474.8, start_img, 1)

    # Button on DassMenu page
    dass21_img = pygame.image.load('pygame/images/dass21.png').convert_alpha()
    dass21_button = buttons.Button(140, 300, dass21_img, 1)
    dass42_img = pygame.image.load('pygame/images/dass42.png').convert_alpha()
    dass42_button = buttons.Button(140, 790, dass42_img, 1)

    # DASS21 pages
    

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
        elif current_page == 1:
            if dass21_button.draw(screen):
                print("dass21_button clicked") 
                # current_question = dass21List[0]
            if dass42_button.draw(screen):
                print("dass42_button clicked")
                # current_question = dass42List[0]

        #for question in dass21List:
            #screenblitz(currrent_question)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()