setMediaPath('/Users/mst/Downloads')
p=makePicture('maze.jpg')
w=makeWorld(400,228)
d=25
t=makeTurtle(w)
t.setColor(white)
w.setPicture(p)
penUp(t)
moveTo(t,20,140)
turnRight(t)
penDown(t)
forward(t,40)

def canTurnLeft(t):
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
    
def canTurnRight(t):
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
  while canGoForward(t):
    forward(t,d)
    if canTurnLeft(t):
      h=getHeading(t)
      h=h-90
      if h == -360:
        h = 0
      tt=makeTurtle(w)
      penUp(tt)
      moveTo(tt,t.getXPos(),t.getYPos())
      penDown(tt)
      tt.setHeading(h)
      forward(tt,d)    
      travelMaze(tt) 
    if canTurnRight(t):
      turnRight(t)
  return


travelMaze(t)
w.repaint()
    