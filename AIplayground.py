goble = int(input())
if goble == 1:
    import pygame
    import time
    import random

    # Initialize pygame
    pygame.init()

    # Define the colors
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    # Set the screen width and height
    width = 600
    height = 400

    # Create the display screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')

    # Define the snake block size and speed
    snake_block = 10
    snake_speed = 15

    # Define the clock object to control the speed of the game
    clock = pygame.time.Clock()

    # Define font styles for displaying text
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)


    # Function to display the score
    def your_score(score):
        value = score_font.render("Your Score: " + str(score), True, black)
        screen.blit(value, [0, 0])


    # Function to draw the snake
    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])


    # Function to display the game over message
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        screen.blit(mesg, [width / 6, height / 3])


    # Main game loop
    def gameLoop():
        game_over = False
        game_close = False

        # Initial position of the snake
        x1 = width / 2
        y1 = height / 2

        # Change in the position of the snake
        x1_change = 0
        y1_change = 0

        # Create the snake's body (list of coordinates)
        snake_List = []
        Length_of_snake = 1

        # Position of the food
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

        # Game loop
        while not game_over:

            while game_close:
                screen.fill(blue)
                message("You Lost! Press C-Play Again or Q-Quit", red)
                your_score(Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            screen.fill(blue)
            pygame.draw.rect(screen, yellow, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            your_score(Length_of_snake - 1)

            pygame.display.update()

            # Check if the snake has eaten the food
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()


    # Start the game
    gameLoop()
if goble == 2:
    import pygame
    import sys

    # Initialize Pygame
    pygame.init()

    # Define constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    BLOCK_SIZE = 40
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    BROWN = (139, 69, 19)

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Minecraft-like Game (Simplified)")

    # Initialize variables
    blocks = []
    is_placing = True


    # Create block grid
    def create_grid():
        grid = []
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
            row = []
            for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
                row.append(None)
            grid.append(row)
        return grid


    # Draw the grid and blocks
    def draw_grid(grid):
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x]:
                    pygame.draw.rect(screen, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)


    # Game loop
    def game_loop():
        global is_placing
        grid = create_grid()

        clock = pygame.time.Clock()

        while True:
            screen.fill(BLUE)  # Background color (sky blue)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    grid_x = mouse_x // BLOCK_SIZE
                    grid_y = mouse_y // BLOCK_SIZE

                    if is_placing:
                        grid[grid_y][grid_x] = BROWN  # Place a block
                    else:
                        grid[grid_y][grid_x] = None  # Remove a block

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        is_placing = not is_placing  # Toggle between placing and removing blocks

            draw_grid(grid)

            # Instructions
            font = pygame.font.SysFont("Arial", 24)
            instruction_text = "Press SPACE to toggle between placing and removing blocks"
            instructions = font.render(instruction_text, True, WHITE)
            screen.blit(instructions, (20, SCREEN_HEIGHT - 40))

            pygame.display.flip()
            clock.tick(30)  # 30 frames per second


    if __name__ == "__main__":
        game_loop()
if goble == 3:
    import pygame
    from pygame.locals import *
    from OpenGL.GL import *
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
    import random

    # Define the block data for 3D rendering (represented as cube vertices)
    vertices = [
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1),
    ]

    # Define the edges for cube
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7),
    ]

    # Define the surfaces for cube to apply color to each face
    surfaces = [
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 2, 6, 5),
        (3, 0, 4, 7),
    ]

    colors = [
        (1, 0, 0),  # Red
        (0, 1, 0),  # Green
        (0, 0, 1),  # Blue
        (1, 1, 0),  # Yellow
        (1, 0, 1),  # Magenta
        (0, 1, 1),  # Cyan
    ]


    # Function to draw a cube with a random color for each face
    def draw_cube():
        glBegin(GL_QUADS)
        for i, surface in enumerate(surfaces):
            glColor3fv(colors[i % len(colors)])  # Assign color to each face
            for vertex in surface:
                glVertex3fv(vertices[vertex])
        glEnd()

        glBegin(GL_LINES)
        glColor3fv((0, 0, 0))  # Black color for edges
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()


    # Set up the 3D environment
    def setup_3d_environment():
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

        # Set up perspective projection
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (800 / 600), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)


    # Main game loop for handling input and rendering the world
    def game_loop():
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

        setup_3d_environment()

        # Camera rotation variables
        x_rotation = 0
        y_rotation = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()

            # Rotate the camera based on arrow keys
            if keys[K_LEFT]:
                y_rotation -= 1
            if keys[K_RIGHT]:
                y_rotation += 1
            if keys[K_UP]:
                x_rotation -= 1
            if keys[K_DOWN]:
                x_rotation += 1

            # Clear the screen and set up the camera rotation
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glPushMatrix()
            glRotatef(x_rotation, 1, 0, 0)  # X-axis rotation
            glRotatef(y_rotation, 0, 1, 0)  # Y-axis rotation
            draw_cube()
            glPopMatrix()

            pygame.display.flip()
            pygame.time.wait(10)  # Reduce CPU usage


    if __name__ == "__main__":
        game_loop()
if goble == 4:
    import pygame
    import random
    import math

    # Initialize pygame
    pygame.init()

    # Game screen setup
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Basketball Game")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    # Game Clock
    clock = pygame.time.Clock()

    # Player settings
    player_width = 50
    player_height = 50
    player_x = WIDTH // 2 - player_width // 2
    player_y = HEIGHT - player_height - 10
    player_speed = 7

    # Ball settings
    ball_radius = 15
    ball_x = player_x + player_width // 2
    ball_y = player_y - ball_radius
    ball_velocity = [0, 0]
    shooting = False
    gravity = 0.5
    bounce_factor = 0.7

    # Hoop settings
    hoop_width = 100
    hoop_height = 20
    hoop_x = random.randint(0, WIDTH - hoop_width)
    hoop_y = 100
    hoop_speed = 5

    # Score settings
    score = 0
    font = pygame.font.SysFont("Arial", 30)

    # Load Sounds
    shoot_sound = pygame.mixer.Sound('shoot.wav')
    score_sound = pygame.mixer.Sound('score.wav')
    bounce_sound = pygame.mixer.Sound('bounce.wav')

    # Background
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(WHITE)


    # Draw Score
    def draw_score():
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))


    # Draw player
    def draw_player():
        pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))


    # Draw the ball
    def draw_ball():
        pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)


    # Draw the hoop
    def draw_hoop():
        pygame.draw.rect(screen, BLUE, (hoop_x, hoop_y, hoop_width, hoop_height))


    # Handle player movement
    def handle_player_movement(keys):
        global player_x
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed


    # Shoot ball with better control
    def shoot_ball():
        global ball_x, ball_y, ball_velocity, shooting
        if shooting:
            ball_velocity[1] += gravity  # Apply gravity
            ball_x += ball_velocity[0]
            ball_y += ball_velocity[1]

            # Ball hits the floor
            if ball_y > HEIGHT - ball_radius:
                ball_y = HEIGHT - ball_radius
                ball_velocity[1] = -ball_velocity[1] * bounce_factor
                bounce_sound.play()

            # Ball reaches the hoop
            if hoop_x <= ball_x <= hoop_x + hoop_width and hoop_y <= ball_y <= hoop_y + hoop_height:
                score_sound.play()
                return True
        return False


    # Move the hoop back and forth
    def move_hoop():
        global hoop_x, hoop_speed
        hoop_x += hoop_speed
        if hoop_x <= 0 or hoop_x >= WIDTH - hoop_width:
            hoop_speed = -hoop_speed


    # Main game loop
    def main():
        global shooting, ball_x, ball_y, ball_velocity, hoop_x, score
        while True:
            screen.blit(background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not shooting:
                        shooting = True
                        ball_velocity = [random.randint(-5, 5), -15]  # Random initial velocity
                        shoot_sound.play()

            # Player movement
            keys = pygame.key.get_pressed()
            handle_player_movement(keys)

            # Check for ball shooting and score
            if shooting:
                if shoot_ball():
                    score += 1
                    shooting = False
                    ball_x = player_x + player_width // 2
                    ball_y = player_y - ball_radius
                    ball_velocity = [0, 0]

            # Move hoop
            move_hoop()

            # Draw everything
            draw_score()
            draw_player()
            draw_ball()
            draw_hoop()

            pygame.display.update()
            clock.tick(60)


    # Start the game
    if __name__ == "__main__":
        main()















