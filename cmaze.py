class Maze:
  def __init__(self, image_file):
    setMediaPath('/Users/toth/Documents/Github/turtlemaze')
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
  
  def getTurtle(self):
    return self.t
    
  def moveForward(self,d):
    forward(self.t,d)
    
  def distance2wall(self):
    d=0
    xpos = self.t.getXPos()
    ypos = self.t.getYPos()
    px = getPixelAt(self.image,xpos,ypos)
    h=self.t.getHeading()
    if h==0:
      while distance(getColor(px),white)<100:
        d += 1
        px = getPixelAt(self.image,xpos,ypos-d)
      return d
    if h == 90 or h == -270:
      while distance(getColor(px),white)<100:
        d += 1
        px = getPixelAt(self.image,xpos+d,ypos)
      return d
    if h==180 or h == -180:
      while distance(getColor(px),white)<100:
        d += 1
        px = getPixelAt(self.image,xpos,ypos+d)
      return d
    if h == -90 or h == 270:
      while distance(getColor(px),white)<100:
        d += 1
        px = getPixelAt(self.image,xpos-d,ypos)
      return d
      
    
      
  def move2wall(self):
    d=self.distance2wall()
    forward(self.t,d-10)
      

m=Maze('maze.jpg')