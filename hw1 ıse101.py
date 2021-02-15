import turtle
scr = turtle.Screen()
t = turtle.Turtle()
t.color('red')
t.shape("circle")
t.pensize(5)
t.hideturtle()  
t.penup()

st = turtle.Turtle()
st.color('blue')
st.shape("turtle")
st.pensize(2)



list = []
def left_click(x, y):
    
    t.goto(x, y)
    t.stamp()
    list.append((x, y))
    print("You clicked at this coordinate({0},{1})".format(x,y)) 

def key_press_s():
    if len(list) > 0:
        st.up()
        st.goto(list[0])
        st.down()    
    for x, y in list:
        
        st.pendown()
        st.goto(x, y)
        st.pendown()
    
        
        
def key_press_r ():
   st.clear()
   t.clear()
   list.clear()
   st.penup()
   st.goto(0,0)
   
    
scr.onclick(left_click)
scr.onkey(key_press_s, 's')
scr.onkey(key_press_s, 'S')
scr.onkey(key_press_r, 'r')
scr.onkey(key_press_r, 'R')
scr.listen()
scr.mainloop()