import tkinter as tk


def myfunction(event):
    x, y = event.x, event.y
    coordinates.append((x, y))
    if canvas.old_coords:
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1)
    canvas.old_coords = x, y
    if str(event.type) == 'ButtonRelease':
        canvas.old_coords = None

def my_button():
    for val in grid:
        isInBounds(val)

def isInBounds(val):
    for coord in coordinates:
        if coord[0] >= val[0] and coord[0] < val[0] + 10 and coord[1] >= val[1] and coord[1] < val[1] + 10:
            validSquares.add((val[0], val[1]))
            canvas.create_rectangle(val[0], val[1], val[0] + 10, val[1]+10, outline="#000000", fill="#69f420")
            break

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.old_coords = None
coordinates = list()
grid = list()
validSquares = set()
root.bind('<B1-Motion>', myfunction)
root.bind('<ButtonRelease-1>', myfunction)

for x in range(0, 400, 10):
    for y in range(0, 400, 10):
        grid.append((x,y))

print (coordinates)
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame,
                   text="Submit",
                   fg="red",
                   command=my_button)
button.pack(side=tk.LEFT)

root.mainloop()


