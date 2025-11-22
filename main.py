import pygame
import sys

pygame.init()

TABLE_WIDTH = 800
TABLE_HEIGHT = 400 
WALL_THICKNESS = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TABLE_FELT_COLOR = (0, 100, 0)   
RAIL_COLOR = (101, 67, 33)       
BACKGROUND_COLOR = (50, 50, 50)  

# 1. Intinyga ini CLASS WALL (Dinding)
class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    
    def draw(self, window):
        pygame.draw.rect(window, RAIL_COLOR, self.rect)
        pygame.draw.rect(window, BLACK, self.rect, 1)

    def get_bounds(self):
        return self.rect


# 2. CLASS TABLE (Meja)
class Table:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.felt_rect = pygame.Rect(
            WALL_THICKNESS, WALL_THICKNESS, 
            width - (2 * WALL_THICKNESS), 
            height - (2 * WALL_THICKNESS)
        )
        
        self.walls = [
            Wall(0, 0, width, WALL_THICKNESS), 
            Wall(0, height - WALL_THICKNESS, width, WALL_THICKNESS), 
            Wall(0, 0, WALL_THICKNESS, height), 
            Wall(width - WALL_THICKNESS, 0, WALL_THICKNESS, height) 
        ]
        

    def draw(self, window):
        for wall in self.walls:
            wall.draw(window)
        
        pygame.draw.rect(window, TABLE_FELT_COLOR, self.felt_rect)


# 3. CLASS GAMEMANAGER (yang ngendaliin lah)
class GameManager:
    def __init__(self):
        self.window = pygame.display.set_mode((TABLE_WIDTH, TABLE_HEIGHT))
        pygame.display.set_caption("Simulasi Billiard - Implementasi Awal")
        
        self.table = Table(TABLE_WIDTH, TABLE_HEIGHT)
        
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            delta_time = self.clock.tick(60) / 1000.0 
            
            self.process_events()
            self.update(delta_time)
            self.render()
            
        self.close()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
    def update(self, delta_time):
        pass

    def render(self):
        self.window.fill(BACKGROUND_COLOR)
        
        self.table.draw(self.window)        
        
        pygame.display.flip()

    def close(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = GameManager()
    game.run()