import arcade


# Set how many rows and columns we will have
ROW_COUNT = 10
COLUMN_COUNT = 10

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out oiur screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


grid = []

def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw the grid
    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            # Figure out what color to draw the box
            if grid[row][column] == 1:
                color = arcade.color.GREEN
            else:
                color = arcade.color.WHITE

            # Do the math to figure out where the box is
            x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
            y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

            # Draw the box
            arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    # Change the x/y screen coordinates to grid coordinates
    column = x // (WIDTH + MARGIN)
    row = y // (HEIGHT + MARGIN)

    print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

    # Make sure we are on-grid. It is possible to click in the upper right
    # corner in the margin and go to a grid location that doesn't exist
    if row < ROW_COUNT and column < COLUMN_COUNT:

        # Flip the location between 1 and 0.
        if grid[row][column] == 0:
            grid[row][column] = 1
        else:
            grid[row][column] = 0


def setup():
    global grid

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Array Backed Grids")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    # array is simply a list of lists.
    for row in range(ROW_COUNT):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(COLUMN_COUNT):
            grid[row].append(0)  # Append a cell

    arcade.run()


if __name__ == '__main__':
    setup()
