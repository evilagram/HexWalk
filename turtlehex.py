from turtle import Turtle
import random
def lerp (start,end,i):
    return start + i * (end - start)

def lerpColor(i):
    if(i <= 1.0/5):
        return [1,lerp(0,1,i/(1.0/5)),0]
    elif(i >= 1.0/5 and i <= 2.0/5):
        return [lerp(1,0,(i-(1.0/5))/((2.0/5)-(1.0/5))),1,0]
    elif(i >= 2.0/5 and i <= 3.0/5):
        return [0,1,lerp(0,1,(i-(2.0/5))/((3.0/5)-(2.0/5)))]
    elif(i >= 3.0/5 and i <= 4.0/5):
        return [0,lerp(1,0,(i-(3.0/5))/((4.0/5)-(3.0/5))),1]
    elif(i >= 4.0/5 and i <= 5.0/5):
        return [lerp(0,1,(i-(4.0/5))/((5.0/5)-(4.0/5))),0,1]

def hexWalk(t,sides=12,distance=150,reps=40,width=4):
    t.pensize(4)
    t.speed(0)
    #redStart=1.0
    #redEnd=0.2
    #greenStart=0.1
    #greenEnd=1.0
    #blueStart=0.0
    #blueEnd=0.5
    for i in range(reps):
        #t.pencolor(lerp(redStart,redEnd,float(i)/float(reps)),lerp(greenStart,greenEnd,float(i)/float(reps)),lerp(blueStart,blueEnd,float(i)/float(reps)))
        t.pencolor(lerpColor(float(i)/float(reps))[0],lerpColor(float(i)/float(reps))[1],lerpColor(float(i)/float(reps))[2])
        for x in range(sides):
            t.forward(distance)
            t.left(360/sides)
        t.penup()
        t.left(540/sides/2)
        t.forward(distance*(width/100))
        t.right(360/sides/2)
        t.pendown()
        distance -= width
        

hexWalk(Turtle())
