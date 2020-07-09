import turtle
import os

wn = turtle.Screen() 		#create the window
wn.title("Pong by Fra")		#set window title
wn.bgcolor("blue")			#set window bg color	
wn.setup(width=800, height=600)		#set window size
wn.tracer(0)						#stops the window from updating. it speeds up the game

#Paddle A
paddle_a = turtle.Turtle()		#recall turtle object. low case t = module name, upper case T = object
paddle_a.speed(0)				#Speed of animation, not speed of the paddle. 0 sets speed at the Max
paddle_a.shape("square")		#set paddle shape
paddle_a.color("white")			#set paddle color
paddle_a.penup()				#to prevent that turtles draws a line for each movement
paddle_a.goto(-350, 0)			#set paddle position on the screen. Axe X = -350 (far left), axe Y=0 (center of the screen)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)	#set the shape of the paddle by stretching it



#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(+350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2   #every time the balls moves it moves to the right by 2 pixels
ball.dy = -2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0	Player B: 0", align="center", font=("Courier", 24, "normal"))


#score
score_a = 0
score_b = 0

#Function
def paddle_a_up():
	y = paddle_a.ycor()		#returns original coordinates on the y axis
	y += 20					#instructs the paddle to move by 20 pixel
	paddle_a.sety(y)		#sets the new coordinates upwards
	
def paddle_a_down():
	y = paddle_a.ycor()		
	y -= 20
	paddle_a.sety(y)
	
def paddle_b_up():
	y = paddle_b.ycor()		
	y += 20
	paddle_b.sety(y)
	
def paddle_b_down():
	y = paddle_b.ycor()		
	y -= 20
	paddle_b.sety(y)
	

# keyboard binding
wn.listen()			#listend for keyboard Input
wn.onkey(paddle_a_up, "w")	#when the user presses the key w, call function paddle_a_up

wn.listen()			
wn.onkey(paddle_a_down, "s")

wn.listen()			
wn.onkey(paddle_b_up, "Up")	

wn.listen()			
wn.onkey(paddle_b_down, "Down")


# Main game loop  

while True:
	wn.update()		#Every time the loop runs, it updates the screen
	
	
	#Move the ball
	ball.setx(ball.xcor() + ball.dx)	#sets the ball new coordinates as the original coordinates + balldx (2 pixels to the right)
	ball.sety(ball.ycor() + ball.dy)
	
	#Border checking
	if ball.ycor() > 290:  #half of the screen is +300 pixels. the ball is 20 pixels. Set coordinates at 290
		ball.sety(290)   #resets the ball coordinate at the end of the screen (bounce)
		ball.dy *= -1		# reverse ball direction. ball.dy(2) * -1 = -2
		os.system("afplay bounce.wav&")
		
	if ball.ycor() < -290:  
		ball.sety(-290)   
		ball.dy *= -1	
		os.system("afplay bounce.wav&")
		
	if ball.xcor() > 390:  
		ball.goto(0, 0)   
		ball.dx *= -1
		score_a += 1
		os.system("afplay fail.wav&")
		pen.clear()
		pen.write("Player A: {}	Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
	
	if ball.xcor() < -390:  
		ball.goto(0, 0)   
		ball.dx *= -1	
		score_b += 1
		os.system("afplay fail.wav&")
		pen.clear()
		pen.write("Player A: {}	Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
		
	# paddle and ball collision
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
		ball.setx (340)
		ball.dx *= -1
		os.system("afplay bounce.wav&")
		
	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
		ball.setx (-340)
		ball.dx *= -1
		os.system("afplay bounce.wav&")
		
done()
		
	
	