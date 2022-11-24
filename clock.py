import time
import turtle
import turtle as t
t.speed(0)
myscreen=turtle.Screen()
myscreen.setup(width=750,height=750)
myscreen.addshape('wall3.gif')
myscreen.bgpic("wall3.gif")
move=turtle.Turtle()
move.hideturtle()
t.tracer(0,0)
for i in range (10,116,3):
    move.speed(0)
    for j in range (5,43,1):
        move.pendown()
        move.pensize(1)
        move.right(160)
        move.forward(j)
    move.right(30)
move.setheading(135) #for easily taking it to the center
move.penup()
move.goto(0,70)
move.setheading(180)
move.forward(83)
move.setheading(90)
for i in range (12):
    move.penup()
    move.forward(67)
    move.pendown()
    move.pensize(5)
    move.forward(18)
    move.penup()
    move.backward(85)
    move.right(30)
#writing number 12 0n the clock
move.penup()
move.forward(46)
move.pendown()
move.pensize(3)
move.write(12,move=False,font=("Forte",15,"bold"))
move.penup()
move.backward(46)
move.pendown()
#writing number 3 0n the clock
move.setheading(0)
move.penup()
move.forward(54)
move.pendown()
move.pensize(3)
move.write(3,move=False,font=("Forte",15,"bold"))
move.penup()
move.backward(54)
move.pendown()
#writing number 6 0n the clock
move.setheading(270)
move.penup()
move.forward(59)
move.pendown()
move.pensize(3)
move.write(6,move=False,font=("Forte",15,"bold"))
move.penup()
move.backward(59)
move.pendown()
#writing number 9 0n the clock
move.setheading(180)
move.penup()
move.forward(59)
move.pendown()
move.pensize(3)
move.write(9,move=False,font=("Forte",15,"bold"))
move.penup()
move.backward(59)
move.pendown()
#drawing the clock hands
pencil=turtle.Turtle()
def  hands(hour,miniute,second,pencil):
    pencil.setheading(135) #for easily taking it to the center
    pencil.penup()
    pencil.goto(0,70)
    pencil.setheading(180)
    pencil.forward(83)
    pencil.setheading(90)
    #hour hand
    pencil.color("green")
    pencil.setheading(90)
    inclination=(hour*30)
    pencil.right(inclination)
    pencil.pendown()
    pencil.pensize(3)
    pencil.forward(24)
    pencil.penup()
    pencil.backward(24)
    #minute hand
    pencil.color("red")
    pencil.setheading(90)
    inclination=(miniute*6)
    pencil.right(inclination)
    pencil.pendown()
    pencil.pensize(3)
    pencil.forward(37)
    pencil.penup()
    pencil.backward(37)
    #second hand
    pencil.color("yellow")
    pencil.setheading(90)
    inclination=(second*6)
    pencil.right(inclination)
    pencil.pendown()
    pencil.forward(52)
    pencil.penup()
    pencil.backward(52)
while True:
    hour=int(time.strftime("%I"))
    miniute=int(time.strftime("%M"))
    second=int(time.strftime("%S"))
    hands(hour,miniute,second,pencil)
    myscreen.update()
    time.sleep(1)
    pencil.clear()

        

               
               
               
    
  
    
    
  
    
    

               
