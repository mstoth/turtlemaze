
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
    moveTo(self.t,25,184)
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
      
  def colorInFront(self,d=20):
    h=self.t.getHeading()
    if h == 0:
      if self.t.getYPos()-d < 0:
        return blue
      else:
        return getColor(getPixelAt(self.image,self.t.getXPos(),self.t.getYPos()-d))
    if h == 90 or h == -270:
      if self.t.getXPos()+d > getWidth(self.image)-1:
        return blue
      else:
        return getColor(getPixelAt(self.image,self.t.getXPos()+d,self.t.getYPos()))
    if h == 180 or h == -180:
      if self.t.getYPos()+d > getHeight(self.image)-1:
        return blue
      else:
        return getColor(getPixelAt(self.image,self.t.getXPos(),self.t.getYPos()+d))
    if h == 270 or h == -90:
      if self.t.getXPos()-d < 0:
        return blue
      else:
        return getColor(getPixelAt(self.image,self.t.getXPos()-d,self.t.getYPos()))
  
  def turnTurtleRight(self):
    self.t.setHeading(self.t.getHeading()+90)
    
  def turnTurtleLeft(self):
    self.t.setHeading(self.t.getHeading()-90)
    
  def surroundings(self):
    sur=[]
    # get color where I am
    c=getColor(getPixelAt(self.image,self.t.getXPos(),self.t.getYPos()))
    if c == None:
      raise Exception("c is None")
    
    sur.append(c)
    for i in range(4):
      if self.colorInFront().__class__ != Color:
        sur.append(blue)
      else:
        sur.append(self.colorInFront())
      self.t.turnRight()
        
    bounds=[]
    for c in sur:
      if distance(c,yellow)<50:
        bounds.append('end')
      elif distance(c,green)<50:
        bounds.append('visited')
      elif distance(c,red)<50:
        bounds.append('visited')
      elif distance(c,blue)<100:
        bounds.append('wall')
      elif distance(c,white)<50:
        bounds.append('empty')
      else: # assume a wall
        bounds.append('wall')
    return bounds
  
      
      
  def move2wall(self):
    d=self.distance2wall()
    self.travelForward(d-10)
      
  def travelForward2BranchOrWall(self):
  
    if self.surroundings().count('empty') > 2 and self.surroundings()[3] != 'empty':
      while self.surroundings().count('empty') > 2:
        self.travelForward(1)
      
        
    while self.surroundings()[1]=='empty':
      s=self.surroundings()[1]
      if s == 'wall':
        return
      if self.surroundings().count('empty')>2 and self.surroundings()[3] != 'empty':
        self.travelForward(10)
        return
      else: 
        self.travelForward(1)
    self.travelForward(10)
    return
    
  def travelForward(self,dist):
    for i in range(int(dist)):
      # printNow(str(distance(getColor(getPixelAt(self.image,self.t.getXPos(),self.t.getYPos())),green)))
      if distance(getColor(getPixelAt(self.image,self.t.getXPos(),self.t.getYPos())),green) < 100:
        self.t.setColor(red)
        color = red
      elif distance(getColor(getPixelAt(self.image,self.t.getXPos(),self.t.getYPos())),red) < 100:
        self.t.setColor(red)
        color = red
      else:
        self.t.setColor(green)
        color = green
      h=self.t.getHeading()
      if h == 0 or h == 180 or h == -180:
        addLine(self.image,self.t.getXPos()-10,self.t.getYPos(),self.t.getXPos()+10,self.t.getYPos(),color)
      else:
        addLine(self.image,self.t.getXPos(),self.t.getYPos()-10,self.t.getXPos(),self.t.getYPos()+10,color)
      forward(self.t,1) 
  
  
  
  
  def solve(self,xpos,ypos,heading):
    
    s=self.surroundings()
    if s[0] == 'end' or s[1] == 'end':
      print 'found at %d, %d' % (xpos,ypos)
      return true
    elif s[0] == 'wall':
      print 'found wall at %d, %d' % (xpos,ypos)
      return false
    elif s[0] == 'visited':
      print 'found visited at %d, %d' % (xpos,ypos)
      return false
    
    print 'visiting %d, %d' % (xpos,ypos)    
    h=heading 
    for i in range(1,5):
      
      if self.surroundings()[1] == 'empty':
        savedX=self.t.getXPos()
        savedY=self.t.getYPos()
        savedH=self.t.getHeading()
        self.travelForward2BranchOrWall()
        if self.solve(self.t.getXPos(),self.t.getYPos(),self.t.getHeading()):
          return true
        else:
          penUp(self.t)
          printNow("Turning to face %d,%d" % (savedX,savedY))
          turnToFace(self.t,savedX,savedY)
          penDown(self.t)
          d=sqrt((self.t.getXPos()-savedX)**2+(self.t.getYPos()-savedY)**2)
          self.travelForward(d)
          self.t.setHeading(savedH)
      
      self.t.turnRight()
      h += 90
        
    return false
  
       
    
  def showGrid(self):
    dx=self.image.getWidth()/20
    dy=dx
    for xpos in range(20):
      addLine(self.image,xpos*dx,0,xpos*dx,self.image.getHeight(),black)
    ypos = 0
    while ypos < getHeight(self.image):
      addLine(self.image,0,ypos,self.image.getWidth(),ypos,black)  
      ypos += dx
    self.w.repaint()
  
  
  
  
  
m=Maze('maze.jpg')
t=m.getTurtle()

# m.solve(t.getXPos(),t.getYPos(),t.getHeading())

  

