
# maze program by Michael Toth
setMediaPath('/Users/michaeltoth/Documents/turtlemaze')
class Maze(object):
  """ Creates and solves a maze using turtles in JES. """
  def __init__(self):
    self.image = makePicture('maze.jpg')
    self.w = makeWorld(getWidth(self.image),getHeight(self.image))
    self.w.setPicture(self.image)
    self.t = makeTurtle(self.w)
    penUp(self.t)
    moveTo(self.t,25,187)
    self.t.setHeading(90)
    penDown(self.t)
    
  def currentColor(self):
    px = getPixelAt(self.image,self.t.getXPos(),self.t.getYPos())
    c = getColor(px)
    if distance(c,white) < 150:
      return white
    if distance(c,blue) < 150:
      return blue
    if distance(c,red) < 150:
      return red
    if distance(c,green) < 150:
      return green
    if distance(c,yellow) < 150:
      return yellow
      
  def colorInFront(self):
    """ returns the color 15 pixels in front of the turtle"""
    heading = self.t.getHeading()
    if heading == 90 or heading == -270: 
      px = getPixelAt(self.image,self.t.getXPos()+15,self.t.getYPos()) 
    if heading == 0:
      px = getPixelAt(self.image,self.t.getXPos(),self.t.getYPos()-15)
    if heading == -90 or heading == 270: 
      px = getPixelAt(self.image,self.t.getXPos()-15,self.t.getYPos()) 
    if heading == 180 or heading == -180:
      px = getPixelAt(self.image,self.t.getXPos(),self.t.getYPos()+15)
    c = getColor(px)
    if distance(c,white) < 150:
      return white
    if distance(c,blue) < 150:
      return blue
    if distance(c,red) < 150:
      return red
    if distance(c,green) < 150:
      return green
    if distance(c,yellow) < 150:
      return yellow
    # Unknown color, assume wall. 
    return blue
    
  def travel2BranchOrWall(self):
    while self.surroundings()[1] == 'empty' or self.surroundings()[3] == 'empty':
      self.travelForward(1)
    while self.surroundings()[0] != 'wall' and self.surroundings()[0] != 'end':
      self.travelForward(1)
      if self.surroundings().count('empty') > 1:
        self.travelForward(9)
        return
    self.travelForward(9)
        
  def surroundings(self):
    """ returns a list of 4 states representing the turtle's environment """
    colorMap = { 'wall':blue,'empty':white,'visited':green,'end':yellow, 'revisited':red }
    s=[]
    for i in range(4):
      c = self.colorInFront()
      # printNow(c)
      assert c.__class__ == Color
      for key,col in colorMap.items(): 
        if col == c:
          s.append(key)
      self.t.turnRight()
    return s
    
  def travelForward(self,dist=10):
    while dist > 0:
      x=self.t.getXPos()
      y=self.t.getYPos()
      if self.colorInFront() == white:
        addOvalFilled(self.image,x-8,y-8,16,16,green)
      else:
        addOvalFilled(self.image,x-8,y-8,16,16,red)
      dist=dist-1
      forward(self.t,1)
      repaint(m.image)
    
  def solve(self):
    """ solves the maze """
    if self.colorInFront()==yellow:
      return true
    
    for d in range(0,360,90):
      self.t.setHeading(d)
      saveH=self.t.getHeading()
      saveX=self.t.getXPos()
      saveY=self.t.getYPos()
      if self.surroundings()[0]=='empty':
        self.travel2BranchOrWall()
        if self.solve():
          return true
        self.t.turnToFace(saveX,saveY)
        self.travelForward(sqrt((saveX-m.t.getXPos())**2 + (saveY-m.t.getYPos())**2))
        self.t.setHeading(saveH)
    return false
    
        
        
    
                
                              
                                                          
# tests

# test the existence of the class
m = Maze()

# test we have the image
show(m.image)

# test we have a world in the maze
world = m.w

# test that the world has the image as a background
p=m.w.getPicture()
assert p.getFileName() != 'None', 'No File Name for world picture.'

# test that we have a turtle
m.t

# test that it is in the right place
assert m.t.getXPos() == 25, 'Turtle x position not correct.'
assert m.t.getYPos() == 187, 'Turtle y position not correct.'

# tests for the existence of colorInFront
c=m.colorInFront()

# test that we get white from colorInFront
assert c == white,'color is not white.'

# test we are near a wall and we get blue
forward(m.t,75)
assert m.colorInFront() == blue, 'color is not blue near the wall.'

# test that we get blue when we are facing north near a wall
backward(m.t,30)
turn(m.t,-90)
assert m.colorInFront() == blue, 'color is not blue facing north'

# test that we get blue when facing south
turn(m.t,180)
assert m.colorInFront() == blue, 'color is not blue facing south'

# test that we get blue for facing west
moveTo(m.t,25,187)
m.t.setHeading(-90)
assert m.colorInFront() == blue, 'color is not blue facing west'

# test that we get blue for facing south
m.t.setHeading(180)
assert m.colorInFront() == blue, 'color is not blue facing south'

# test for the existence of travel2BranchOrWall
moveTo(m.t,25,187)
m.t.setHeading(90)
m.image = makePicture('maze.jpg')
m.travel2BranchOrWall()

# test that we are at the wall
assert m.t.getXPos() == 100, 'X position not correct for travel2BranchOrWall'
assert m.t.getYPos() == 187, 'Y position not correct for travel2BranchOrWall'

# test for a method called surroundings
s=m.surroundings()

# test that it returns 4 items; empty, wall, wall, empty. 
moveTo(m.t,25,187)
m.t.setHeading(90)
assert m.surroundings() == ['visited','wall','wall','empty'], m.surroundings()

# test for the existence of currentColor
moveTo(m.t,25,187)
m.t.setHeading(90)
m.image = makePicture('maze.jpg')
assert m.currentColor() == white

# test that we get ['empty','wall','visited','wall']
# after moving forward 30 pixels
m.travelForward(30)
assert m.surroundings() == ['empty','wall','visited','wall'],m.surroundings()

# test that we stop at the branch going north
moveTo(m.t,25,187)
m.image = makePicture('maze.jpg')
m.t.setHeading(0)
m.travel2BranchOrWall()
assert m.t.getYPos()==105, 'did not stop at the branch.'

# test existence of solve
# success = m.solve()

# test that we can solve it from the easy location just above the cheese
penUp(m.t)
moveTo(m.t,377,143)
turnToFace(m.t,377,183)
penDown(m.t)
assert m.solve() == true, 'did not solve above the cheese.'

# test that we can solve if the turtle is above the cheese and has to travel.
m.image = makePicture('maze.jpg')
penUp(m.t)
moveTo(m.t,377,93)
m.t.setHeading(180)
penDown(m.t)
m.travelForward(10)
# printNow(m.surroundings())
assert m.solve() == true, 'did not solve from above the cheese.'

# test that we turn our green path to red when we travel over it
m.image = makePicture('maze.jpg')
penUp(m.t)
moveTo(m.t,25,187)
m.t.setHeading(90)
penDown(m.t)
m.travelForward(30)
turnRight(m.t)
turnRight(m.t)
m.travelForward(30)
turnRight(m.t)
turnRight(m.t)
assert m.colorInFront() == red, "Didn't change color of trail."

# test starting from the isolated region, should always fail. 
m.image=makePicture('maze.jpg')
penUp(m.t)
moveTo(m.t,141,219)
m.t.setHeading(0)
penDown(m.t)
assert m.solve()==false


# test that we can solve if the turtle is above the cheese and facing north.
# penUp(m.t)
# moveTo(m.t,377,93)
# turnToFace(m.t,377,83)
# penDown(m.t)
# assert m.solve() == true, 'did not solve from above the cheese.'


#if c != white:
#  raise "Bad Color from colorInFront" 
#forward(m.t,70)
#c=m.colorInFront()
#if c != blue:
#  raise "Bad Color from colorInFront" 
#moveTo(m.t,26,182)    