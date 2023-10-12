import tkinter as tk
import random
import winsound  # For sound effect on Windows

def lagrange_interpolation(points, x):
    """
    This function performs Lagrange polynomial interpolation.
    It returns the y value corresponding to a given x using the provided points.
    """
    total_sum = 0
    n = len(points)
    
    # Iterate through all provided points
    for i in range(n):
        xi, yi = points[i]
        term = yi
        for j in range(n):
            if i != j:
                xj, _ = points[j]
                # Calculate the term of the Lagrange formula
                term = term * (x - xj) / (xi - xj)
        total_sum += term

    return total_sum

class InteractiveCanvas:
    """
    This class manages the interactive canvas where points can be added and the graph is drawn.
    """
    def __init__(self, root):
        self.canvas = tk.Canvas(root, bg="white", width=400, height=400)
        self.canvas.pack(pady=20)
        
        # Initial message "Click to add"
        self.start_message = self.canvas.create_text(200, 200, text="Click to add", font=("Arial", 14))
        
        # Author's name
        self.author_message = self.canvas.create_text(350, 385, text="by Lucas Rafael", anchor="e")

        # Bind mouse events to corresponding functions
        self.canvas.bind("<Button-1>", self.add_point_and_redraw)
        self.canvas.bind("<Motion>", self.show_mouse_position)
        
        # List to store added points
        self.points = []

    def add_point_and_redraw(self, event):
        """
        This function is called when you click on the canvas to add a point.
        It updates the points list and redraws the canvas.
        """
        # Play a sound effect when adding a point
        winsound.Beep(500, 150)
        x, y = event.x, event.y
        self.points.append((x, y))
        
        # Remove the "Click to add" message after the first click
        if len(self.points) == 1:
            self.canvas.delete(self.start_message)

        # Change the color of the "by Lucas Rafael" message with each click
        random_color = '#%06X' % random.randint(0, 0xFFFFFF)
        self.canvas.itemconfig(self.author_message, fill=random_color)
        
        self.redraw()

    def show_mouse_position(self, event):
        """
        This function is called whenever the mouse moves over the canvas.
        It shows the current mouse position on the canvas.
        """
        x, y = event.x, event.y
        # Delete the last shown cursor position
        self.canvas.delete("cursor_position")
        # Display the new cursor position
        self.canvas.create_text(x + 10, y, text=f"({x-200}, {200-y})", anchor="w", tags="cursor_position")

    def redraw(self):
        """
        This function is called every time a new point is added to redraw the graph.
        """
        # Delete specific items in preparation for new drawing
        self.canvas.delete("lines", "points", "cursor_position")

        # Draw the graph axes
        self.canvas.create_line(0, 200, 400, 200, arrow=tk.LAST, tags="lines")
        self.canvas.create_line(200, 0, 200, 400, arrow=tk.LAST, tags="lines")

        # Draw the points that were interactively added
        for x, y in self.points:
            self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="blue", tags="points")
            self.canvas.create_text(x + 10, y - 10, text=f"({x-200}, {200-y})", anchor="w", tags="points")

        # If more than one point exists, draw the interpolated graph
        if len(self.points) > 1:
            for x in range(0, 400):
                y1 = lagrange_interpolation(self.points, x)
                y2 = lagrange_interpolation(self.points, x+1)
                self.canvas.create_line(x, y1, x+1, y2, fill="red", tags="lines")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Interactive Graph with Polynomial Interpolation")
    app = InteractiveCanvas(root)
    root.mainloop()
