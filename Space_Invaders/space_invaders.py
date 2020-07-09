#### test 1

import turtle
import os
import math
import random 

#set up the screen
wn = turtle.Screen()	
wn.bgcolor("black")					#Set widow color
wn.title("Space Invaders by Fra")	#Set window title
wn.bgpic("space_invaders_background.gif")

#Register shapes
turtle.register_shape("ship.gif")
turtle.register_shape("invader.gif")


#Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)		#set pen speed to 0
border_pen.color("white")		#set pen color
border_pen.penup()		#set penup as we don't want the pen trace but just to move the pen
border_pen.setposition(-300, -300)	#set pen position (y=-300, x=-300)
border_pen.pendown()	#set pendown as we want the pen to leave a trace now
border_pen.pensize(3)	#set pentip size
for side in range (4):	#set function to move the pen forward by 600 and left by90
	border_pen.fd(600)	#the function range (4) repeats the given movement 4 times
	border_pen.lt(90)
border_pen.hideturtle()	#no more need to see the pen pointer. This hides the pen

#Set the score to 0
score = 0

#Draw the score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-290, 280)
scorestring = "Score: %s" %score
pen.write(scorestring, False, align="left", font=("Courier", 16, "normal"))
pen.hideturtle


#Create the player turtle
player = turtle.Turtle()
player.color("blue")		#set player color
player.shape("ship.gif")	#set player shape
player.penup()				#lift pen
player.speed(0)				#set animation speed to 0
player.setposition(0, -250)	#set player position at the bottom of the window
player.setheading(90)		#change player orientation by 90 degrees. from < to ∆

playerspeed = 15

#Choose number of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies = [] #empty list

#Add enemies to the list
for i in range(number_of_enemies):
	#Create the enemies
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color ("red")
	enemy.shape ("invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint (100, 250)
	enemy.setposition (x, y)

enemyspeed = 2


#Create the player's bullet

bullet = turtle.Turtle()
bullet.color ("white")
bullet.shape ("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 40

#Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"



# player left movement
def player_left():
	x = player.xcor()		
	x -= playerspeed
	if x < -280:
		x = -280
	player.setx(x)
	
# player right movement		
def player_right():
	x = player.xcor()		
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)
	

	
def fire_bullet():
	#declare bullet state as global if it needs to be changed
	global bulletstate
	os.system("afplay laser.wav&")
	if bulletstate == "ready":
		bulletstate = "fire"
	#Move the bullet to just above player position
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x, y)
		bullet.showturtle()

#set collisions
def isCollision(t1, t2): #turtle 1 (bullet), turtle 2 (enemy)
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 20:
		return True
	else:
		return False
	

#keyboard links for player
turtle.listen()
turtle.onkey(player_left, "Left")
turtle.listen()
turtle.onkey(player_right, "Right")
turtle.listen() 
turtle.onkey(fire_bullet, "space")

#Main game loop
while True:

	for enemy in enemies:
		# Move enemy 
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)
	
		#move enemy back and down
		if enemy.xcor() > 280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1
			
		if enemy.xcor() < -280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1
		
		if isCollision (bullet, enemy):
			os.system("afplay explosion.wav&")
			#reset bullet
			bullet.hideturtle
			bulletstate = "ready"
			bullet.setposition (0, -400)
			#reset enemy
			x = random.randint(-200, 200)
			y = random.randint (100, 250)
			enemy.setposition (x, y)
			#update score
			score += 10	
			scorestring = "Score: %s" %score
			pen.clear()
			pen.write(scorestring, False, align="left", font=("Courier", 16, "normal"))

		if isCollision (player, enemy):
			os.system("afplay Explosion+3.wav&")
			player.hideturtle()
			enemy.hideturtle()
			print("Game Over")
			break

	#Move bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)
	
	#check to see if the bullet has gone to the top
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"
	

delay = raw_input("Press enter to finsh.")




