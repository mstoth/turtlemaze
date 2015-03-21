
class Maze:
  def __init__(self, image_file):
    """
    Methods: __init__ needs an image file. The media path is set. Edit for your needs.
          getTurtle() returns the turtle
          moveForward(distance) moves the turtle forward the supplied distance
          distance2wall() returns the distance to the wall in front of the turtle
          colorInFrontOfTurtle() returns the color of the pixel 10 pixels in front of the turtle
    """
    self.image = makePicture(image_file)
    self.w = makeWorld(getWidth(self.image),getHeight(self.image))
    self.t = makeTurtle(self.w)
    penUp(self.t)
    self.w.setPicture(self.image)
    moveTo(self.t,22,184)
    self.t.setHeading(90)
    self.t.setPenWidth(20)
    penDown(self.t)
    self.t.setColor(green)
  
  def getWorld(self):
    return self.w
  def getTurtle(self):
    return self.t
  def getImage(self):
    return self.image
    
  def moveForward(self,d):
    self.travelForward(d)
    
  def distance2wall(self):
    d=0
    xpos = self.t.getXPos()
    ypos = self.t.getYPos()
    px = getPixelAt(self.image,xpos,ypos)
    h=self.t.getHeading()
    if h==0:
      while distance(getColor(px),white)<100 or distance(getColor(px),green)<100:
        d += 1
        px = getPixelAt(self.image,xpos,ypos-d)
      return d
    if h == 90 or h == -270:
      while distance(getColor(px),white)<100 or distance(getColor(px),green)<100:
        d += 1
        px = getPixelAt(self.image,xpos+d,ypos)
      return d
    if h==180 or h == -180:
      while distance(getColor(px),white)<100 or distance(getColor(px),green)<100:
        d += 1
        px = getPixelAt(self.image,xpos,ypos+d)
      return d
    if h == -90 or h == 270:
      while distance(getColor(px),white)<100 or distance(getColor(px),green)<100:
        d += 1
        px = getPixelAt(self.image,xpos-d,ypos)
      return d
      
  def colorInFront(self):
    h=self.t.getHeading()
    if h == 0:
      return getColor(getPixelAt(self.image,self.t.getXPos(),self.t.getYPos()-10))
    if h == 90 or h == -270:
      return getColor(getPixelAt(self.image,self.t.getXPos()+10,self.t.getYPos()))
    if h == 180 or h == -180:
      return getColor(getPixelAt(self.image,self.t.getXPos(),self.t.getYPos()+10))
    if h == 270 or h == -90:
      return getColor(getPixelAt(self.image,self.t.getXPos()-10,self.t.getYPos()))
  
  def turnTurtleRight(self):
    self.t.setHeading(self.t.getHeading()+90)
    
  def turnTurtleLeft(self):
    self.t.setHeading(self.t.getHeading()-90)
    
  
      
  def move2wall(self):
    d=self.distance2wall()
    self.travelForward(d-10)
      
  def travelForward(self,dist):
    for i in range(dist):
      printNow(str(distance(getColor(getPixelAt(self.image,self.t.getXPos(),self.t.getYPos())),green)))
      if distance(getColor(getPixelAt(self.image,self.t.getXPos(),self.t.getYPos())),green) < 100:
        self.t.setColor(red)
        color = red
      else:
        self.t.setColor(green)
        color = green
      h=self.t.getHeading()
      if h == 0 or h == 180 or h == -180:
        addLine(self.image,self.t.getXPos()-5,self.t.getYPos(),self.t.getXPos()+5,self.t.getYPos(),color)
      else:
        addLine(self.image,self.t.getXPos(),self.t.getYPos()-5,self.t.getXPos(),self.t.getYPos()+5,color)
      forward(self.t,1) 
      
m=Maze('maze.jpg')

m.move2wall()
m.turnTurtleRight()
m.move2wall()
m.turnTurtleRight()
m.move2wall()
m.turnTurtleLeft()
m.move2wall()
m.turnTurtleLeft()
m.move2wall()
m.turnTurtleLeft()
m.turnTurtleLeft()
m.move2wall()
m.turnTurtleRight()
m.move2wall()
m.turnTurtleRight()
m.move2wall()


