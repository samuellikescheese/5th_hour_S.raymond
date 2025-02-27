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
    def draw_cube(position):
        glPushMatrix()
        glTranslatef(position[0], position[1], position[2])  # Move the cube to the correct position
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
        glPopMatrix()


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

        blocks = []  # Store placed blocks here
        block_size = 2  # Size of each block in the 3D world

        # Camera rotation variables
        x_rotation = 0
        y_rotation = 0
        camera_position = [0, 0, -10]  # Initial camera position
        camera_speed = 0.1

        # Main game loop
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

            # Move the camera with WASD keys
            if keys[K_w]:
                camera_position[2] += camera_speed
            if keys[K_s]:
                camera_position[2] -= camera_speed
            if keys[K_a]:
                camera_position[0] += camera_speed
            if keys[K_d]:
                camera_position[0] -= camera_speed

            # Check for mouse clicks to place blocks
            if pygame.mouse.get_pressed()[0]:  # Left mouse button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                world_x = (mouse_x - 400) / 100.0  # Map mouse position to world coordinates
                world_y = -(mouse_y - 300) / 100.0
                # Place the block at the calculated position
                blocks.append([world_x, world_y, -5])  # Place block at a fixed Z position

            # Clear the screen and set up the camera rotation
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()

            # Move camera based on position and rotation
            glTranslatef(camera_position[0], camera_position[1], camera_position[2])
            glRotatef(x_rotation, 1, 0, 0)  # X-axis rotation
            glRotatef(y_rotation, 0, 1, 0)  # Y-axis rotation

            # Draw all placed blocks
            for block in blocks:
                draw_cube(block)

            pygame.display.flip()
            pygame.time.wait(10)  # Reduce CPU usage


    if __name__ == "__main__":
        game_loop
if goble == 4:
    import pygame
    from pygame.locals import *
    from OpenGL.GL import *
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
    import math

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
    def draw_cube(position):
        glPushMatrix()
        glTranslatef(position[0], position[1], position[2])  # Move the cube to the correct position
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
        glPopMatrix()


    # Set up the 3D environment
    def setup_3d_environment():
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

        # Set up perspective projection
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (800 / 600), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -15)


    # Convert screen coordinates to 3D world coordinates for placing blocks
    def screen_to_world(x, y):
        # Convert from screen space to normalized device coordinates (-1 to 1)
        normalized_x = (x / 400.0) - 1
        normalized_y = -((y / 300.0) - 1)
        return normalized_x, normalized_y, -5  # Fixed Z value to place blocks on the "ground"


    # Main game loop for handling input and rendering the world
    def game_loop():
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

        setup_3d_environment()

        blocks = []  # Store placed blocks here

        # Camera rotation variables
        x_rotation = 0
        y_rotation = 0
        camera_position = [0, 0, -15]  # Initial camera position
        camera_speed = 0.1

        # Main game loop
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

            # Move the camera with WASD keys
            if keys[K_w]:
                camera_position[2] += camera_speed
            if keys[K_s]:
                camera_position[2] -= camera_speed
            if keys[K_a]:
                camera_position[0] += camera_speed
            if keys[K_d]:
                camera_position[0] -= camera_speed

            # Check for mouse clicks to place blocks
            if pygame.mouse.get_pressed()[0]:  # Left mouse button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                world_x, world_y, world_z = screen_to_world(mouse_x, mouse_y)
                # Place the block at the calculated position
                blocks.append([world_x, world_y, world_z])  # Place block at a fixed Z position

            # Clear the screen and set up the camera rotation
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()

            # Move camera based on position and rotation
            glTranslatef(camera_position[0], camera_position[1], camera_position[2])
            glRotatef(x_rotation, 1, 0, 0)  # X-axis rotation
            glRotatef(y_rotation, 0, 1, 0)  # Y-axis rotation

            # Draw all placed blocks
            for block in blocks:
                draw_cube(block)

            pygame.display.flip()
            pygame.time.wait(10)  # Reduce CPU usage


    if __name__ == "__main__":
        game_loop()















