import pygame
import sys
import random
import pymunk
import pymunk.pygame_util
import math

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Physics Simulator')
icon = pygame.image.load('pendulum.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800, 600), 0, 32)
font = pygame.font.SysFont('Comic Sans MS', 20)
background = pygame.image.load('Ui-1.png')

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


click = False


def main_menu():
    while True:

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(100, 150, 205, 40)
        button_2 = pygame.Rect(500, 150, 200, 40)
        button_3 = pygame.Rect(350, 150, 100, 40)
        if button_1.collidepoint((mx, my)):
            if click:
                game1()
        if button_2.collidepoint((mx, my)):
            if click:
                game2()
        if button_3.collidepoint((mx, my)):
            if click:
                game3()
        pygame.draw.rect(screen, (7, 192, 198), button_1)
        pygame.draw.rect(screen, (7, 192, 198), button_2)
        pygame.draw.rect(screen, (7, 192, 198), button_3)
        draw_text('InclinedPlane', font, (0, 0, 0), screen, 145, 155)
        draw_text('Collision', font, (0, 0, 0), screen, 560, 155)
        draw_text('orbiting', font, (0, 0, 0), screen, 360, 155)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game1():
    pygame.init()
    clock = pygame.time.Clock()
    # creating screen
    screen = pygame.display.set_mode((800, 600))
    base_font = pygame.font.Font(None, 32)
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    my_font2 = pygame.font.SysFont('Comic Sans MS', 25)
    user_text = ''
    user_text2 = ''
    user_text3 = ''
    force_result = ''
    acc_result = ''
    time_result = ''
    msg1 = 'value cant be zero'
    show1 = False
    show2 = False
    show3 = False
    # defining variables
    acceleration = 0
    imass = 0
    angle = 0
    ilength = 0
    sin0 = 0
    time = 0
    force = 0
    # creating rectangle1
    input_rect = pygame.Rect(680, 60, 100, 32)
    color_active = pygame.Color('blue4')
    color_passive = pygame.Color('gray15')
    color = color_passive
    active = False

    # creating rectangle2
    input_rect2 = pygame.Rect(680, 110, 100, 32)
    color_active2 = pygame.Color('lightskyblue3')
    color_passive2 = pygame.Color('gray15')
    color2 = color_passive2
    active2 = False

    # creating rectangle3
    input_rect3 = pygame.Rect(680, 160, 100, 32)
    color_active3 = pygame.Color('lightskyblue3')
    color_passive3 = pygame.Color('gray15')
    color3 = color_passive3
    active3 = False

    # background
    background = pygame.image.load('ϴ.png')

    # title and icon
    pygame.display.set_caption("Motion on Inclined Plane")
    icon = pygame.image.load('physics-7.png')
    pygame.display.set_icon(icon)

    # game loop
    running = True
    while running:
        # rgb- red ,green ,blue
        screen.fill((0, 0, 0))
        # background
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True

                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        mass = user_text
                        # converting str into int
                        imass = int(mass)
                        if imass == 0:
                            send_message1 = my_font2.render(msg1, True, (255, 0, 0))
                            screen.blit(send_message1, (0, 0))
                    else:
                        user_text += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect2.collidepoint(event.pos):
                    active2 = True
                else:
                    active2 = False

            if event.type == pygame.KEYDOWN:
                if active2:
                    if event.key == pygame.K_BACKSPACE:
                        user_text2 = user_text2[:-1]
                    elif event.key == pygame.K_RETURN:
                        angle = user_text2
                        iangle = int(angle)
                        sinp = math.sin(math.radians(iangle))
                        force = imass * 9.8 * sinp
                        iforce = round(force, 2)
                        force_result = my_font2.render("{}".format(iforce), True, (0, 100, 0))
                        show1 = True

                    else:
                        user_text2 += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect3.collidepoint(event.pos):
                    active3 = True
                else:
                    active3 = False

            if event.type == pygame.KEYDOWN:
                if active3:
                    if event.key == pygame.K_BACKSPACE:
                        user_text3 = user_text3[:-1]
                    elif event.key == pygame.K_RETURN:
                        length = user_text3
                        ilength = int(length)
                        acceleration = force / imass
                        iacceleration = round(acceleration, 2)
                        acc_result = my_font2.render("{}".format(iacceleration), True, (0, 100, 0))
                        show2 = True
                        # t= t*t
                        t = 2 * ilength / acceleration
                        time = math.sqrt(t)
                        itime = round(time, 2)
                        time_result = my_font2.render("{}".format(itime), True, (0, 100, 0))
                        show3 = True
                    else:
                        user_text3 += event.unicode

        if active:
            color = color_active
        else:
            color = color_passive

        if active2:
            color2 = color_active2
        else:
            color2 = color_passive2

        if active3:
            color3 = color_active3
        else:
            color3 = color_passive3

        pygame.draw.rect(screen, color, input_rect, 2)
        pygame.draw.rect(screen, color, input_rect2, 2)
        pygame.draw.rect(screen, color, input_rect3, 2)

        text_surface = base_font.render(user_text, True, (0, 0, 0))
        text_surface2 = base_font.render(user_text2, True, (0, 0, 0))
        text_surface3 = base_font.render(user_text3, True, (0, 0, 0))

        # linking input text to rectangle and printing and making it look good
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        screen.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))
        screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
        #     limiting the no.of characters input and stopping the text from leaving box.
        input_rect.w = max(100, text_surface.get_width() + 10)
        input_rect2.w = max(100, text_surface2.get_width() + 10)
        input_rect3.w = max(100, text_surface3.get_width() + 10)

        # headings
        # inputs:
        input_heading = my_font.render('Input:', True, (0, 0, 0))
        screen.blit(input_heading, (650, 10))
        mass_heading = base_font.render('mass(kg):', True, (0, 0, 0))
        screen.blit(mass_heading, (565, 65))
        Angle_heading = base_font.render('angle(θ):', True, (0, 0, 0))
        screen.blit(Angle_heading, (580, 115))
        Length_heading = base_font.render('length(m):', True, (0, 0, 0))
        screen.blit(Length_heading, (560, 165))
        # Result:
        Result_heading = my_font.render('Result:', True, (0, 0, 0))
        screen.blit(Result_heading, (650, 215))
        force_heading = my_font2.render('force(N):', True, (0, 0, 0))
        screen.blit(force_heading, (560, 265))
        acc_heading = my_font2.render('Acc(m/s²):', True, (0, 0, 0))
        screen.blit(acc_heading, (540, 315))
        time_heading = my_font2.render('time(s):', True, (0, 0, 0))
        screen.blit(time_heading, (580, 365))
        # print results
        if show1:
            screen.blit(force_result, (680, 265))
        if show2:
            screen.blit(acc_result, (680, 315))
        if show3:
            screen.blit(time_result, (680, 365))

        #  updating screen
        pygame.display.update()
        clock.tick(60)

def game3():
    random.seed(5)
    gravityStrength = 5.0e6

    def planetGravity(body, gravity, damping, dt):
        # Gravitational acceleration is proportional to the inverse square of
        # distance, and directed toward the origin. The central planet is assumed
        # to be massive enough that it affects the satellites but not vice versa.
        sq_dist = body.position.get_dist_sqrd((300, 300))
        g = (
                (body.position - pymunk.Vec2d(300, 300))
                * -gravityStrength
                / (sq_dist * math.sqrt(sq_dist))
        )
        pymunk.Body.update_velocity(body, g, damping, dt)

    def add_box(space):
        body = pymunk.Body()
        body.position = pymunk.Vec2d(random.randint(50, 550), random.randint(50, 550))
        body.velocity_func = planetGravity

        # Set the box's velocity to put it into a circular orbit from its
        # starting position.
        r = body.position.get_distance((300, 300))
        v = math.sqrt(gravityStrength / r) / r
        body.velocity = (body.position - pymunk.Vec2d(300, 300)).perpendicular() * v
        # Set the box's angular velocity to match its orbital period and
        # align its initial angle with its position.
        body.angular_velocity = v
        body.angle = math.atan2(body.position.y, body.position.x)

        box = pymunk.Poly.create_box(body, size=(10, 10))
        box.mass = 1
        box.friction = 0.7
        box.elasticity = 0
        box.color = pygame.Color("white")
        space.add(body, box)

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    background = pygame.image.load('space2.jpg')
    space = pymunk.Space()
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    icon = pygame.image.load('physics-8.png')
    pygame.display.set_icon(icon)
    for x in range(30):
        add_box(space)
    star_surface = pygame.image.load('star.png')
    star_rect = star_surface.get_rect(center=(300, 300))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        screen.blit(background, (0, 0))
        space.debug_draw(draw_options)
        screen.blit(star_surface, star_rect)
        space.step(1 / 60)

        pygame.display.flip()
        clock.tick(60)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))

def game2():
    # title and icon
    pygame.display.set_caption("collision of two bodies")
    icon = pygame.image.load('collision.png')
    pygame.display.set_icon(icon)

    def create_apple(space, pos):
        body = pymunk.Body(10, 100, body_type=pymunk.Body.DYNAMIC)  # MASS, INERTIA
        body.position = pos
        shape = pymunk.Circle(body, 10)  # adding a circle
        space.add(body, shape)
        return shape

    def draw_apples(apples):
        for apple in apples:
            pos_x = int(apple.body.position.x)
            pos_y = int(apple.body.position.y)
            apple_rect = apple_surface.get_rect(center=(pos_x, pos_y))
            screen.blit(apple_surface, apple_rect)

    def static_ball(space, pos):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)  # no need of mass, inertia for static bodies
        body.position = pos
        shape = pymunk.Circle(body, 40)
        space.add(body, shape)
        return shape

    def draw_static_ball(balls):
        for ball in balls:
            pos_x = int(ball.body.position.x)
            pos_y = int(ball.body.position.y)
            ball_rect = ball_surface.get_rect(center=(pos_x, pos_y))
            screen.blit(ball_surface, ball_rect)

    pygame.init()  # initiating pygame
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    space = pymunk.Space()
    gd = 0
    gs = 500
    apple_surface = pygame.image.load('asteroid-3.png')
    apples = []
    ball_surface = pygame.image.load('planet-2.png')
    balls = []
    balls.append(static_ball(space, (400, 400)))
    balls.append(static_ball(space, (200, 300)))
    balls.append(static_ball(space, (600, 300)))
    # background
    background1 = pygame.image.load('Untitled design-3.png')
    active = True
    running = True
    while running:  # gameloop
        screen.fill((217, 217, 217))
        # background
        screen.blit(background1, (0, 0))
        space.gravity = (gd, gs)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                apples.append(create_apple(space, event.pos))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    gd += 100
                if event.key == pygame.K_LEFT:
                    gd -= 100
                if event.key == pygame.K_UP:
                    gs += 1000
                if event.key == pygame.K_DOWN:
                    gs -= 1000

        draw_apples(apples)
        draw_static_ball(balls)
        space.step(1 / 50)
        pygame.display.update()
        clock.tick(120)


main_menu()
