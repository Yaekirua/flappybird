import pygame

GRAVITY = 1
FLAP_STRENGTH = -15
x
# This class is used to represent a bird in a game
class Bird:
    # Initialize the bird with an image located at the specified path
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path) # Load the image from the file
        self.rect = self.image.get_rect(center=(100, 300)) # Get the rectangle representing the image and center it at (100, 300)
        self.velocity = 0 # Initialize the velocity to 0

    # This method is used to make the bird flap its wings
    def flap(self):
        self.velocity = FLAP_STRENGTH # Set the velocity to the flap strength

    # This method is used to update the bird's position based on its velocity
    def update(self):
        self.velocity += GRAVITY # Add gravity to the velocity
        self.rect.y += self.velocity # Update the bird's y-position based on its velocity

    # This method is used to draw the bird on the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect) # Draw the bird's image on the screen