import pygame
import math

pygame.init()

window_size = (400, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Calculator")

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

font_small = pygame.font.SysFont(None, 30)
font_large = pygame.font.SysFont(None, 50)

button_width = 80
button_height = 80
button_margin = 10
buttons = []
for row in range(5):
    for col in range(4):
        button = pygame.Rect(
            button_margin + col * (button_width + button_margin),
            120 + row * (button_height + button_margin),
            button_width,
            button_height
        )
        buttons.append(button)

button_labels = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", ".", "+",
    "=", "(", ")", "sqrt"
]

expression = ""
result = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i, button in enumerate(buttons):
                if button.collidepoint(mouse_pos):
                    if i == 16:  # evaluate expression
                        try:
                            result = str(eval(expression))
                        except:
                            result = "Error"
                        expression = ""
                    elif i == 19:  # square root
                        expression += "math.sqrt("
                    elif i == 18:  # close parentheses
                        expression += ")"
                    elif i == 17:  # open parentheses
                        expression += "("
                    elif i == 12:  # clear
                        expression = ""
                        result = ""
                    else:  # add digit/operator to expression
                        expression += button_labels[i]

    window.fill(white)

    for i, button in enumerate(buttons):
        pygame.draw.rect(window, gray, button)
        label = font_large.render(button_labels[i], True, black)
        label_rect = label.get_rect(center=button.center)
        window.blit(label, label_rect)

    expression_label = font_small.render(expression, True, black)
    expression_rect = expression_label.get_rect(x=button_margin, y=button_margin)
    window.blit(expression_label, expression_rect)

    result_label = font_large.render(result, True, black)
    result_rect = result_label.get_rect(right=window_size[0] - button_margin, y=button_margin)
    window.blit(result_label, result_rect)

    pygame.display.flip()

pygame.quit()
