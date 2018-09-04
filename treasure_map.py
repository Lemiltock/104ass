#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10163425
#    Student name: Adam.Bretherton
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  TREASURE MAP
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "follow_path".  You are required to
#  complete this function so that when the program is run it traces
#  a path on the screen, drawing "tokens" to indicate discoveries made
#  along the way, while using data stored in a list to determine the
#  steps to be taken.  See the instruction sheet accompanying this
#  file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.

import turtle
import random

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

grid_size = 100 # pixels
num_squares = 7 # to create a 7x7 map grid
margin = 50 # pixels, the size of the margin around the grid
legend_space = 400 # pixels, the space to leave for the legend
window_height = grid_size * num_squares + margin * 2
window_width = grid_size * num_squares + margin +  legend_space
font_size = 18 # size of characters for the coords
starting_points = ['Top left', 'Top right', 'Centre',
                   'Bottom left', 'Bottom right']

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.  (Very keen students are welcome
# to draw their own background, provided they do not change the map's
# grid or affect the ability to see it.)
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():

    # Set up the drawing window with enough space for the grid and
    # legend
    turtle.setup(window_width, window_height)
    turtle.setworldcoordinates(-margin, -margin, window_width - margin,
                        window_height - margin)

    # Draw as quickly as possible
    turtle.tracer(False)

    # Choose a neutral background colour (if you want to draw your
    # own background put the code here, but do not change any of the
    # following code that draws the grid)
    turtle.bgcolor('light grey')

    # Get ready to draw the grid
    turtle.penup()
    turtle.color('slate grey')
    turtle.width(2)

    # Draw the horizontal grid lines
    turtle.setheading(0) # face east
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        turtle.penup()
        turtle.goto(0, y_coord)
        turtle.pendown()
        turtle.forward(num_squares * grid_size)

    # Draw the vertical grid lines
    turtle.setheading(90) # face north
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        turtle.penup()
        turtle.goto(x_coord, 0)
        turtle.pendown()
        turtle.forward(num_squares * grid_size)

    # Draw each of the labels on the x axis
    turtle.penup()
    y_offset = -27 # pixels
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        turtle.goto(x_coord, y_offset)
        turtle.write(str(x_coord), align = 'center',
              font=('Arial', font_size, 'normal'))

    # Draw each of the labels on the y axis
    turtle.penup()
    x_offset, y_offset = -5, -10 # pixels
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        turtle.goto(x_offset, y_coord + y_offset)
        turtle.write(str(y_coord), align = 'right',
              font=('Arial', font_size, 'normal'))

    # Mark the space for drawing the legend
    turtle.goto(750, 700)
    turtle.fillcolor('light blue')
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.width(5)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(700)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(700)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(760, 650)
    turtle.write('     Programming', align = 'left',
          font=('Arial', 24, 'normal'))
    turtle.goto(760, 600)
    turtle.write('       Languages', align = 'left',
          font=('Arial', 24, 'normal'))
    tokens = {'python': python_icon,
              'C': c_icon,
              'C++': c_plusplus_icon,
              'C#': c_sharp_icon,
              'JS': javascript_icon}
    icon_location = [810, 500]
    for name, token in tokens.items():
        turtle.goto(icon_location)
        token()
        turtle.color('slate grey')
        turtle.goto(icon_location[0]+60, icon_location[1]-25)
        turtle.write(name, align = 'left',
          font=('Arial', 24, 'normal'))
        icon_location[1] -= 100

    # Reset everything ready for the student's solution
    turtle.pencolor('black')
    turtle.width(1)
    turtle.penup()
    turtle.home()
    turtle.tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    turtle.tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        turtle.hideturtle()
    turtle.done()

#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the follow_path function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_path function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_path function.
#
# Each of the data sets is a list of instructions expressed as
# triples.  The instructions have two different forms.  The first
# instruction in the data set is always of the form
#
#     ['Start', location, token_number]
#
# where the location may be 'Top left', 'Top right', 'Centre',
# 'Bottom left' or 'Bottom right', and the token_number is an
# integer from 0 to 4, inclusive.  This instruction tells us where
# to begin our treasure hunt and the token that we find there.
# (Every square we visit will yield a token, including the first.)
#
# The remaining instructions, if any, are all of the form
#
#     [direction, number_of_squares, token_number]
#
# where the direction may be 'North', 'South', 'East' or 'West',
# the number_of_squares is a positive integer, and the token_number
# is an integer from 0 to 4, inclusive.  This instruction tells
# us where to go from our current location in the grid and the
# token that we will find in the target square.  See the instructions
# accompanying this file for examples.
#

# Some starting points - the following fixed paths just start a path
# with each of the five tokens in a different location

fixed_path_0 = [['Start', 'Top left', 0]]
fixed_path_1 = [['Start', 'Top right', 1]]
fixed_path_2 = [['Start', 'Centre', 2]]
fixed_path_3 = [['Start', 'Bottom left', 3]]
fixed_path_4 = [['Start', 'Bottom right', 4]]

# Some miscellaneous paths which encounter all five tokens once

fixed_path_5 = [['Start', 'Top left', 0], ['East', 1, 1], ['East', 1, 2],
                ['East', 1, 3], ['East', 1, 4]]
fixed_path_6 = [['Start', 'Bottom right', 0], ['West', 1, 1], ['West', 1, 2],
                ['West', 1, 3], ['West', 1, 4]]
fixed_path_7 = [['Start', 'Centre', 4], ['North', 2, 3], ['East', 2, 2],
                ['South', 4, 1], ['West', 2, 0]]

# A path which finds each token twice

fixed_path_8 = [['Start', 'Bottom left', 1], ['East', 5, 2],
                ['North', 2, 3], ['North', 4, 0], ['South', 3, 2],
                ['West', 4, 0], ['West', 1, 4],
                ['East', 3, 1], ['South', 3, 4], ['East', 1, 3]]

# Some short paths

fixed_path_9 = [['Start', 'Centre', 0], ['East', 3, 2],
                ['North', 2, 1], ['West', 2, 3],
                ['South', 3, 4], ['West', 4, 1]]

fixed_path_10 = [['Start', 'Top left', 2], ['East', 6, 3], ['South', 1, 0],
                 ['South', 1, 0], ['West', 6, 2], ['South', 4, 3]]

fixed_path_11 = [['Start', 'Top left', 2], ['South', 1, 0], ['East', 2, 4],
                 ['South', 1, 1], ['East', 3, 4], ['West', 1, 3],
                 ['South', 2, 0]]

# Some long paths

fixed_path_12 = [['Start', 'Top right', 2], ['South', 4, 0],
                 ['South', 1, 1], ['North', 3, 4], ['West', 4, 0],
                 ['West', 2, 0], ['South', 3, 4], ['East', 2, 3],
                 ['East', 1, 1], ['North', 3, 2], ['South', 1, 3],
                 ['North', 3, 2], ['West', 1, 2], ['South', 3, 4],
                 ['East', 3, 0], ['South', 1, 1]]

fixed_path_13 = [['Start', 'Top left', 1], ['East', 5, 3], ['West', 4, 2],
                 ['East', 1, 3], ['East', 2, 2], ['South', 5, 1],
                 ['North', 2, 0], ['East', 2, 0], ['West', 1, 1],
                 ['West', 5, 0], ['South', 1, 3], ['East', 3, 0],
                 ['East', 1, 4], ['North', 3, 0], ['West', 1, 4],
                 ['West', 3, 1], ['South', 4, 1], ['East', 5, 1],
                 ['West', 4, 0]]

# "I've been everywhere, man!" - this path visits every square in
# the grid, with randomised choices of tokens

fixed_path_99 = [['Start', 'Top left', random.randint(0, 4)]] + \
                [['East', 1, random.randint(0, 4)] for step in range(6)] + \
                [['South', 1, random.randint(0, 4)]] + \
                [['West', 1, random.randint(0, 4)] for step in range(6)] + \
                [['South', 1, random.randint(0, 4)]] + \
                [['East', 1, random.randint(0, 4)] for step in range(6)] + \
                [['South', 1, random.randint(0, 4)]] + \
                [['West', 1, random.randint(0, 4)] for step in range(6)] + \
                [['South', 1, random.randint(0, 4)]] + \
                [['East', 1, random.randint(0, 4)] for step in range(6)] + \
                [['South', 1, random.randint(0, 4)]] + \
                [['West', 1, random.randint(0, 4)] for step in range(6)] + \
                [['South', 1, random.randint(0, 4)]] + \
                [['East', 1, random.randint(0, 4)] for step in range(6)]

# If you want to create your own test data sets put them here

#
#--------------------------------------------------------------------#


#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a path
# to follow.  Your program must work for any data set that can be
# returned by this function.  The results returned by calling this
# function will be used as the argument to your follow_path function
# during marking.  For convenience during code development and
# marking this function also prints the path to be followed to the
# shell window.
#
# Note: For brevity this function uses some Python features not taught
# in IFB104 (dictionaries and list generators).  You do not need to
# understand this code to complete the assignment.
#
def random_path(print_path = True):
    # Select one of the five starting points, with a random token
    path = [['Start', random.choice(starting_points), random.randint(0, 4)]]
    # Determine our location in grid coords (assuming num_squares is odd)
    start_coords = {'Top left': [0, num_squares - 1],
                    'Bottom left': [0, 0],
                    'Top right': [num_squares - 1, num_squares - 1],
                    'Centre': [num_squares // 2, num_squares // 2],
                    'Bottom right': [num_squares - 1, 0]}
    location = start_coords[path[0][1]]
    # Keep track of squares visited
    been_there = [location]
    # Create a path up to 19 steps long (so at most there will be 20 tokens)
    for step in range(random.randint(0, 19)):
        # Find places to go in each possible direction, calculating both
        # the new grid square and the instruction required to take
        # us there
        go_north = [[[location[0], new_square],
                     ['North', new_square - location[1], token]]
                    for new_square in range(location[1] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_south = [[[location[0], new_square],
                     ['South', location[1] - new_square, token]]
                    for new_square in range(0, location[1])
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_west = [[[new_square, location[1]],
                    ['West', location[0] - new_square, token]]
                    for new_square in range(0, location[0])
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        go_east = [[[new_square, location[1]],
                    ['East', new_square - location[0], token]]
                    for new_square in range(location[0] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        # Choose a free square to go to, if any exist
        options = go_north + go_south + go_east + go_west
        if options == []: # nowhere left to go, so stop!
            break
        target_coord, instruction = random.choice(options)
        # Remember being there
        been_there.append(target_coord)
        location = target_coord
        # Add the move to the list of instructions
        path.append(instruction)
    # To assist with debugging and marking, print the list of
    # instructions to be followed to the shell window
    print('Welcome to the Treasure Hunt!')
    print('Here are the steps you must follow...')
    for instruction in path:
        print(instruction)
    # Return the random path
    return path

#
#--------------------------------------------------------------------#

'''
Token functions
The below functions are for drawing the individual function,
or any healper function used by the token functions
'''
def python_icon(coord='loc', heading=180):
    '''
    coord: list of two elements, x and y
    draws a 100x100 image of the python icon centered on x, y
    Heading variable is just to cover for future rotation if required
    Uses turtles current position unless otherwise set
    '''
    if coord == 'loc':
        coord = turtle.pos()
    home = coord
    turtle.penup()
    colours = ['yellow', 'blue']
    turtle.pencolor('white')
    turtle.width(1)
    turtle.goto(coord)
    #draw half of icon the swap colours and rotate
    for colour in colours:
        turtle.pendown
        turtle.setheading(heading)
        turtle.fillcolor(colour)
        turtle.begin_fill()
        turtle.forward(16)
        turtle.circle(10, extent=90)
        turtle.forward(33)
        turtle.setheading(heading+150)
        turtle.circle(50, extent=60)
        turtle.setheading(heading-90)
        turtle.forward(11)
        turtle.left(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(1)
        turtle.right(90)
        turtle.forward(43)
        turtle.setheading(heading-120)
        turtle.circle(50, extent=60)
        turtle.setheading(heading)
        turtle.forward(15)
        turtle.left(90)
        turtle.forward(10)
        turtle.circle(-10, extent=90)
        turtle.forward(14)
        turtle.end_fill()
        turtle.penup()
        turtle.setheading(heading+112)
        turtle.forward(40)
        turtle.dot(5)
        turtle.goto(coord)
        heading += 180
    turtle.goto(home)

def hexagon(coord, colours, heading=210):
    '''
    coord: list of two elements, x and y
    colours: list of two elements, top colour, botom color
    draws a 100x100 image of a hexagon (two colour) icon centered on x, y
    Heading variable is just to cover for future rotation if required
    '''
    turtle.speed('fastest')
    turtle.penup()
    turtle.pencolor('black')
    turtle.width(1)
    side_length = 50
    ext_vertex = 120
    turtle.goto(coord)
    #draw a a triangle, repeat 3 times then rotate swap colours and complete
    for colour in colours:
        turtle.fillcolor(colour)
        for triangle in range(3):
            turtle.setheading(heading)
            turtle.begin_fill()
            for side in range(3):
                turtle.forward(side_length)
                turtle.right(ext_vertex)
            turtle.end_fill()
            heading -= 60

def letter_c(coord, heading=30):
    '''
    coord: list of two elements, x and y
    draws a white C centered in a 100x100 image
    Heading variable is just to cover for future rotation if required
    '''
    turtle.speed('fastest')
    turtle.penup()
    turtle.pencolor('white')
    turtle.fillcolor('white')
    turtle.width(1)
    width = 15
    centre = 15
    turtle.goto(coord)
    turtle.setheading(heading)
    turtle.forward(centre)
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.circle(centre+width, extent=300)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.circle(-centre, extent=300)
    turtle.end_fill()
    turtle.penup()

def plus_icon(coord, heading=0):
    '''
    coord: list of two elements, x and y
    draws a white + starting at top left point
    Heading variable is just to cover for future rotation if required
    '''
    turtle.speed('fastest')
    turtle.penup()
    turtle.pencolor('white')
    turtle.fillcolor('white')
    turtle.width(1)
    width = 10
    turtle.goto(coord)
    turtle.setheading(heading)
    turtle.begin_fill()
    for side in range(12):
        turtle.forward(width/3)
        if side%3 == 0:
            turtle.left(90)
        else:
            turtle.right(90)
    turtle.end_fill()

def hash_icon(coord, heading=0):
    '''
    coord: list of two elements, x and y
    draws a white # starting at top left point
    Heading variable is just to cover for future rotation if required
    '''
    turtle.speed('fastest')
    turtle.penup()
    turtle.pencolor('white')
    turtle.fillcolor('white')
    width = 5
    side = 2*width+(3*(width/2))
    turtle.width(width)
    turtle.goto(coord)
    for half in range(2):
        turtle.setheading(heading)
        turtle.pendown()
        turtle.forward(side)
        turtle.penup()
        turtle.right(90)
        turtle.forward(width*1.5)
        turtle.right(90)
        turtle.pendown()
        turtle.forward(side)
        turtle.penup()
        heading += 90
        turtle.goto(coord[0] + width, coord[1] - (5 * (width/2)))

def c_icon(coord='loc', heading=0):
    '''
    coord: list of two elements, x and y
    draws the C programming icon centered on coord
    Heading variable is just to cover for future rotation if required
    Uses turtles current position unless otherwise set
    '''
    if coord == 'loc':
        coord = turtle.pos()
    home = coord
    colours = ['grey', 'silver']
    hexagon(coord, colours)
    letter_c(coord)
    turtle.goto(home)

def c_plusplus_icon(coord='loc', heading=0):
    '''
    coord: list of two elements, x and y
    draws the C programming icon centered on coord
    Heading variable is just to cover for future rotation if required
    Uses turtles current position unless otherwise set
    '''
    if coord == 'loc':
        coord = turtle.pos()
    home = coord
    colours = ['royal blue', 'blue']
    hexagon(coord, colours)
    letter_c(coord)
    plus_icon([coord[0] + 18, coord[1]])
    plus_icon([coord[0] + 30, coord[1]])
    turtle.goto(home)

def c_sharp_icon(coord='loc', heading=0):
    '''
    coord: list of two elements, x and y
    draws the C programming icon centered on coord
    Heading variable is just to cover for future rotation if required
    Uses turtles current position unless otherwise set
    '''
    if coord == 'loc':
        coord = turtle.pos()
    home = coord
    colours = ['dark orchid', 'purple']
    hexagon(coord, colours)
    letter_c(coord)
    hash_icon([coord[0] + 22, coord[1] + 3])
    turtle.goto(home)

def javascript_icon(coord='loc', heading=0):
    '''
    coord: list of two elements, x and y
    draws the javascript programming icon centered on coord
    Heading variable is just to cover for future rotation if required
    Uses turtles current position unless otherwise set
    '''
    if coord == 'loc':
        coord = turtle.pos()
    home = coord
    turtle.width(2)
    turtle.penup()
    turtle.pencolor('black')
    turtle.fillcolor('yellow')
    width = 100
    turtle.setheading(heading)
    turtle.goto(coord)
    #Draw background
    turtle.pendown()
    turtle.forward(width/2)
    turtle.left(90)
    turtle.forward(width/2)
    turtle.begin_fill()
    for side in range(4):
        turtle.left(90)
        turtle.forward(width)
    turtle.end_fill()
    turtle.penup()
    #Draw letters
    turtle.pencolor('black')
    turtle.width(15)
    turtle.goto(coord)
    heading -= 90
    turtle.setheading(heading)
    # Draw J
    turtle.pendown()
    turtle.forward((3*width) / 10)
    turtle.circle(-10, extent=180)
    turtle.penup()
    # Draw S
    turtle.goto(coord[0] + 40, coord[1] - 5)
    turtle.setheading(heading)
    turtle.right(135)
    turtle.pendown()
    turtle.circle(10, extent=210)
    turtle.circle(-10, extent=210)
    turtle.penup()
    turtle.goto(home)

#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "follow_path" function.
#

# Follow the path as per the provided dataset
def follow_path(path):
    #create constant for start locations, offset by 50 on both x and y for center of grid
    locations = {'Bottom left': [50, 50],
                 'Bottom right': [650, 50],
                 'Top left': [50, 650],
                 'Top right': [650, 650],
                 'Centre': [350, 350]}
    headings = {'East': 0,
                'West': 180,
                'North': 90,
                'South': 270}
    tokens = {0: python_icon,
              1: c_icon,
              2: c_plusplus_icon,
              3: c_sharp_icon,
              4: javascript_icon}
    for step in path:
        if step[0] == 'Start':
            turtle.goto(locations[step[1]])
            tokens[step[2]]()
        else:
            turtle.setheading(headings[step[0]])
            turtle.forward(step[1]*100)
            tokens[step[2]]()
            '''
    turtle.goto([50, 50])
    turtle.dot(50)
    tokens[0]()
    turtle.goto([650, 50])
    turtle.dot(50)
    tokens[1]()
    turtle.goto([350, 350])
    turtle.dot(50)
    tokens[2]()
    turtle.goto([50, 650])
    turtle.dot(50)
    tokens[3]()
    turtle.goto([650, 650])
    turtle.dot(50)
    tokens[4]()
    '''
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
turtle.speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves around the screen
turtle.tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its tokens
turtle.title("Programming Languages [Python, C, C++, C#, JS]")

### Call the student's function to follow the path
### ***** While developing your program you can call the follow_path
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_path()" as the
### ***** argument to the follow_path function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_path function.
# follow_path(fixed_path_0) # <-- used for code development only, not marking
follow_path(random_path()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
