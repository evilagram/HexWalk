from turtle import Turtle
import random
def lerp (S,E,i):
    return S + i * (E - S)

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

def hexWalk(t,sides=3,distance=200,reps=40,width=4):
    interiorAng=(sides-2)*180
    t.pensize(3)
    t.speed(0)
    #rS=1.0
    #rE=0.2
    #gS=0.1
    #gE=1.0
    #bS=0.0
    #bE=0.5
    for i in range(reps):
        #t.pencolor(lerp(rS,rE,float(i)/float(reps)),lerp(gS,gE,float(i)/float(reps)),lerp(bS,bE,float(i)/float(reps)))
        t.pencolor(lerpColor(float(i)/float(reps))[0],lerpColor(float(i)/float(reps))[1],lerpColor(float(i)/float(reps))[2])
        for x in range(sides):
            t.forward(distance)
            t.left(360/sides)
        t.penup()
        t.left(interiorAng/sides/2)
        t.forward(distance*(width/100))
        t.right(interiorAng/sides/2)
        t.pendown()
        distance *= (100-width)/100
        

hexWalk(Turtle())
