import pygame

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((534, 950))
    pygame.display.set_caption("InsightMind")

    #Image loading
    # image1 = pygame.image.load("images/filename.png")
    main_menu = pygame.image.load("images/Main Menu.png")


    running = True
    while running:
        screen.fill((0,0,0))

        #ImAGE draw
        # screen.blit(Image variable name, (x position, y position))
        screen.blit(main_menu, (0,0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()