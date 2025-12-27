# Lets yu move a box with the arror keys\
import intrographics


#This function moves the box
def timer():
    box.move(box.dx,box.dy)
    
    #bounce off the bottom or top the edge
    if box.bottom >= window.bottom:
        box.dy = -2
    elif box.top <= window.top:
        box.dy = 2
     #bounce off the right or top the edge
    if box.right >= window.right:
        box.dx = -2
    elif box.left<= window.left:
        box.dx = 2

#Tis code sets the Window
window = intrographics.window(300,200)

box = window.rectangle(0,0,20,20)
box.fill("red")
box.dx = 2
box.dy = 2

window.on_timer(30, timer)


window.open()