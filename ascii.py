import tkinter as tk


def draw(event):
    x, y = event.x, event.y
    coordinates.append((x, y))
    if canvas.old_coords:
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1)
    canvas.old_coords = x, y
    if str(event.type) == 'ButtonRelease':
        canvas.old_coords = None

def my_button():
    f = open("output.txt","w+")
    f.write('..')
    for val in grid:
        isInBounds(val)
        if val[0] % canvasSize - res == 0 and val[0] != 0:
            f.write('\n')
        if(val in validSquares):
            f.write('#.')
            print (val)
        else:
            f.write('..')
    f.close()

def isInBounds(val):
    for coord in coordinates:
        if coord[0] >= val[0] and coord[0] < val[0] + res and coord[1] >= val[1] and coord[1] < val[1] + res:
            validSquares.add((val[0], val[1]))
            canvas.create_rectangle(val[0], val[1], val[0] + res, val[1]+res, outline="#000000", fill="#69f420")
            break

res = 10
canvasSize = 400
root = tk.Tk()
canvas = tk.Canvas(root, width=canvasSize, height=canvasSize)
canvas.pack()
canvas.old_coords = None
coordinates = list()
grid = list()
validSquares = set()
root.bind('<B1-Motion>', draw)
root.bind('<ButtonRelease-1>', draw)

for x in range(0, canvasSize, res):
    for y in range(0, canvasSize, res):
        grid.append((y,x))

frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame,
                   text="Submit",
                   fg="red",
                   command=my_button)
button.pack(side=tk.LEFT)

root.mainloop()


