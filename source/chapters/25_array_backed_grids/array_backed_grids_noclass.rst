.. _array-backed-grids:

Array-Backed Grids
==================

Introduction
------------


Games like minesweeper, tic-tac-toe, and many types of adventure games keep
data for the game in a grid of numbers. For example, a tic-tac-toe board:
 
+---+---+---+
|   | O | O |
+---+---+---+
|   | X |   |
+---+---+---+
| X |   |   |
+---+---+---+
 
. . . can use a grid of numbers to represent the empty spots, the O's and the
X's like this:

+---+---+---+
| 0 | 2 | 2 |
+---+---+---+
| 0 | 1 | 0 |
+---+---+---+
| 1 | 0 | 0 |
+---+---+---+

This grid of numbers can also be called a *two-dimensional* array or a *matrix*.
(Finally, we get to learn about The Matrix.) The values of the numbers in the
grid represent what should be displayed at each board location. In the prior
example, 0 represents a spot where no one has played, a 1 represents an X, and
a 2 represents an O.

.. figure:: minesweeper.png

    Figure 16.1: Minesweeper game, showing the backing grid of numbers

The figure above is an example from the classic minesweeper game. This example
has been modified to show both the classic display on the left, and the grid of
numbers used to display the board on the right.

The number ``10`` represents a mine, the number ``0`` represents a space that
has not been clicked, and the number 9 represents a cleared space. The numbers
``1`` to ``8`` represent how many mines are within the surrounding eight
squares, and is only filled in when the user clicks on the square.

Minesweeper can actually have two grids. One for the regular display, and a
completely separate grid of numbers that will track if the user has placed
"flags" on the board marking where she thinks the mines are.

Classic adventure game maps are created using a tiled map editor. These are
huge grids where each location is simply a number representing the type of
terrain that goes there. The terrain could be things like dirt, a road, a
path, green grass, brown grass, and so forth. Programs like Tiled_ shown in
the figure below allow a developer to easily make these maps and write the grid to
disk.

.. _Tiled: http://www.mapeditor.org/

.. figure:: qt_tiled.png

    Figure 16.2: Using Qt Tiles to create an adventure map

Adventure games also use multiple grids of numbers, just like minesweeper has
a grid for the mines, and a separate grid for the flags. One grid, or "layer,"
in the adventure game represents terrain you can walk on; another for things
you can't walk on like walls and trees; a layer for things that can instantly
kill you, like lava or bottomless pits; one for objects that can be picked up
and moved around; and yet another layer for initial placement of monsters.

Maps like these can be loaded in a Python program, but unfortunately a full
description of how to manage is beyond the scope of this book. Projects like
PyTMX_ that provide some of the code needed to load these maps.

.. _PyTMX: https://github.com/bitcraft/PyTMX

Application
-----------

Enough talk, let's write some code. This example will create a grid that will
trigger if we display a white or green block. We can change the grid value and
make it green by clicking on it. This is a first step to a grid-based game
like minesweeper, battleship, connect four, etc. (One year I had a student
call me over and she had modified a program like this to show my name in
flashing lights. That was . . . disturbing. So please use this knowledge
only for good!)

Start with this template:

.. code-block:: python

    import arcade


    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 600


    def on_update(delta_time):
        pass


    def on_draw():
        arcade.start_render()
        # Draw in here...



    def on_key_press(key, modifiers):
        pass


    def on_key_release(key, modifiers):
        pass


    def on_mouse_press(x, y, button, modifiers):
        pass


    def setup():
        arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "My Arcade Game")
        arcade.set_background_color(arcade.color.WHITE)
        arcade.schedule(on_update, 1/60)

        # Override arcade window methods
        window = arcade.get_window()
        window.on_draw = on_draw
        window.on_key_press = on_key_press
        window.on_key_release = on_key_release
        window.on_mouse_press = on_mouse_press

        arcade.run()


    if __name__ == '__main__':
        setup()


Starting with the file above, attempt to recreate this program
following the instructions here. The final program is at the end of this
chapter but don't skip ahead and copy it! If you do that you'll have learned
nothing. Anyone can copy and paste the code, but if you can recreate this
program you have skills people are willing to pay for. If you can only copy
and paste, you've wasted your time here.

Drawing the Grid
^^^^^^^^^^^^^^^^

1. Create variables named ``WIDTH``, ``HEIGHT``, and ``MARGIN``. Set the width
   and height to 20. This will represent how large each grid location is. Set
   the margin to 5. This represents the margin between each grid location and
   the edges of the screen. Create these variables at the top of the program, after
   the ``import`` statements.
   Also create variables ``ROW_COUNT`` and ``COLUMN_COUNT``. Set them to 10.
   This will control how many rows and columns we will have.  Finally, create a
   ``grid`` variable (still in the global variables area after the ``import`` statement)
   and set it to an empty list ``[]``
2. Calculate ``SCREEN_WIDTH`` and ``SCREEN_HEIGHT`` based on the variables we
   created above. If we have 10 rows, and each row is 20 high, that's 200 pixels.
   If we have 10 rows, that's also 11 margins. (Nine between the cells and two on
   each edge.) That is 55 more pixels for a total of 255. Write the equation
   so it works with whatever we select in the constants created by step 1.
3. Change the background to black. Draw a white box in the lower-left corner. Draw the box drawn using the
   height and width variables created earlier. (Feel free to adjust the colors.)
   Use the `draw_rectangle_filled`_ function. You will need to center the
   rectangle not at (0, 0) but at a coordinate that takes into account the
   height and width of the rectangle, such as ``width/2``.
   When you get done your program's window should look like:

.. figure:: step_03.png

    Figure 16.3: Step 3

4. Use a ``for`` loop to draw ``COLUMN_COUNT`` boxes in a row. Use ``column``
   for the variable name in the ``for`` loop. The output will look like one
   long box until we add in the margin between boxes. See Figure 16.4.

.. figure:: step_04.png

    Figure 16.4: Step 4

5. Adjust the drawing of the rectangle to add in the ``MARGIN`` variable. Now
   there should be gaps between the rectangles. See Figure 16.5.

.. figure:: step_05.png

    Figure 16.5: Step 5

6. Add the margin before drawing the rectangles, in addition to between each
   rectangle. This should keep the box from appearing right next to the window
   edge. See Figure 16.6. You'll end up with an equation like: ``(margin + width)*column + margin + width/2``


.. figure:: step_06.png

    Figure 16.6: Step 6

7. Add another ``for`` loop that also will loop for each row. Call the variable in
   this ``for`` loop ``row``. Now we should have a full grid of boxes. See Figure 16.7.

.. figure:: step_07.png

    Figure 16.7: Step 7

Populating the Grid
^^^^^^^^^^^^^^^^^^^

8. Now we need to create a two-dimensional array. We need to create this once, at program
   start-up. So this will go in the program's ``setup()`` method.
   Creating a two-dimensional array
   in Python is, unfortunately, not as easy as it is in some other computer
   languages. There are some libraries that can be downloaded for Python that make
   it easy (like numpy), but for this example they will not be used. To create a two-dimensional
   array and set an example, use the code below:

.. code-block:: python

    def setup():

        global grid

        arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "My Arcade Game")
        arcade.set_background_color(arcade.color.WHITE)
        arcade.schedule(on_update, 1/60)

        # Override arcade window methods
        window = arcade.get_window()
        window.on_draw = on_draw
        window.on_key_press = on_key_press
        window.on_key_release = on_key_release
        window.on_mouse_press = on_mouse_press



        # create a 10 x 10 2D list of numbers

        # --- Populate grid the grid
        # Loop for each row
        for row in range(ROW_COUNT):
            # For each row, create a list that will
            # represent an entire row
            grid.append([])
            # Loop for each column
            for column in range(COLUMN_COUNT):
                # Add a the number zero to the current row
                grid[row].append(0)

        arcade.run()

A much shorter example is below, but this example uses some odd parts of
Python that I don't bother to explain in this book:

.. code-block:: python

    grid = [[0 for x in range(10)] for y in range(10)]

Use one of these two examples and place the code to create our array ahead of
your main program loop.

9. Set an example location in the array to 1.

Two dimensional arrays are usually represented addressed by first their row,
and then the column. This is called a row-major storage. Most languages use
row-major storage, with the exception of Fortran and MATLAB. Fortran and
MATLAB use column-major storage.

.. code-block:: python

    # Set row 1, column 5 to one
    grid[1][5] = 1

Place this code somewhere ahead of your main program loop.

10. Select the color of the rectangle based on the value of a variable named
    ``color``. Do this by first finding the line of code where the rectangle is
    drawn. Ahead of it, create a variable named ``color`` and set it equal to white.
    Then replace the white color in the rectangle declaration with the ``color``
    variable.

11. Select the color based on the value in the grid. After setting color to
    white, place an if statement that looks at the value in
    ``grid[row][column]`` and changes the color to green if the grid value is
    equal to 1. There should now be one green square. See Figure 16.8.

.. figure:: step_11.png

    Figure 16.8: Step 11

12. Print "click" to the screen if the user clicks the mouse button.
    See the button_click.py example if you've forgotten how to do that.

13. Print the mouse coordinates when the user clicks the mouse.

14. Convert the mouse coordinates into grid coordinates. Print those
    instead. Remember to use the width and height of each grid location
    combined with the margin. It will be necessary to convert the final
    value to an integer. This can be done by using int or by using the
    integer division operator ``//`` instead of the normal division operator
    ``/``. See Figure 16.9.

.. figure:: step_14.png

    Figure 16.9: Step 14

15. Set the grid location at the row/column clicked to 1. See Figure 16.10.

.. figure:: step_15.png

    Figure 16.10: Step 15

Final Program
^^^^^^^^^^^^^
.. code-block:: python

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


