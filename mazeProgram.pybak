#maze program written by Alex Dwyer
setMediaPath('/Users/toth/Documents/Github/turtlemaze')
class Maze(object):
  """ solves a maze in JES """
  def __init__(self):
    """initialization"""
    self.image=makePicture('maze.jpg')
    self.w=makeWorld(getWidth(self.image), getHeight(self.image))
    self.w.setPicture(self.image)
    self.t=makeTurtle(self.w)
    moveTo(self.t,30,190)
    turnRight(self.t)
  def colorInFront(self):
    dx=11
    xpos=self.t.getXPos()
    ypos=self.t.getYPos()
    h=self.t.getHeading()
    if h==0:
     ypos=ypos-dx
    if h==90 or h==-270:
     xpos=xpos+dx
    if h==180 or h==-180:
     ypos=ypos+dx
    if h==270 or h==-90:
     xpos=xpos-dx
    c=getColor(getPixelAt(self.image, xpos, ypos))
    if distance(c,white)<150:
     return white
    if distance(c,blue) <150:
     return blue 
    if distance(c,green)<150:
     return green 
    if distance(c,yellow)<150:
     return yellow
    if distance(c, red)<150:
     return red 
    return blue
  def travel2BranchOrWall(self):
    if self.surroundings().count(white) >1:
      while self.surroundings().count(white) >1: 
        self.forward(1)
    if self.colorInFront()==white: 
      while self.colorInFront() == white and self.surroundings().count(white)==1:
        self.forward(1)
      if self.surroundings().count(white) >1: 
        forward(self.t, 8)
  def reset(self):
    self.image=makePicture("maze.jpg")
    self.w.setPicture(self.image)
    self.t.clearPath()
    penUp(self.t)
    moveTo(self.t,30,190)
    self.t.setHeading(90)
    penDown(self.t)
  def surroundings(self):
    a=[]
    for i in range(4):
      a.append(self.colorInFront())
      turn(self.t)
    return a
  def forward(self,dist):
    while dist>0: 
      if self.colorInFront()==green:
        addOvalFilled(self.image, self.t.getXPos()-10, self.t.getYPos()-10,20,20,red)
      else:
        addOvalFilled(self.image, self.t.getXPos()-10, self.t.getYPos()-10, 20, 20, green)
      dist=dist-1
      forward(self.t,1)
  def solve(self):
    if self.colorInFront() == yellow: 
      return true
    for i in range(4):
      if self.colorInFront()==white:
        saveX=m.t.getXPos()
        saveY=m.t.getYPos()
        saveH=m.t.getHeading()
        self.travel2BranchOrWall()
        if self.solve():
          return true
        else:
          penUp(self.t)
          turnToFace(self.t, saveX, saveY)
          d=sqrt((self.t.getXPos()-saveX)**2+(self.t.getYPos()-saveY)**2)
          penDown(self.t)
          self.forward(d)
          self.t.setHeading(saveH)
      turnRight(self.t)
    return false
      
      





#Tests follow this line
doTests=true
if doTests:
  #Test 1, verify we have a Maze
  m=Maze()
  if m.__class__ == Maze:
    printNow("Test 1 passed, Maze exists.")
  else: 
    printNow("Test 1 failed, Maze does not exist.")
  #Test 2, verify we have the image
  if m.image.__class__ == Picture: 
    printNow("Test 2 passed, image exists.")
  else: 
    printNow("Test 2 failed, image does not exist")
  #Test 3, verify world exists
  try: 
    if m.w.__class__ == World: 
      printNow("Test 3 passed, world exists")
  except:
     printNow("Test 3 failed, world does not exist.")
  #Test 4, verify world picture is the maze
  try:
    if m.w.getPicture().fileName[-14:] == "maze image.jpg":
      printNow("Test 4 passed, world picture is maze image.jpg")  
    else: 
      printNow("Test 4 failed, world picture is " + m.w.getPicture().fileName)
  except: 
    printNow("Test 4 failed, unable to get file name.")
  #Test 5, verify a turtle exists 
  try: 
    if m.t.__class__ == Turtle: 
      printNow("Test 5 passed, turtle exists in maze")
    else: 
      printNow("Test 5 failed, turtle is not a turtle")
  except:
    printNow("Test 5 failed, turtle does not exist in maze")
  #Test 6, Turtle is at (30,190)
  try: 
    if m.t.getXPos()==30 and m.t.getYPos()== 190:
      printNow("Test 6 passed, turtle is at (30, 190).")
    else: 
      printNow("Test 6 failed, turtle location is wrong")
  except: 
    printNow("Test 6 failed, turtle just isn't")
  #Test 7, Check for colorInFront
  if dir(m).index('colorInFront') > 0: 
    printNow("Test 7 passed, colorInFront works.")
  else: 
    printNow("Test 7 failed, colorInFront does not work")
  #Test 8, Check that color in front returns white. 
  if m.colorInFront()==white:
    printNow("Test 8 passed, turtle is facing white")
  else:
    printNow("Test 8 failed, turtle is not facing white")
  #Test 9, Check that colorInFront changes with turtle
  turnLeft(m.t)
  turnLeft(m.t)
  if m.colorInFront()==blue:
    printNow("Test 9 passed, colorInFront changes")
  else:
    printNow("Test 9 failed, colorInFront returned" +str(m.colorInFront()))
  #Test 10, Check for existance of travel2BranchOrWall
  try:
    if dir(m).index("travel2BranchOrWall") >0:
      printNow("Test 10 passed, travel2BranchOrWall exists")
    else: 
      printNow("Test 10 failed, travel2BranchOrWall does not exist")
  except:
    printNow("Test 10 failed, it blew up")
  #Test 11, Check that reset exists
    try: 
     if dir(m).index("reset") >0:
        printNow("Test 11 passed, reset exists")
     else:
        printNow("Test 11 failed, reset does not exist")
    except:
      printNow("Test 11 failed, it blew up")
  #Test 12, Check that reset puts turtle back to starting point. 
  m.reset()
  assert m.t.getXPos()==30, "Test 12 failed, x position is "+str(m.t.getXPos())
  assert m.t.getYPos()==190, "Test 12 failed, y position "+str(m.t.getYPos())
  assert m.t.getHeading()==90, "Test 12 failed, heading is "+str(m.t.getHeading())
  printNow("Test 12 passed, x,y and heading are correct after command")
  #Test 13, Check that turtle moves
  m.reset()
  m.travel2BranchOrWall()
  if m.t.getXPos() !=108:
    printNow("Test 13 failed, x position is "+ str(m.t.getXPos()))
  elif m.t.getYPos() !=190:
    printNow("Test 13 passed, y position is" + str(m.t.getYPos()))
  else:
    printNow("Test 13 passed, turtle moves")
  #Test 13b check surroundings
  m.reset()
  s=m.surroundings()
  assert s==[white, blue, blue, white]
  #Test 13c check surroundings
  m.reset()
  moveTo(m.t, 30, 110)
  m.t.setHeading(0)
  assert m.surroundings() == [white, white, white, blue], str(m.surroundings())
  #Test pre14, Check for green trail
  m.reset()
  m.t.setHeading(0)
  m.forward(80)
  assert m.surroundings() == [white, white, green, blue],"Test 14 failed, " +str(m.surroundings())
 
  
  #Test 14, Check that travel2BranchOrWall going north.
  m.reset()
  turnLeft(m.t)
  m.travel2BranchOrWall()
  if m.t.getXPos() !=30:
    printNow("Test 14 failed, x position is" + str(m.t.getXPos()))
  elif m.t.getYPos() != 110: 
    printNow("Test 14 failed, y position is" + str(m.t.getYPos()))
  else:
    printNow("Test 14 passed")
  #Test 15, Check we are leaving a green trail. 
  m.reset()
  m.forward(30)
  m.t.setHeading(-90)
  if m.colorInFront() !=green:
   printNow("Test 15 failed, color is not green but is" +str(m.colorInFront()))
  else:
   printNow("Test 15 passed.")
  #Test 16, Checks that surroundings passes back [white, blue, blue, white].
  m.reset()
  if m.surroundings() !=[white, blue, blue, white]:
   printNow("Test 16 failed, surroundings returned" +str(m.surroundings()))
  else: 
   printNow("Test 16 passed, after reset turtle is at beginning")
  #Test 17, Check for solve when turtle is at the cheese. 
  m.reset()
  penUp(m.t)
  moveTo(m.t, 390, 155)
  m.t.setHeading(180)
  if m.solve():
    printNow("Test 17 passed")
  else:
    printNow("Test 17 failed")
  #Test 18, Check for solve returning false from impossible position.
  m.reset()
  penUp(m.t)
  moveTo(m.t, 150, 230)
  m.t.setHeading(0)
  if m.solve():
    printNow("Test 18 failed, returned true")
  else:
    printNow("Test 18 passed, returned false") 
  #Test 19, Check for a red trail. 
  m.reset()
  m.forward(50)
  m.t.setHeading(270)
  m.forward(50)
  if m.colorInFront() == red:
    printNow("Test 19 passed")
  else: 
    printNow("Test 19 failed, color in front is " +str(m.colorInFront()))
 
  
  