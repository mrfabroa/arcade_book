"""
Example "Arcade" library code.

This example shows the drawing primitives and
how they are used.
"""

# Library imports
import math
import arcade
import time

# Open the window and set the background
arcade.open_window("Drawing Example", 600, 600)

arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

arcade.draw_line(120, 0, 120, 600, arcade.color.BLACK, 2)

# Draw a grid
x = 120
while x < 800:
    arcade.draw_line(x, 0, x, 600, arcade.color.BLACK, 2)
    x += 120

y = 200
while y < 500:
    arcade.draw_line(0, y, 800, y, arcade.color.BLACK, 2)
    y += 200

# Draw a point
arcade.draw_text("draw_point", 3, 405, arcade.color.BLACK, 12)
arcade.draw_point(60, 495, arcade.color.RED, 10)

# Draw a set of points
arcade.draw_text("draw_points", 123, 405, arcade.color.BLACK, 12)
point_list = ((165, 495),
              (165, 480),
              (165, 465),
              (195, 495),
              (195, 480),
              (195, 465))
arcade.draw_points(point_list, arcade.color.ZAFFRE, 10)

# Draw a line
arcade.draw_text("draw_line", 243, 405, arcade.color.BLACK, 12)
arcade.draw_line(270, 495, 300, 450, arcade.color.WOOD_BROWN, 3)

# Draw a set of lines
arcade.draw_text("draw_lines", 363, 405, arcade.color.BLACK, 12)
point_list = ((390, 450),
              (450, 450),
              (390, 480),
              (450, 480),
              (390, 510),
              (450, 510)
              )
arcade.draw_lines(point_list, arcade.color.BLUE, 3)

# Draw a line strip
arcade.draw_text("draw_line_strip", 483, 405, arcade.color.BLACK, 12)
point_list = ((510, 450),
              (570, 450),
              (510, 480),
              (570, 480),
              (510, 510),
              (570, 510)
              )
arcade.draw_line_strip(point_list, arcade.color.TROPICAL_RAIN_FOREST, 3)

# Draw a polygon
arcade.draw_text("draw_polygon_outline", 3, 207, arcade.color.BLACK, 9)
point_list = ((30, 240),
              (45, 240),
              (60, 255),
              (60, 285),
              (45, 300),
              (30, 300))
arcade.draw_polygon_outline(point_list, arcade.color.SPANISH_VIOLET, 3)

# Draw a filled in polygon
arcade.draw_text("draw_polygon_filled", 123, 207, arcade.color.BLACK, 9)
point_list = ((150, 240),
              (165, 240),
              (180, 255),
              (180, 285),
              (165, 300),
              (150, 300))
arcade.draw_polygon_filled(point_list, arcade.color.SPANISH_VIOLET)

# Draw an outline of a circle
arcade.draw_text("draw_circle_outline", 243, 207, arcade.color.BLACK, 10)
arcade.draw_circle_outline(300, 285, 18, arcade.color.WISTERIA, 3)

# Draw a filled in circle
arcade.draw_text("draw_circle_filled", 363, 207, arcade.color.BLACK, 10)
arcade.draw_circle_filled(420, 285, 18, arcade.color.GREEN, 3)

# Draw an ellipse outline, and another one rotated
arcade.draw_text("draw_ellipse_outline", 483, 207, arcade.color.BLACK, 10)
arcade.draw_ellipse_outline(540, 273, 15, 36, arcade.color.AMBER, 3)
arcade.draw_ellipse_outline(540, 336, 15, 36,
                            arcade.color.BLACK_BEAN, 3, 45)

# Draw a filled ellipse, and another one rotated
arcade.draw_text("draw_ellipse_filled", 3, 3, arcade.color.BLACK, 10)
arcade.draw_ellipse_filled(60, 81, 15, 36, arcade.color.AMBER)
arcade.draw_ellipse_filled(60, 144, 15, 36,
                           arcade.color.BLACK_BEAN, 45)

# Draw an arc, and another one rotated
arcade.draw_text("draw_arc/filled_arc", 123, 3, arcade.color.BLACK, 10)
arcade.draw_arc_outline(150, 81, 15, 36,
                        arcade.color.BRIGHT_MAROON, 90, 360)
arcade.draw_arc_filled(150, 144, 15, 36,
                       arcade.color.BOTTLE_GREEN, 90, 360, 45)

# Draw an rectangle outline
arcade.draw_text("draw_rect", 243, 3, arcade.color.BLACK, 10)
arcade.draw_rect_outline(278, 150, 45, 105,
                         arcade.color.BRITISH_RACING_GREEN, 2)

# Draw a filled in rectangle
arcade.draw_text("draw_filled_rect", 363, 3, arcade.color.BLACK, 10)
arcade.draw_rect_filled(390, 150, 45, 105, arcade.color.BLUSH)

# Load and draw an image to the screen
arcade.draw_text("draw_bitmap", 483, 3, arcade.color.BLACK, 12)
texture = arcade.load_texture("images/playerShip1_orange.png")
scale = .6
arcade.draw_texture_rect(540, 120, scale * texture.width,
                         scale * texture.height, texture, 0)
arcade.draw_texture_rect(540, 60, scale * texture.width,
                         scale * texture.height, texture, 90)

# Finish the render.
# Nothing will be drawn without this.
# Must happen after all draw commands
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
