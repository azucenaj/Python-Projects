import pygame, sys
from simulation import Simulation
# from sandgrid import Grid
# from sandparticle import SandParticle

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
FPS = 120
GREY = (29, 29, 29)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Sand Box')

clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
# simulation.add_particle(0,0)
# simulation.add_particle(1,1)
# simulation.remove_particle(1,1)
# grid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
# grid.cells[0][0] = SandParticle()
# grid.cells[2][1] = SandParticle()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    buttons = pygame.mouse.get_pressed()
    if buttons[0]:
        pos = pygame.mouse.get_pos()
        row = pos[1] // CELL_SIZE
        column = pos[0] // CELL_SIZE
        simulation.add_particle(row, column) 
    
    simulation.update()

    window.fill(GREY)
    simulation.draw(window)
    # grid.draw(window)

    pygame.display.flip()
    clock.tick(FPS)