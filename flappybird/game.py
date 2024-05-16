import pygame
from .bird import Bird
from .pipe import Pipe

class FlappyBirdGame:
    def __init__(self, bird_image, background_image):
        pygame.init() 
        self.screen = pygame.display.set_mode((400, 600))
        self.clock = pygame.time.Clock()
        self.bird = Bird(bird_image)
        self.pipes = [Pipe(pipe_image, 400 + i * 200) for i in range(3)]
        self.background = pygame.image.load(background_image)
        self.score = 0

    def reset(self):
        self.bird = Bird(bird_image)
        self.pipes = [Pipe(pipe_image, 400 + i * 200) for i in range(3)]
        self.score = 0

    def run(self):
        running = True
        while running:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.flap()

            self.bird.update()
            for pipe in self.pipes:
                pipe.update()
                if pipe.is_off_screen():
                    self.pipes.remove(pipe)
                    self.pipes.append(Pipe(pipe_image, 400))
                    self.score += 1
                if pipe.collides_with(self.bird):
                    self.reset()

            self.bird.draw(self.screen)
            for pipe in self.pipes:
                pipe.draw(self.screen)

            font = pygame.font.SysFont(None, 36)
            score_surface = font.render(f'Score: {self.score}', True, (255, 255, 255))
            self.screen.blit(score_surface, (10, 10))

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()