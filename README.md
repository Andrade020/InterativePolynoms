# Interactive Polynomial Interpolation with tkinter
This program allows users to interactively add points on a canvas and then visualize a polynomial curve that interpolates those points. The main mathematical technique used is the Lagrange Polynomial Interpolation.
# Lagrange Polynomial Interpolation
The concept of Lagrange Interpolation is to find a polynomial that passes through a given set of points. Given n points, there exists a unique polynomial of degree n-1 that passes through these points. The formula for the Lagrange polynomial is implemented as:

L(x) = sum(yi * li(x) for i in range(n))

Where the li(x) function is:
li(x) = product((x - xj) / (xi - xj) for j in range(n) if i != j)
This is implemented in the lagrange_interpolation function.

# Program Structure
# Initialization with tkinter:
The program uses the tkinter module to create a graphical user interface. The canvas allows users to click and add points. Messages and points' coordinates are displayed interactively.

# InteractiveCanvas Class:
This class manages the canvas where the user can add points and view the interpolated polynomial.

# __init__ Method:
Initializes the canvas and sets up interactive messages. Binds mouse events to their respective functions.

# add_point_and_redraw Method:
When the canvas is clicked, this function is triggered. It records the point clicked, plays a sound, and initiates the redraw of the canvas with the updated set of points.

# show_mouse_position Method:
As the mouse hovers over the canvas, this function continuously updates to display the cursor's current position.

# redraw Method: 
This function clears the canvas and then redraws everything – the points, the interpolated polynomial (if applicable), and the axes.

# Usage
Simply run the program and a window will appear. Users can click on the canvas to add points. After adding two or more points, a red polynomial curve will appear, connecting all the points. The curve adjusts dynamically with every new point added.
