import pygame, pymunk, pymunk.pygame_util

def apple(space, pos):
    body = pymunk.Body(10, 10, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    body.angular_velocity = -10
    shape = pymunk.Circle(body, 20)
    shape.elasticity = 1
    space.add(body, shape)
    return body, shape

def ledge(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)    
    shape = pymunk.Segment(body, (600,400), (0, 500), 2)
    shape.elasticity = 0.5
    space.add(body, shape)
    return shape

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((600,500))
space = pymunk.Space()
space.gravity = (50 ,700)


apples = []
ledge_shape = ledge(space)

while True:    
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONUP:
            ball_body, arrow_shape = apple(space, event.pos)
            apples.append(arrow_shape)
            
    space.debug_draw(pymunk.pygame_util.DrawOptions(screen))
    
    space.step(1/60)
    pygame.display.update()
    clock.tick(60)