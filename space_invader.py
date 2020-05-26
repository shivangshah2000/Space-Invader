import math
import re
import turtle
import random
import os


window=turtle.Screen()
window.bgcolor("black")
window.title("Space Invader")


pen= turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.setposition(-250,-250)
pen.pendown()

for i in range(4):
    pen.fd(500)
    pen.lt(90)


pen.hideturtle()

player=turtle.Turtle()
player.speed(0)
player.color("yellow")
player.pensize(3)
player.setheading(90)
player.shapesize(2.5,2.5)
player.penup()
player.setposition(0,-220)
player.showturtle()

bullet=turtle.Turtle()
bullet.color("white")
bullet.setheading(90)
bullet.speed(0)
bullet.penup()
bullet.shape("triangle")
bullet.shapesize(0.5,0.5)
bullet.pensize(2)
bullet.hideturtle()

enemy=turtle.Turtle()
enemy.shape("circle")
enemy.shapesize(1,1)
enemy.color("blue")
enemy.speed(0)
enemy.penup()
x=random.randint(-240,240)
y=random.randint(0,200)
enemy.setposition(x,y)


player_movement=10
bullet_speed=20
enemy_movement=5
bullet_state="not_fired"

def move_left():
    x=player.xcor()
    x-=player_movement
    if(x<-240):
        x=-240
    player.setx(x)
        

def move_right():
    x=player.xcor()
    x+=player_movement
    if (x>240):
        x=240
    player.setx(x)

def shoot_bullet():
    global bullet_state
    x=player.xcor()
    y=player.ycor()
    if bullet_state=="not_fired":
        bullet_state="fired"
        bullet.setx(x)
        bullet.sety(y+20)
        bullet.showturtle()
        

def isCollision(t1,t2):
    dist=math.sqrt((t1.xcor()-t2.xcor())*(t1.xcor()-t2.xcor())+(t1.ycor()-t2.ycor())*(t1.ycor()-t2.ycor()))
    if dist<18:
        return True
    else: return False

cnt=0

turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(shoot_bullet,"space")

flag=0
while True:
        x=enemy.xcor()
        y=enemy.ycor()
        x+=enemy_movement
        enemy.setx(x)
        if x>240:
            y-=30
            enemy.sety(y)
            enemy_movement*=-1
        if x<-240:
            y-=30
            enemy.sety(y)
            enemy_movement*=-1
        if isCollision(bullet,enemy) and bullet_state=="fired":
            cnt+=1
            enemy.hideturtle()
            bullet.hideturtle()
            bullet_state="not_fired"
            x=random.randint(-240,240)
            y=random.randint(0,200)
            enemy.setposition(x,y)
            enemy.showturtle()
        if isCollision(player,enemy):
            print("Game Over. Your score is "+str(cnt))
            break

        if bullet_state=="fired":
            y1=bullet.ycor()
            y1+=bullet_speed
            bullet.sety(y1)
            if bullet.ycor()>240:
                bullet.hideturtle()
                bullet_state="not_fired"

    
