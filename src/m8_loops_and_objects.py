"""
This module demonstrates simple LOOPS of the form:
   for k in range(blah):
      ... k ...

and also USING OBJECTS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Colton McKay.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math
window = rg.RoseWindow(400, 400)
window1 = rg.RoseWindow(400, 400)
window2 = rg.RoseWindow(300, 300)
window3 = rg.RoseWindow(400,400)

def main():
    test_print_sequence1()
    test_draw_circles1()
    test_print_sequence2()
    test_draw_circles2()
    test_print_sequence3()
    test_draw_circles3()
    test_print_cosines()
    test_draw_cosine_and_sines()
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:

def test_print_sequence1():
    print()
    print('--------------------------------------------------')
    print('testing print_sequence1:')
    print('--------------------------------------------------')


    # Test 1:
    expected = 0, 10, 20, 30, 40
    answer = print_sequence1(5)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # Test 2:
    expected = 0, 10
    answer = print_sequence1(2)
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    # Test 3:
    expected = 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140
    answer = print_sequence1(15)
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

def print_sequence1(n):
    """
    Prints:
       0
       10
       20
       30
       40
       ...
       200
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence1:')
    print('--------------------------------------------------')

    for k in range(n):
        print(k*10)
        answer =(k*10)
    return answer

def test_draw_circles1():
    print()
    print('--------------------------------------------------')
    print('testing draw_cicrcles:')
    print('--------------------------------------------------')

    # Test 1:
    print('radii should be up to 200, and there should be 20 circles and 1 point')
    draw_circles1(21)


def draw_circles1(n):
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws 21 rg.Circle objects such that:
         -- Each is centered at (200, 200)
         -- They have radii:  0  10  20  30  40 ... 200, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # HINT: You might find a prior module useful when 'writing' this code.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles1:  See graphics window')
    print('--------------------------------------------------')


    for k in range(n):
        center = rg.Point(200,200)
        circles = rg.Circle(center,k*10)
        circles.attach_to(window)
    window.render()

def test_print_sequence2():
    print()
    print('--------------------------------------------------')
    print('testing print_sequence2:')
    print('--------------------------------------------------')


    # Test 1:
    expected = 'expect from 50 to 390 increasing by 20 each time'
    print(expected)
    answer = print_sequence2(18)

def print_sequence2(n):
    """
    Prints:
      50
      70
      90
      110
      130
      ...
      390.
    """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence2:')
    print('--------------------------------------------------')

    for k in range(n):
        print(50+(20*k))
        answer =(50+(20*k))
    return answer

def test_draw_circles2():
    print()
    print('--------------------------------------------------')
    print('testing draw_cicrcles2:')
    print('--------------------------------------------------')

    # Test 1:
    print('')
    draw_circles2(18)

def draw_circles2(n):
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- Each has fill_color 'blue'.
         -- They are centered at, respectively:
               (50, 100)   (70, 100)   (90, 100)  (110, 100) ... (390, 100)
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 5. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles2:  See graphics window')
    print('--------------------------------------------------')

    for k in range(n):
        center = rg.Point(((50)+20*k),100)
        radius = 10
        circles = rg.Circle(center,radius)
        circles.fill_color = 'blue'
        circles.attach_to(window1)
    window1.render()

def test_print_sequence3():
    print()
    print('--------------------------------------------------')
    print('testing print_sequence1:')
    print('--------------------------------------------------')


    # Test 1:
    expected = '1 to 100'
    answer = print_sequence3(100)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

def print_sequence3(n):
    """
    Prints:
      1
      2
      3 
      4
      ...
      100.
    """
    # -------------------------------------------------------------------------
    # DONE: 6. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence3:')
    print('--------------------------------------------------')

    for k in range(n):
        print(k+1)
    return

def test_draw_circles3():
    print()
    print('--------------------------------------------------')
    print('testing draw_cicrcles3:')
    print('--------------------------------------------------')

    # Test 1:
    print(' circles with radius 1 to 100')
    draw_circles3(100)

def draw_circles3(n):
    """
    -- Constructs an rg.RoseWindow whose width and height are both 300.
    -- Constructs and draws 100 rg.Circle objects such that:
         -- Each is centered at (200, 150)
         -- They have radii:  1  2  3  4  ... 100, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 7. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles3:  See graphics window')
    print('--------------------------------------------------')

    for k in range(n):
        center = rg.Point(200,150)
        radius = (k+1)
        circles = rg.Circle(center,radius)
        circles.attach_to(window2)
    window2.render()

def test_print_cosines():
    print()
    print('--------------------------------------------------')
    print('testing print_cosines:')
    print('--------------------------------------------------')

    # Test 1:
    print(' values of 80*cosine from 0 to 100')
    print_cosines(101)

def print_cosines(n):
    """
    For each of the integers 0  1  2  ... 100,
    prints 80 times the cosine of that integer.
    Thus, the numbers printed should be about:
       80.0
       43.224184469451174
       -33.29174692377139
       -79.19939972803563
       -52.29148966908895
       22.6929748370581
       76.81362293202928
       60.31218034746437
         ...
       -65.54305962331674
       3.185670431451112
       68.9855097830147
    """
    # -------------------------------------------------------------------------
    # DONE: 8. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    #
    # HINT: You need to   import math   at the top of this file
    #       to use math functions like the ones for cosine and sine.
    #       Once you have that import in place, typing
    #            math.
    #       (note the DOT) and pausing will display options that make
    #       it plain what the notation for the cosine function is.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_cosines:')
    print('--------------------------------------------------')

    for k in range(n):
        print(80*math.cos(k))


def test_draw_cosine_and_sines():
    print()
    print('--------------------------------------------------')
    print('testing draw_cosines_and_sines:')
    print('--------------------------------------------------')

    # Test 1:
    print('circles, with varying center positons')
    draw_cosines_and_sines(101)

def draw_cosines_and_sines(n):
    """
    -- Constructs a window whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- They are centered at, respectively:
               ( 200 + (80 * cos(0)), 200 + (80 * sin(0) )
               ( 200 + (80 * cos(1)), 200 + (80 * sin(1) )
               ( 200 + (80 * cos(2)), 200 + (80 * sin(2) )
               ( 200 + (80 * cos(3)), 200 + (80 * sin(3) )
                   ...
               ( 200 + (80 * cos(100)), 200 + (80 * sin(100) )
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 9. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_cosines_and_sines:  See graphics window')
    print('--------------------------------------------------')

    for k in range(n):
        center = rg.Point(200+((80*math.cos(k))),200+(80*math.sin(k)))
        radius = 10
        circles = rg.Circle(center,radius)
        circles.attach_to(window3)
    window3.render()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------

main()
window.close_on_mouse_click()
window1.close_on_mouse_click()
window2.close_on_mouse_click()
window3.close_on_mouse_click()