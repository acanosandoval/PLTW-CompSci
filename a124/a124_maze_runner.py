#   a124_maze_spiral.py
#----INITIAL SETUP----
import turtle as trtl
import random as rand
wn = trtl.Screen()

#----VARIABLES SETUP----
num_of_walls = 5 * 5
wall_length = 50
path_width = 12
wall_color = "black"
wall_count = 1

#----WALL PEN SETUP----
wall_pen = trtl.Turtle()
wall_pen.hideturtle()
wall_pen.pensize(4)
wall_pen.speed("fastest")
wall_pen.color(wall_color)

#----MAZE RUNNER SETUP----
maze_runner1 = trtl.Turtle(shape="circle")
maze_runner1.penup()
maze_runner1.goto((-path_width*2), 0)
maze_runner1.pendown()
maze_runner1.color("orchid")
maze_runner1.shapesize(0.5)

#----FUNCTIONS----
def draw_door(doorplace):
  wall_pen.forward(doorplace)
  wall_pen.penup()
  wall_pen.forward(path_width*2)
  if wall_count > 4:
    wall_pen.pendown()
    
def draw_barrier(barrierplace):
  wall_pen.forward(barrierplace)
  wall_pen.left(90)
  wall_pen.forward(path_width*2)
  wall_pen.back(path_width*2)
  wall_pen.right(90)
  
def move_runner1():
  maze_runner1.forward(int(15))

def up_key():
  maze_runner1.setheading(90)
  move_runner1()
def down_key():
  maze_runner1.setheading(270)
  move_runner1()
def right_key():
  maze_runner1.setheading(0)
  move_runner1()
def left_key():
  maze_runner1.setheading(180)
  move_runner1()


#----DRAWING THE MAZE----
for r in range(num_of_walls):
  #---random door and barrier setup---
  door = rand.randint(path_width*2, (wall_length - path_width*2))
  barrier = rand.randint(path_width*2, (wall_length - path_width*2))
  
  #---skip over first 4 walls---
  if wall_count > 4:
    wall_pen.pendown()
    #--if door and barrier values too close, get new door value--
    while abs(door - barrier) < path_width*2:
      door = rand.randint(path_width*2, (wall_length - path_width*2))
  else:
    wall_pen.penup()
  wall_pen.left(90)

  #if door comes first
  if (door < barrier):
    #---draws doors---
    draw_door(door)
    #---draws barriers---
    draw_barrier((barrier - door - path_width*2))
    wall_pen.forward(wall_length - barrier)

  #if barrier comes first
  else:
    #---draws barriers---
    draw_barrier(barrier)
    #---draws doors---
    draw_door((door - barrier))
    wall_pen.forward(wall_length - door - path_width*2)

  #---final variable changes---
  wall_length = wall_length + path_width
  wall_count = wall_count + 1

wn.listen()
wn.onkeypress(up_key, "Up")
wn.onkeypress(down_key, "Down")
wn.onkeypress(right_key, "Right")
wn.onkeypress(left_key, "Left")
wn.mainloop()