import pygame

print("SETUP START")
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print("SETUP END")

print("LOOP START")
while True:
    # CHECK FOR ALL EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # CLOSE THE WINDOW
            quit()
