import turtle

# generate turtle and screen objects
tt = turtle.Turtle()
tt.shape('turtle')
tt.pensize(2)
tt.color('red')
scr = turtle.Screen()

# Implement handlers
def follow_click(x, y):
    tt.setposition(x, y)
    
# setup event handlers
scr.onclick(follow_click)

# setup listener and main loop
scr.listen()
scr.mainloop()