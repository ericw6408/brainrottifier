import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

options = ["goob", "gooby", "Option 3", "Option 4", "Option 5"]
selected = None
dropdown_open = False
dropdown_rect = pygame.Rect(50, 50, 150, 30)
option_height = 30
scroll_offset = 0
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(144)
    screen.fill((30, 30, 30))
    mouse_pos = pygame.mouse.get_pos()

    # Draw dropdown button
    pygame.draw.rect(screen, (200, 200, 200), dropdown_rect)
    font = pygame.font.Font(None, 24)
    text = font.render(selected if selected else "Select...", True, (0, 0, 0))
    print(selected)
    screen.blit(text, (dropdown_rect.x + 5, dropdown_rect.y + 5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            if dropdown_rect.collidepoint(event.pos):
                dropdown_open = not dropdown_open
            else:
                if dropdown_open:
                    dropdown_open = False
        elif event.type == pygame.MOUSEWHEEL:
            if dropdown_open:
                scroll_offset = min(max(scroll_offset - event.y, 0), len(options) - 3)

    # Draw options if open

    if dropdown_open:
        for i, option in enumerate(options[scroll_offset:scroll_offset+3]):  # show max 3
            option_rect = pygame.Rect(dropdown_rect.x, dropdown_rect.y + (i+1)*option_height, dropdown_rect.width, option_height)
            pygame.draw.rect(screen, (180, 180, 180), option_rect)
            screen.blit(font.render(option, True, (0, 0, 0)), (option_rect.x + 5, option_rect.y + 5))
            if option_rect.collidepoint(mouse_pos):
                print(option)

                if event.type == pygame.MOUSEBUTTONDOWN or pygame.mouse.get_pressed()[0]:
                    selected = option
                    dropdown_open = False


    pygame.display.flip()
    clock.tick(60)

pygame.quit()