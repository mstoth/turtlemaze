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
    penDown(self.t)

  def colorInFront(self):
    """ Returns the color 9 pixels in front of the turtle. """
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