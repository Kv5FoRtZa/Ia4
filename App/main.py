from global_variables import *

# filling the screen with white temporarily 
screen.fill(white)
pygame.display.update()

# method that keeps the screen open until the x button is pressed
def main():
    
    run = True
    while run:
        CLOCK.tick(fps)     # maintains frame rate 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()

main()
