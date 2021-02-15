import turtle
import time
animate = 0
scr = turtle.Screen()
print(scr.tracer(0))
t = turtle.Turtle()
t.hideturtle()       
t.penup()   
t.forward(20)
t.pendown()
t.setheading(90)       
t.color('red')       
t.circle(20)         
st = turtle.Turtle()
st.hideturtle()
st.color('blue')
st.speed(0)
t.speed(0)

def rectangle():

    st.penup()
    st.forward(140)     
    st.left(90)
    st.pendown()
    st.forward(10)
    st.left(90)
    st.forward(120)
    st.left(90)
    st.forward(20)
    st.left(90)
    st.forward(120)
    st.left(90)
    st.forward(10)

def drawrectangles():
    for i in range(4):
      rectangle()
      st.penup()
      st.goto(0, 0)
      st.pendown()
      
     
      

while True:
    
  st.clear()
  
  scr.ontimer(drawrectangles(),300)  
  st.left(10)
  scr.update()
  scr.tracer(0,0) 

