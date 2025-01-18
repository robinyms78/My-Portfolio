from Tkinter import *
import Tkinter as tk
import tkMessageBox

def sel():
    selection = "You selected student " + str(var.get())
    label.config(text = selection)

# Create the root window
root = tk.Tk()

# Title
root.title("Pepper Navigation Program")

# Set the root window's height, width and x, y position
# x and y are the coordinates of the upper left corner
w = 1375
h = 800
x = 0
y = 0

# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# Use a white frame
frame = tk.Canvas(root, bg ="white")
frame.pack(fill = "both", expand = "yes")

# Classroom
oval = frame.create_polygon(5, 5, 1375, 5, 1375, 800, 5, 800, fill = "green") 
line = frame.create_line(5, 5, 1375, 5, 1375, 800, 5, 800, 5, 5, width = 2) 

# Side table 1
oval = frame.create_polygon(945, 5, 1375, 5, 1375, 60, 945, 60, fill = "blue") 
line = frame.create_line(945, 5, 1375, 5, 1375, 60, 945, 60, 945, 5, width = 2) 

# Side table 2
oval = frame.create_polygon(1025, 740, 1375, 740, 1375, 800, 1025, 800, fill = "blue") 
line = frame.create_line(1025, 740, 1375, 740, 1375, 800, 1025, 800, 1025, 740, width = 2) 

# Side storeroom
oval = frame.create_polygon(775, 5, 945, 5, 945, 90, 775, 90, fill = "blue")
line = frame.create_line(775, 5, 945, 5, 945, 90, 775, 90, 775, 5, width = 2)

# First table
oval = frame.create_polygon(105, 200, 195, 200, 195, 500, 105, 500, fill = "blue")
line = frame.create_line(105, 200, 195, 200, 195, 500, 105, 500, 105, 200, width = 2)
label = tk.Label(frame, text = "Table 1", justify = CENTER)
label.place(x = 125, y = 330)

# Second table
oval = frame.create_polygon(355, 200, 445, 200, 445, 500, 355, 500, fill = "blue")
line = frame.create_line(355, 200, 445, 200, 445, 500, 355, 500, 355, 200,  width = 2)
label = tk.Label(frame, text = "Table 2", justify = CENTER)
label.place(x = 375, y = 330)

# Third table
oval = frame.create_polygon(605, 200, 695, 200, 695, 500, 605, 500, fill = "blue")
line = frame.create_line(605, 200, 695, 200, 695, 500, 605, 500, 605, 200, width = 2)
label = tk.Label(frame, text = "Table 3", justify = CENTER)
label.place(x = 625, y = 330)

# Fourth table
oval = frame.create_polygon(855, 200, 945, 200, 945, 500, 855, 500, fill = "blue")
line = frame.create_line(855, 200, 945, 200, 945, 500, 855, 500, 855, 200, width = 2)
label = tk.Label(frame, text = "Table 4", justify = CENTER)
label.place(x = 875, y = 330)

# Fifth table
oval = frame.create_polygon(1105, 200, 1195, 200, 1195, 500, 1105, 500, fill = "blue")
line = frame.create_line(1105, 200, 1195, 200, 1195, 500, 1105, 500, 1105, 200, width = 2)
label = tk.Label(frame, text = "Table 5", justify = CENTER)
label.place(x = 1125, y = 330)

# Teacher's table
oval = frame.create_polygon(535, 590, 835, 590, 835, 680, 535, 680, fill = "blue")
line = frame.create_line(535, 590, 835, 590, 835, 680, 535, 680, 535, 590, width = 2)
label = tk.Label(frame, text = "Table 6", justify = CENTER)
label.place(x = 655, y = 625)

# Small table
oval = frame.create_polygon(360, 140, 440, 140, 460, 200, 340, 200, fill = "blue")  
line = frame.create_line(360, 140, 440, 140, 460, 200, 340, 200, 360, 140, width = 2)

# Chair 1
oval = frame.create_polygon(330, 435, 350, 435, 350, 455, 330, 455, fill = "red")
line = frame.create_line(330, 435, 350, 435, 350, 455, 330, 455, 330, 435, width = 2)
line = frame.create_line(330, 435, 350, 455, width = 2)
line = frame.create_line(350, 435, 330, 455, width = 2)
label = tk.Label(frame, text = "1", width = 2, justify = CENTER)
label.place(x = 330, y = 460)

# Chair 2
oval = frame.create_polygon(330, 380, 350, 380, 350, 400, 330, 400, fill = "red")
line = frame.create_line(330, 380, 350, 380, 350, 400, 330, 400, 330, 380, width = 2)
line = frame.create_line(330, 380, 350, 400, width = 2)
line = frame.create_line(350, 380, 330, 400, width = 2)
label = tk.Label(frame, text = "2", width = 2, justify = CENTER)
label.place(x = 330, y = 405)

# Chair 3
oval = frame.create_polygon(330, 290, 350, 290, 350, 310, 330, 310, fill = "red")
line = frame.create_line(330, 290, 350, 290, 350, 310, 330, 310, 330, 290, width = 2)
line = frame.create_line(330, 290, 350, 310, width = 2)
line = frame.create_line(350, 290, 330, 310, width = 2)
label = tk.Label(frame, text = "3", width = 2, justify = CENTER)
label.place(x = 330, y = 315)

# Chair 4
oval = frame.create_polygon(330, 235, 350, 235, 350, 255, 330, 255, fill = "red")
line = frame.create_line(330, 235, 350, 235, 350, 255, 330, 255, 330, 235, width = 2)
line = frame.create_line(330, 235, 350, 255, width = 2)
line = frame.create_line(350, 235, 330, 255, width = 2)
label = tk.Label(frame, text = "4", width = 2, justify = CENTER)
label.place(x = 330, y = 260)

# Chair 5
oval = frame.create_polygon(360, 110, 380, 110, 380, 130, 360, 130, fill = "red")
line = frame.create_line(360, 110, 380, 110, 380, 130, 360, 130, 360, 110, width = 2)
line = frame.create_line(360, 110, 380, 130, width = 2)
line = frame.create_line(380, 110, 360, 130, width = 2)
label = tk.Label(frame, text = "5", width = 2, justify = CENTER)
label.place(x = 335, y = 110)

# Chair 6
oval = frame.create_polygon(420, 110, 440, 110, 440, 130, 420, 130, fill = "red")
line = frame.create_line(420, 110, 440, 110, 440, 130, 420, 130, 420, 110, width = 2)
line = frame.create_line(420, 110, 440, 130, width = 2)
line = frame.create_line(440, 110, 420, 130, width = 2)
label = tk.Label(frame, text = "6", width = 2, justify = CENTER)
label.place(x = 395, y = 110)

# Chair 7
oval = frame.create_polygon(450, 235, 470, 235, 470, 255, 450, 255, fill = "red")
line = frame.create_line(450, 235, 470, 235, 470, 255, 450, 255, 450, 235, width = 2)
line = frame.create_line(450, 235, 470, 255, width = 2)
line = frame.create_line(470, 235, 450, 255, width = 2)
label = tk.Label(frame, text = "7", width = 2, justify = CENTER)
label.place(x = 450, y = 260)

# Chair 8
oval = frame.create_polygon(450, 290, 470, 290, 470, 310, 450, 310, fill = "red")
line = frame.create_line(450, 290, 470, 290, 470, 310, 450, 310, 450, 290, width = 2)
line = frame.create_line(450, 290, 470, 310, width = 2)
line = frame.create_line(470, 290, 450, 310, width = 2)
label = tk.Label(frame, text = "8", width = 2, justify = CENTER)
label.place(x = 450, y = 315)

# Chair 9
oval = frame.create_polygon(450, 380, 470, 380, 470, 400, 450, 400, fill = "red")
line = frame.create_line(450, 380, 470, 380, 470, 400, 450, 400, 450, 380, width = 2)
line = frame.create_line(450, 380, 470, 400, width = 2)
line = frame.create_line(470, 380, 450, 400, width = 2)
label = tk.Label(frame, text = "9", width = 2, justify = CENTER)
label.place(x = 450, y = 405)

# Chair 10
oval = frame.create_polygon(450, 435, 470, 435, 470, 455, 450, 455, fill = "red")
line = frame.create_line(450, 435, 470, 435, 470, 455, 450, 455, 450, 435, width = 2)
line = frame.create_line(450, 435, 470, 455, width = 2)
line = frame.create_line(470, 435, 450, 455, width = 2)
label = tk.Label(frame, text = "10", width = 2, justify = CENTER)
label.place(x = 450, y = 460)

# Screen
oval = frame.create_polygon(240, 630, 535, 630, 535, 645, 240, 645, fill = "black")
label = tk.Label(frame, text = "Screen", justify = CENTER)
label.place(x = 370, y = 655)

# Radiobutton
var = IntVar()
R1 = Radiobutton(root, text = "Student 1", variable = var, value = 1, command = sel)
R1.place(x = 1380, y = 0)

R2 = Radiobutton(root, text = "Student 2", variable = var, value = 2, command = sel)
R2.place(x = 1380, y = 20)

R3 = Radiobutton(root, text = "Student 3", variable = var, value = 3, command = sel)
R3.place(x = 1380, y = 40)

R4 = Radiobutton(root, text = "Student 4", variable = var, value = 4, command = sel)
R4.place(x = 1380, y = 60)

R5 = Radiobutton(root, text = "Student 5", variable = var, value = 5, command = sel)
R5.place(x = 1380, y = 80)

R6 = Radiobutton(root, text = "Student 6", variable = var, value = 6, command = sel)
R6.place(x = 1380, y = 100)

R7 = Radiobutton(root, text = "Student 7", variable = var, value = 7, command = sel)
R7.place(x = 1380, y = 120)

R8 = Radiobutton(root, text = "Student 8", variable = var, value = 8, command = sel)
R8.place(x = 1380, y = 140)

R9 = Radiobutton(root, text = "Student 9", variable = var, value = 9, command = sel)
R9.place(x = 1380, y = 160)

R10 = Radiobutton(root, text = "Student 10", variable = var, value = 10, command = sel)
R10.place(x = 1380, y = 180)

label = Label(root)
label.pack()
frame.pack()
root.mainloop()


                            


                            

                            
    


    




    
