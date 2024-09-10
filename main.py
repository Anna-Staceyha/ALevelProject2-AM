import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("dark blue")

        PLAY_TEXT = get_font(45).render("Levels", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 60))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 660), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        PLAY_LEVEL1 = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="Level 1", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        
        PLAY_LEVEL1.changeColor(PLAY_MOUSE_POS)
        PLAY_LEVEL1.update(SCREEN)
    

        PLAY_LEVEL2 = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 400), 
                            text_input="Level 2", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        
        PLAY_LEVEL2.changeColor(PLAY_MOUSE_POS)
        PLAY_LEVEL2.update(SCREEN)


        PLAY_LEVEL3 = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 550), 
                            text_input="Level 3", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        
        PLAY_LEVEL3.changeColor(PLAY_MOUSE_POS)
        PLAY_LEVEL3.update(SCREEN)

        for button in [PLAY_LEVEL1, PLAY_LEVEL2, PLAY_LEVEL3]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_LEVEL1.checkForInput(PLAY_MOUSE_POS):
                        play()
                if PLAY_LEVEL2.checkForInput(PLAY_MOUSE_POS):
                    options()
                if PLAY_LEVEL3.checkForInput(PLAY_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("Earthly Duo", True, "#89cff0")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(55), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()





main_menu()

def play_level1():
    while True:
        play_level1_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        play_level1_TEXT = get_font(45).render("This is the LEVEL 1 screen.", True, "Black")
        play_level1_RECT = play_level1_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(play_level1_TEXT, play_level1_RECT)

        play_level1_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        play_level1_BACK.changeColor(play_level1_MOUSE_POS)
        play_level1_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           

        pygame.display.update()



def level_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        LEVELS_MOUSE_POS = pygame.mouse.get_pos()

        LEVELS_TEXT = get_font(80).render("Levels", True, "#89cff0")
        LEVELS_RECT = LEVELS_TEXT.get_rect(center=(640, 100))

        LEVELS_BACK = Button(image=None, pos=(640, 660), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        LEVELS_BACK.changeColor(LEVELS_MOUSE_POS)
        LEVELS_BACK.update(SCREEN)

        LEVELS_LEVEL1 = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="Level 1", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        
        LEVELS_LEVEL1.changeColor(LEVELS_MOUSE_POS)
        LEVELS_LEVEL1.update(SCREEN)
    

        LEVELS_LEVEL2 = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 400), 
                            text_input="Level 2", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        
        LEVELS_LEVEL2.changeColor(LEVELS_MOUSE_POS)
        LEVELS_LEVEL2.update(SCREEN)


        LEVELS_LEVEL3 = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 550), 
                            text_input="Level 3", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        
        LEVELS_LEVEL3.changeColor(LEVELS_MOUSE_POS)
        LEVELS_LEVEL3.update(SCREEN)

        SCREEN.blit(LEVELS_TEXT, LEVELS_RECT)

        for button in [LEVELS_LEVEL1, LEVELS_LEVEL2, LEVELS_LEVEL3]:
            button.changeColor(LEVELS_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():      
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVELS_LEVEL1.checkForInput(LEVELS_MOUSE_POS):
                    play_level1()
                if LEVELS_LEVEL2.checkForInput(LEVELS_MOUSE_POS):
                    play_level2()
                if LEVELS_LEVEL3.checkForInput(LEVELS_MOUSE_POS):
                    play_level3()

        pygame.display.update()