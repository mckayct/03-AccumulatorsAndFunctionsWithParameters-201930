"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Colton McKay.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
window = rg.RoseWindow(300,300)
window1 = rg.RoseWindow(400, 400)
window2 = rg.RoseWindow(400,400)


def main():
    two_circles(rg.Point(100,100),15,rg.Point(100,100),25)
    circle_and_rectangle(100,100,25,100,100,300,300)
    lines(rg.Point(100,100),rg.Point(200,200), rg.Point(100,300),rg.Point(-200,300),8)
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:


def two_circles(point,radius,point1,radius1):
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------


    circle1 = rg.Circle(point,radius)
    circle1.fill_color = "midnight blue"
    circle2 = rg.Circle(point1,radius1)
    circle1.attach_to(window)
    circle2.attach_to(window)
    window.render()
    return



def circle_and_rectangle(center_x,center_y,radius,rectangle_corner1_x,rectangle_corner1_y,rectangle_corner2_x,rectangle_corner2_y ):

    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    print('CIRCLE Parts')

    circle = rg.Circle(rg.Point(center_x,center_y),radius)
    circle.fill_color = ('blue')
    circle.attach_to(window1)
    print(circle.center)
    print(center_x)
    print(center_y)
    print('blue')
    circle.outline_thickness = 1
    print(circle.outline_thickness)

    print('RECTANGLE Parts')
    rectangle_corner1 = rg.Point(rectangle_corner1_x, rectangle_corner1_y)
    rectangle_corner2 = rg.Point(rectangle_corner2_x, rectangle_corner2_y)

    rectangle = rg.Rectangle(rectangle_corner1, rectangle_corner2)
    rectangle.attach_to(window1)
    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print(rectangle.get_center())
    print(rectangle.get_center().x)
    print(rectangle.get_center().y)


    window1.render()
    return




def lines(start1,end1,start2,end2, thickness2):
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # DONE: 4. Implement and test this function.

    line1 = rg.Line(start1,end1)
    line2 = rg.Line(start2,end2)
    line1.attach_to(window2)
    line2.attach_to(window2)
    line2.thickness = thickness2

    print('LINE Parts')
    print(line2.get_midpoint())
    print(line2.get_midpoint().x)
    print(line2.get_midpoint().y)

    window2.render()
    return
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()

window2.close_on_mouse_click()
window1.close_on_mouse_click()
window.close_on_mouse_click()