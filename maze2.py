setMediaPath('/Users/mst/Downloads')

p=makePicture('maze.jpg')
w=makeWorld(400,228)
d=8
t=makeTurtle(w)
t.setColor(white)
w.setPicture(p)
penUp(t)
moveTo(t,20,140)
turnRight(t)
# penDown(t)
forward(t,40)
import time
import random

addRectFilled(p,53,137,10,10,blue)
addRectFilled(p,350,123,20,20,red)

def canGoLeft(t):
  global p
  global d
  heading=getHeading(t)
  if heading == 90 or heading == -270:
    xpos,ypos=t.getXPos(),t.getYPos()-d
  if heading == 0:
    xpos,ypos=t.getXPos()-d,t.getYPos()
  if heading == -90 or heading == 270:
    xpos,ypos=t.getXPos(),t.getYPos()+d
  if heading == 180 or heading == -180:
    xpos,ypos=t.getXPos()+d,t.getYPos()
  pixel2left=getPixelAt(p,xpos,ypos)
  if distance(getColor(pixel2left),white)>100:
    return false
  else:
    return true
    
def canGoRight(t):
  global p
  global d
  heading=getHeading(t)
  if heading == 90 or heading == -270:
    xpos,ypos=t.getXPos(),t.getYPos()+d
  if heading == 0:
    xpos,ypos=t.getXPos()+d,t.getYPos()
  if heading == -90 or heading == 270:
    xpos,ypos=t.getXPos(),t.getYPos()-d
  if heading == 180 or heading == -180:
    xpos,ypos=t.getXPos()-d,t.getYPos()
  pixel2right=getPixelAt(p,xpos,ypos)
  if distance(getColor(pixel2right),white)>100:
    return false
  else:
    return true
    
    
 
def solved(t):
  global p
  global d
  heading=getHeading(t)
  if heading == 90 or heading == -270:
    xpos,ypos=t.getXPos()+d,t.getYPos()
  if heading == 0:
    xpos,ypos=t.getXPos(),t.getYPos()-d
  if heading == -90 or heading == 270:
    xpos,ypos=t.getXPos()-d,t.getYPos()
  if heading == 180 or heading == -180:
    xpos,ypos=t.getXPos(),t.getYPos()+d
  pixelInFront=getPixelAt(p,xpos,ypos)
  if getColor(pixelInFront)==red:
    return true
  else:
    return false

def canGoForward(t):
  global p
  global d
  heading=getHeading(t)
  if heading == 90 or heading == -270:
    xpos,ypos=t.getXPos()+d,t.getYPos()
  if heading == 0:
    xpos,ypos=t.getXPos(),t.getYPos()-d
  if heading == -90 or heading == 270:
    xpos,ypos=t.getXPos()-d,t.getYPos()
  if heading == 180 or heading == -180:
    xpos,ypos=t.getXPos(),t.getYPos()+d
  pixelInFront=getPixelAt(p,xpos,ypos)
  if distance(getColor(pixelInFront),white)<100:
    return true
  else:
    return false
    
def canGoBack(t):
  global p
  global d
  heading=getHeading(t)
  if heading == 90 or heading == -270:
    xpos,ypos=t.getXPos()-d,t.getYPos()
  if heading == 0:
    xpos,ypos=t.getXPos(),t.getYPos()-d
  if heading == -90 or heading == 270:
    xpos,ypos=t.getXPos()-d,t.getYPos()
  if heading == 180 or heading == -180:
    xpos,ypos=t.getXPos(),t.getYPos()+d
  pixelBehindMe=getPixelAt(p,xpos,ypos)
  if distance(getColor(pixelBehindMe),white)>100:
    return false
  else:
    return true
    
def travelMaze(t):
  global d
  while not solved(t):
    goToBranch(t)
    if canGoLeft(t):
      savex=t.getXPos()
      savey=t.getYPos()
      saveh=t.getHeading()
      turnLeft(t)
      if travelMaze(t):
        return true
      else:
        t.setXPos(savex)
        t.setYPos(savey)
        t.setHeading(saveh)
        return travelMaze(t)
    else:
      
        
    goToWall(t)
    if canGoLeft(t):
      turnLeft(t)
      goToWall(t)
    elif canGoRight(t):
      turnRight(t)
      goToWall(t)
    else:
      turnRight(t)
      turnRight(t)
      goToWall(t)

    
  


# travelMaze(t)
# w.repaint()
    
def goToWall(t):
  counter = 0
  while canGoForward(t):
    forward(t,1)
    time.sleep(0.01)
    if canGoRight(t):
      while canGoRight(t):
        forward(t,1)
        counter += 1
      backward(t,counter/2)
      turnRight(t)
      
      if random.randint(0,1): # randomly choose to take the right turn
        forward(t,5)
        turnRight(t)
      else:
        forward(t,20)
    elif canGoLeft(t):
      if random.randint(0,1): # randomly choose to take the right turn
        forward(t,4)
        turnLeft(t)
      else:
        forward(t,20)
    else:
      return

      
def distance2wall(t):
  h=getHeading(t)
  
      
    
    
travelMaze(t)



    
