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

    start_img = pygame.image.load('pygame/images/MainButton.png').convert_alpha()

    start_button = buttons.Button(35, 474.8, start_img, 1)

    # slide_list = [main_menu, second_page]
    # questionair1 = [...]
    # questionair2 = [...]

    current_page = 0

    running = True
    while running:
        screen.fill((0,0,0))

        #ImAGE draw
        # screen.blit(Image variable name, (x position, y position))
        screen.blit(main_menu, (0,0))

        if start_button.draw(screen):
            print("click")

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()