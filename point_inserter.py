import pygame
import sys

class PointInserter:
    def __init__(self, screen):
        self.screen = screen

    def insert_point(self, position, point_color):
        pygame.draw.circle(self.screen, point_color, position, 5)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.insert_point(event.pos, selected_color)

    def update_display(self):
        pygame.display.flip()

# Main module combining both functionalities
if __name__ == "__main__":
    from color_selector import ColorSelector

    selected_color = None

    def on_color_selected(color):
        global selected_color
        selected_color = color

    color_selector = ColorSelector(on_color_selected)
    color_selector.run()

    # Pygame initialization
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 800, 600

    # Create the Pygame window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point Inserter")

    # Initialize PointInserter with the Pygame screen
    point_inserter = PointInserter(screen)

    # Main game loop
    while True:
        point_inserter.handle_events()
        point_inserter.update_display()
