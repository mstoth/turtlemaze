# Maze Program Written by Michael Toth
setMediaPath('/Users/toth/Documents/GitHub/turtlemaze')
class Maze(object):
  """ Solves a maze with a turtle in JES """
  def __init__(self):
    """ Initializer, sets image """
    self.image = makePicture('maze.jpg')
    self.w = makeWorld(getWidth(self.image),getHeight(self.image))
    self.w.setPicture(self.image)
    self.t = makeTurtle(self.w)
    penUp(self.t)
    moveTo(self.t,25,184)
    m.t.setHeading(90)
    penDown(self.t)

  def reset(self):
    """ resets the turtle and image. """
    self.image = makePicture('maze.jpg')
    self.w.setPicture(self.image)
    self.t.clearPath()
    penUp(self.t)
    moveTo(self.t,25,184)
    self.t.setHeading(90)
    penDown(self.t)
    
  def colorInFront(self):
    """ Returns the color 11 pixels in front of the turtle. """
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
      
  def travel2BranchOrWall(self):
    """ Moves the mouse to the next occurrance of a branch or a wall. """
    if self.colorInFront() == white:
      while self.colorInFront() == white:
        forward(m.t,1)






# Tests Follow This Line

doTests = true
if doTests:
  # First Test
  m=Maze()
  if m.__class__ == Maze:
    printNow("Test 1 passed, Maze exists.")
  else:
    printNow("Test 1 failed. Maze does not exist.")
  
  # Second Test, Test for image
  if m.image.__class__ == Picture:
    printNow("Test 2 passed, Image exists.")
  else:
    printNow("Test 2 failed, Image does not exist.")
  
  # Third test.  Test for existence of the turtle 'world'. 
  try: 
    if m.w.__class__ == World:
      printNow("Test 3 passed, World exists.")
      # m.w.hideFrame()
  except:
    printNow("Test 3 failed, World does not exist.")
  
  # Test 4: Test for maze.jpg as background image
  try:
    if m.w.getPicture().fileName[-8:] == 'maze.jpg':
      printNow("Test 4 passed, world picture is maze.jpg")
    else:
      printNow("Test 4 failed, world picture is " + m.w.getPicture().fileName)
  except:
    printNow("Test 4 failed, unable to get file name.")
    
  # Test 5: Check for turtle.
  try:
    if m.t.__class__ == Turtle:
      printNow("Test 5 passed, turtle exists.")
    else:
      printNow("Test 5 failed, turtle does not exist.")
  except:
    printNow("Test 5 failed, unable to access turtle.")
    
  # Test 6: Check for turtle in proper starting location
  if m.t.getXPos() == 25 and m.t.getYPos() == 184: 
    printNow("Test 6 passed, turtle is in the correct position.")
  else:
    printNow("Test 6 failed, turtle is not in the correct starting position.")
    
  # Test 7: Check for colorInFront. It should return None 
  if dir(m).index('colorInFront') > 0:
    printNow("Test 7 passed, colorInFront exists.")
  else:
    printNow("Test 7 failed, colorInFront does not exist")
    
  # Test 8: Check that colorInFront returns white
  if m.colorInFront() == white:
    printNow("Test 8 passed, colorInFront returns white.")
  else:
    printNow("Test 8 failed, colorInFront does not return white.")
    
  
  # Test 9: Check that colorInFront returns blue when facing a wall
  turnLeft(m.t)
  if m.colorInFront() == blue:
    printNow("Test 9 passed, colorInFront is blue when facing a wall.")
  else:
    printNow("Test 9 failed, colorInFront returned " + str(m.colorInFront()))
    
  # Test 10: Check for existence of travel2BranchOrWall
  try:
    if dir(m).index('travel2BranchOrWall') > 0:
      printNow("Test 10 passed, travel2BranchOrWall exists.")
    else:
      printNow("Test 10 failed, travel2BranchOrWall does not exist")
  except:
    printNow("Test 10 failed, travel2BranchOrWall does not exist.")

  # Test 11: Check for existence of reset
  try:
    if dir(m).index('reset') > 0:
      printNow("Test 11 passed, reset exists.")
    else:
      printNow("Test 11 failed, reset does not exist")
  except:
    printNow("Test 11 failed, reset does not exist.")
    
  # Test 12: Check that reset puts the turtle at 25,184 facing north. 
  m.reset()
  assert m.t.getXPos() == 25, "Test 12 failed, x position is " + str(m.t.getXPos())
  assert m.t.getYPos() == 184, "Test 12 failed, y position is " + str(m.t.getYPos())
  assert m.t.getHeading() == 90, "Test 12 failed, heading is " + str(m.t.getHeading())
  printNow("Test 12 passes, x,y, and heading are correct after reset.")
  
  # Test 13: Check that we travel to wall after travel2BranchOrWall
  m.travel2BranchOrWall()
  if m.t.getXPos() != 101:
    printNow("Test 13 failed, x position is " + str(m.t.getXPos()))
  elif m.t.getYPos() != 184: 
    printNow("Test 13 failed, x position is " + str(m.t.getYPos()))
  else:
    printNow("Test 13 passed.")
  
  # Test 14: Check travel2BranchOrWall going north
  m.reset()
  turnLeft(m.t)
  m.travel2BranchOrWall()
  if m.t.getXPos() != 25: 
    printNow("Test 14 failed, x position is " + str(m.t.getXPos()))
  elif m.t.getYPos() != 105:
    printNow("Test 14 failed, y position is " + str(m.t.getYPos()))
  else:
    printNow("Test 14 passed.")
    
    
  