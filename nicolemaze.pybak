# maze program by Nicole Roth
setMediaPath ("/Users/toth/Documents/Github/turtlemaze") #/Users/PC5/Documents/GitHub/maze
class Maze (object):
  """ solves a maze """
  def __init__(self):
    """ initialization """
    self.image = makePicture ("maze.jpg")
    self.w = makeWorld(getWidth (self.image), getHeight (self.image))
    self.w.setPicture(self.image)
    self.t = makeTurtle (self.w)
   
    penUp(self.t)
    moveTo (self.t, 30,190)
    penDown(self.t)
   
   
  def colorInFront(self):
    """ Returns color in front of turtle """
    dx = 11
    xpos = self.t.getXPos()
    ypos = self.t.getYPos()
   
    h = self.t.getHeading()
    if h == 0:
      ypos = ypos - dx
    if h == 90 or h == -270:
      xpos = xpos + dx
    if h == 180 or h == -180:
      ypos = ypos + dx
    if h == -90 or h == 270:
      xpos = xpos - dx
    c = getColor(getPixelAt(self.image,xpos,ypos))
    if distance(c,white) < 150:
      return white
    if distance(c,blue) < 150:
      return blue
    if distance(c,green) < 150:
      return green
    if distance(c,red) < 150:
      return red
    if distance(c,yellow) < 150:
      return yellow
    return blue

   
  def travel2BranchOrWall(self):
    """Moves turtle forward until it hits branch or gets to alternative path"""
    if self.surroundings().count(white) > 1:
      while self.surroundings().count(white) > 1:
        self.forward(1)
    if self.colorInFront() == white:
      while self.colorInFront() == white and self.surroundings().count(white) == 1:
        self.forward(1)
    if self.surroundings().count(white) > 1:
     
      self.forward(8)

  def reset(self):
    """Resets maze to original"""
    self.image = makePicture('Maze.jpg')
    self.w.setPicture(self.image)
    self.t.clearPath()
    penUp(self.t)
    moveTo(self.t, 30, 190)
    turnToFace(self.t, 35, 190)
    penDown(self.t)

  def surroundings(self):
    a = []
    for i in range (4):
      a.append(self.colorInFront())
      turn(self.t)
    return a

   
  def forward(self, dist):
    while dist > 0:
      if self.colorInFront () == green:
        addOvalFilled(self.image, self.t.getXPos()-10, self.t.getYPos()-10, 20, 20, red)
      else:
        addOvalFilled (self.image, self.t.getXPos()-10, self.t.getYPos()-10, 20, 20, green)
      dist = dist-1
      forward(self.t, 1)
      
 
  def solve (self, xpos=30, ypos=190, hdg=90):
    if self.colorInFront () == yellow:
      return true
    for i in range (4):
      if self.colorInFront() == white:
        saveX = m.t.getXPos ()
        saveY = m.t.getYPos()
        saveH = m.t.getHeading()
        self.travel2BranchOrWall()
        if self.solve():
          return true
        else:
          penUp(self.t)
          turnToFace(self.t, saveX, saveY)
          d = sqrt((self.t.getXPos () - saveX)**2 + (self.t.getYPos() - saveY)**2)
          penDown (self.t)
          self.forward(d)
          self.t.setHeading (saveH)
      self.t.turnRight()
    return false
    
   
# Tests follow here
doTests =1
if doTests:
  #Test 1, Make maze
  m=Maze()
 
  #Test 2, Make image
  if m.image.__class__ == Picture:
    printNow ("Test 2 passed, image exists.")
  else:
    printNow ("Test 2 failed, image does not exist.")
 
  #Test 3, Make world
  try:
    if m.w.__class__== World:
      printNow ("Test 3 passed, world exists.")
  except:
    printNow ("Test 3 failed, world does not exist.")
   
  #Test 4, Make image in world
 
  try:
    if m.w.getPicture().fileName[-8:] == "maze.jpg":
      printNow ("Test 4 passed, world picture is maze.jpg")
    else:
      printNow ("Test 4 failed, world picture is " + m.w.getPicture())
  except:
    printNow ("Test 4 failed, unable to get filename.")
 
  #Test 5, Check for turtle
 
  try:
    if m.t.__class__== Turtle:
      printNow ("Test 5 passed, turtle exists.")
  except:
    printNow ("Test 5 failed, turtle does not exist.")
 
  #Test 6, Check if turtle is in right starting position
 
  if m.t.getXPos() == 30 and m.t.getYPos() == 190:
    printNow ("Test 6 passed, turtle is in right starting postiion")
  else:
    printNow ("Test 6 failed, turtle is not in right starting postition.")
   
  #Test 7, Check for colorInFront
 
  if dir(m).index ('colorInFront') > 0:
    printNow ("Test 7 passed, colorInFront exists.")
  else:
    printNow ("Test 7 failed, colorInFront does not exist")
   
  #Test 8, Check that colorInFront returns white
 
  if m.colorInFront () == white:
    printNow ("Test 8 passed, colorInFront returns white")
  else:
    printNow ("Test 8 failed, colorInFront does not return white")
   
  #Test 9, Check that colorInFront returns blue when facing a wall
  turnLeft (m.t)
  turnLeft (m.t)
  if m.colorInFront () == blue:
    printNow ("Test 9 passed, colorInFront returns blue when facing wall")
  else:
    printNow ("Test 9 failed, colorInFront does not return blue when facing wall")
   
 #Test 10, Check for existence of travel2BranchOrWall
 
  try:
    if dir(m).index('travel2BranchOrWall') > 0:
      printNow ("Test 10 passed, travel2BranchOrWall exists")
    else:
       printNow ("Test 10 failed, travel2BranchOrWall does not exist")
  except:
    printNow ("Test 10 failed, travel2BranchOrWall does not exist")
   
 #Test 11, Check for existence of reset
  try:
    if dir(m).index('reset') > 0:
      printNow ("Test 11 passed, reset exists")
    else:
      printNow ("Test 11 failed, reset does not exist")
  except:
    printNow ("Test 11 failed, reset does not exist")
   
 #Test 12, Check that reset puts the turtle at 30, 190 facing east
  m.reset()
  assert m.t.getXPos() == 30 #can't get text?
  assert m.t.getYPos() == 190
  assert m.t.getHeading() == 90
  printNow ("Test 12 passed, x, y, and heading are correct after reset")
 
 #Test 13, Check that we travel to wall after travel2BranchOrWall
  m.reset()
  m.travel2BranchOrWall()
  if m.t.getXPos() != 109:
    printNow ("Test 13 failed")
  elif m.t.getYPos() != 190:
    printNow ("Test 13 failed")
  else:
    printNow ("Test 13 passed")
   
 #Test 14, Check travel2BranchOrWall going north
  m.reset()
  turnLeft(m.t)
  m.travel2BranchOrWall()
  if m.t.getXPos() != 30:
    printNow ("Test 14 failed")
  elif m.t.getYPos() != 110:
    printNow ("Test 14 failed")
  else:
    printNow ("Test 14 passed")
   
 #Test 15, Check that we are leaving a green trail
  m.reset()
  m.forward (30)
  m.t.setHeading(-90)
  if m.colorInFront () != green:
    printNow ("Test 15 failed")
  else:
    printNow ("Test 15 passed")
 #Test 16, Check if surroundings passes back (white, blue, blue, white)
  m.reset()
  if m.surroundings() != [white, blue, blue, white]:
    printNow ("Test 16 failed")
  else:
    printNow ("Test 16 passed")
 #Test 17, Check for solve when turtle is at the cheese
 
  m.reset
  penUp(m.t)
  moveTo(m.t, 390, 155)
  m.t.setHeading(180)
  if m.solve ():
    printNow ("Test 17 passed")
  else:
    printNow ("Test 17 failed")
   
 #Test 18, Check for solve returning false from 150, 230
 
  m.reset()
  penUp (m.t)
  moveTo (m.t, 150, 230)
  m.t.setHeading (0)
  if m.solve():
    printNow ("Test 18 failed, returned true")
  else:
    printNow ("Test 18 passed")
   
 #Test 19, Check for a red trail
 
  m.reset()
  m.forward(50)
  m.t.setHeading (-90)
  m.forward(50)
  m.t.setHeading (90)
  if m.colorInFront() == red:
    printNow("Test 19 passed")
  else:
    printNow ("Test 19 failed")
    