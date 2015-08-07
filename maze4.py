# Maze Program Written by Michael Toth
setMediaPath('/Users/toth/Documents/Github/turtlemaze')
import time
import random

class Maze(object):
  """ Solves a maze with a turtle in JES """
  def __init__(self):
    """ Initializer, sets image """
    self.image = makePicture('maze.jpg')
    self.w = makeWorld(getWidth(self.image),getHeight(self.image))
    self.w.setPicture(self.image)
    self.t = makeTurtle(self.w)
    self.home()
    self.endSound = makeSound('end.wav')
    self.searchSound = makeSound('searching.wav')
    self.soundOn=false

  def home(self):
    penUp(self.t)
    moveTo(self.t,30,190)
    self.t.setHeading(90)
    
  def clear(self):
    """ sets the maze to all walls """
    for col in range(0,420,20):
      for row in range(0,300,20):
        addRectFilled(self.image,col,row,20,20,blue)
    addRectFilled(self.image,20,180,20,20,white)
    self.w.hide()
    self.w.show()
    
  def reset(self):
    """ resets the turtle and image. """
    self.image = makePicture('maze.jpg')
    self.w.setPicture(self.image)
    self.t.clearPath()
    penUp(self.t)
    moveTo(self.t,30,190)
    self.t.setHeading(90)
    penDown(self.t)
    
  def find_space(self):
    ''' finds 9x9 all blue area '''
    for col in range(30,getWidth(self.image),20):
      printNow(col)
      for row in range(30,getHeight(self.image),20):
        empty=true
        for dx in range(-20,40,20):
          for dy in range(-20,40,20):
            if col+dx>=0 and col+dx<420 and row+dy>=0 and row+dy<300:
              p=getPixel(self.image,col+dx,row+dy)
              if getColor(p)!=blue:
                empty=false
        if empty:
          return (col,row)
          
  def dig(self,through=false):
    """ 
    digs in the current direction and returns true if successful 
    if through is true, it will dig through to existing paths
    """
    if self.colorInFront() != blue:
      #printNow("color in front is " + str(self.colorInFront()))
      return false
    x=getXPos(self.t)
    y=getYPos(self.t)
    x=x-10
    y=y-10
    h=self.t.getHeading()
    #printNow(str(x)+","+str(y)+" "+str(h))
    if h==0:
      y=y-20; yy=y-20; xx=x
      if xx<=0 or yy<=0:
        return false
      if not through:
        if getColor(getPixelAt(self.image,xx-20,yy))!=blue:
          return false
        if getColor(getPixelAt(self.image,xx+20,yy))!=blue:
          return false
        if getColor(getPixelAt(self.image,xx-20,y))!=blue:
          return false
        if getColor(getPixelAt(self.image,xx+20,y))!=blue:
          return false
    if h==90 or h==-270:
      x=x+20; xx=x+20; yy=y
      if not through:
        try:
          if getColor(getPixelAt(self.image,xx,yy-20))!=blue:
            #printNow(str(x)+","+str(y))
            #printNow(getColor(getPixelAt(self.image,xx,yy-20)))
            return false
          if getColor(getPixelAt(self.image,xx,yy+20))!=blue:
            #printNow(str(x)+","+str(y))
            #printNow(getColor(getPixelAt(self.image,xx,yy+20)))
            return false
          if getColor(getPixelAt(self.image,x,yy-20))!=blue:
            #printNow(str(x)+","+str(y))
            #printNow(getColor(getPixelAt(self.image,x,yy-20)))
            return false
          if getColor(getPixelAt(self.image,x,yy+20))!=blue:
            #printNow(str(x)+","+str(y))
            #printNow(getColor(getPixelAt(self.image,xx,yy+20)))
            return false
        except:
          print "."
          # do nothing
    if h==180 or h==-180:
      y=y+20; yy=y+20; xx=x
      if not through:
        try:
          if getColor(getPixelAt(self.image,xx-20,yy))!=blue:
            return false
          if getColor(getPixelAt(self.image,xx+20,yy))!=blue:
            return false
          if getColor(getPixelAt(self.image,xx-20,y))!=blue:
            return false
          if getColor(getPixelAt(self.image,xx+20,y))!=blue:
            return false
        except:
          print "."
          # return false
    if h==-90 or h==270:
      x=x-20; xx=x-20; yy=y
      if not through:
        try:
          if getColor(getPixelAt(self.image,x,yy-20))!=blue:
            #printNow(getColor(getPixelAt(self.image,x,yy-20)))
            return false
          if getColor(getPixelAt(self.image,x,yy+20))!=blue:
            #printNow(getColor(getPixelAt(self.image,x,yy+20)))
            return false
          if getColor(getPixelAt(self.image,xx,yy-20))!=blue:
            #printNow(getColor(getPixelAt(self.image,xx,yy-20)))
            return false
          if getColor(getPixelAt(self.image,xx,yy+20))!=blue:
            #printNow(getColor(getPixelAt(self.image,xx,yy+20)))
            return false
        except:
          print "."
          # return false
    if x<=0 or x>=420 or y<=0 or y>=280:
      return false
    if xx<=0 or xx>=420 or yy<=0 or yy>=280:
      return false
    if getColor(getPixelAt(self.image,xx,yy))==white:
      return false
    addRectFilled(self.image,x,y,20,20,white)
    self.w.hide()
    self.w.show()
    return true
  
  def makePathFrom(self,t):
    ''' t is a tuple specifying a starting location surrounded by walls. '''
    self.t.moveTo(t[0],t[1])
    addRectFilled(self.image,t[0]-10,t[1]-10,20,20,white)
    ntimes=0
    while self.colorInFront()!=white and ntimes<1000:
      ntimes=ntimes+1
      dx=random.randint(-3,5)
      dy=random.randint(-3,5)
      if dx<0: # direction is west
        self.t.setHeading(-90)
      else:
        self.t.setHeading(90)
      while dx!=0 and self.colorInFront()!=white:
        if dx<0:
          dx=dx+1
        elif dx>0:
          dx=dx-1
        self.dig(through=true)
        self.move()
      if dy<0: # direction is north
        self.t.setHeading(0)
      else:
        self.t.setHeading(180)
      while dy!=0 and self.colorInFront()!=white:
        if dy<0:
          dy=dy+1
        elif dy>0:
          dy=dy-1
        self.dig(through=true)
        self.move()
    if ntimes>=1000:
      return false
    else:
      return true

            
  def makePath(self,mark_end=True):
    ''' makes a path to the right hand wall '''
    ntimes=0
    while self.t.getXPos() < 380 and ntimes<1000:
      ntimes=ntimes+1
      dx=random.randint(-3,5)
      dy=random.randint(-3,5)
      if dx<0: # direction is west
        self.t.setHeading(-90)
      else:
        self.t.setHeading(90)
      while dx!=0:
        if dx<0:
          dx=dx+1
        elif dx>0:
          dx=dx-1
        self.dig()
        self.move()
      if dy<0: # direction is north
        self.t.setHeading(0)
      else:
        self.t.setHeading(180)
      while dy!=0:
        if dy<0:
          dy=dy+1
        elif dy>0:
          dy=dy-1
        self.dig()
        self.move()
    if ntimes>=1000:
      return false
    else:
      x=self.t.getXPos()+10
      y=self.t.getYPos()-10
      if mark_end:
        addRectFilled(self.image,x,y,20,20,yellow)
      return true
        
  def move(self):
    ''' moves without painting '''
    if self.colorInFront()!=white:
      return false
    self.t.forward(20)
    return true
      
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
    try:
      c = getColor(getPixelAt(self.image,xpos,ypos))
    except:
      return blue
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
    return blue # assume wall if uncertain
      
  def travel2BranchOrWall(self):
    """ Moves the mouse to the next occurrance of a branch or a wall. """
    if self.surroundings().count(white) > 1: 
      while self.surroundings().count(white) > 1: 
        self.forward(1)
        
    if self.colorInFront() == white:
      while self.colorInFront() == white and self.surroundings().count(white) == 1:
        self.forward(1)
    if self.surroundings().count(white) > 1: 
      if self.soundOn:
        play(self.searchSound)
      time.sleep(0.6)
      self.forward(9)
      
  def forward(self,dist):
    while dist > 0:
      if self.colorInFront() == green:
        addOvalFilled(self.image,self.t.getXPos()-10,self.t.getYPos()-10,20,20,red)
      else:
        addOvalFilled(self.image,self.t.getXPos()-10,self.t.getYPos()-10,20,20,green)
      dist = dist - 1
      forward(self.t,1)
      
  def surroundings(self):
    s=[]
    for i in range(4):
      s.append(self.colorInFront())
      turn(self.t)
    return s

  def turnOnSound(self):
    self.soundOn=true
    
  def turnOffSound(self):
    self.soundOn=false
    
  def solveFrom(self,xpos,ypos,hdg):
    penUp(self.t)
    moveTo(self.t,xpos,ypos)
    self.t.setHeading(hdg)
    penDown(self.t)
    self.solve()
   
  def solve(self,xpos=30,ypos=190,hdg=90):
    if self.colorInFront() == yellow:
      if self.soundOn:
        play(self.endSound)
      return true
    for i in range(4):
      if self.colorInFront()==yellow:
        return true
      if self.colorInFront()==white:
        saveX = m.t.getXPos()
        saveY = m.t.getYPos()
        saveH = m.t.getHeading()
        self.travel2BranchOrWall()
        if self.solve():
          return true
        else:
          penUp(self.t)
          turnToFace(self.t,saveX,saveY)
          d=sqrt((self.t.getXPos()-saveX)**2+(self.t.getYPos()-saveY)**2)
          penDown(self.t)
          self.forward(d)
          self.t.setHeading(saveH)
      self.t.turnRight()
    return false

  def create(self):  
    m.t.penUp()
    m.clear()
    m.makePath()
    m.t.moveTo(30,190)
    m.t.setHeading(90)

    
    
    
    
# Tests Follow This Line

if true:
  m=Maze()
  m.clear()
  assert(m.find_space()!=None)
  printNow("find_space is ok")
  printNow(str(m.find_space()))
  
  m.create()
  s=m.find_space()
  while s!=None:
    m.makePathFrom(s)
    s=m.find_space()
  m.home()
  m.solve()

if false:
  # we should be able to dig to second-to-last column
  m=Maze()
  m.clear()
  addRectFilled(m.image,360,180,20,20,white)
  m.t.moveTo(370,190)
  m.t.setHeading(90)
  assert(m.dig())
   # we want to draw a maze. 
  # blank the screen
  m=Maze()
  m.reset()
  m.clear()
  if m.colorInFront() == blue:
    printNow("Test 20 passed")
  else:
    printNow("Test 20 failed, color should be blue in front after clear.")
  
  # our current position should be white. 
  if getColor(getPixelAt(m.image,getXPos(m.t),getYPos(m.t))) != white:
    printNow("Test 21 failed, not white at home location")
  else:
    printNow("Test 21 passed.")
  
  # we should not be able to move
  assert(m.move()==false)
  
  # we should be able to dig
  assert(m.dig())
  
  # we should be able to move
  assert(m.move())
  
 
  # insure a wall separates previous trails from current dig
  m=Maze()
  m.clear()
  addRectFilled(m.image,60,180,20,20,white)
  m.w.hide(); m.w.show()
  assert(m.dig()==false)
  m.clear()
  addRectFilled(m.image,60,200,20,20,white)
  m.w.hide(); m.w.show()
  assert(m.dig()==false)
  m.clear()
  addRectFilled(m.image,60,160,20,20,white)
  m.w.hide(); m.w.show()
  assert(m.dig()==false)
  
  # make a path to the right hand side
  m=Maze()
  m.clear()
  m.t.penUp()
  assert(m.makePath()==true)
  m.t.moveTo(30,190)
  m.t.setHeading(90)
  m.solve()
  
doTests = false
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
  if m.t.getXPos() == 30 and m.t.getYPos() == 190: 
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
    
  # Test 12: Check that reset puts the turtle at 30,190 facing north. 
  m.reset()
  assert m.t.getXPos() == 30, "Test 12 failed, x position is " + str(m.t.getXPos())
  assert m.t.getYPos() == 190, "Test 12 failed, y position is " + str(m.t.getYPos())
  assert m.t.getHeading() == 90, "Test 12 failed, heading is " + str(m.t.getHeading())
  printNow("Test 12 passed, x,y, and heading are correct after reset.")
  
  # Test 13: Check that we travel to wall after travel2BranchOrWall
  m.reset()
  m.travel2BranchOrWall()
  if m.t.getXPos() != 109:
    printNow("Test 13 failed, x position is " + str(m.t.getXPos()))
  elif m.t.getYPos() != 190: 
    printNow("Test 13 failed, y position is " + str(m.t.getYPos()))
  else:
    printNow("Test 13 passed.")
  
  # Test 14: Check travel2BranchOrWall going north
  m.reset()
  turnLeft(m.t)
  m.travel2BranchOrWall()
  if m.t.getXPos() != 30: 
    printNow("Test 14 failed, x position is " + str(m.t.getXPos()))
  elif m.t.getYPos() != 110:
    printNow("Test 14 failed, y position is " + str(m.t.getYPos()))
  else:
    printNow("Test 14 passed.")
  
  # Test 15: Check that we are leaving a green trail
  m.reset()
  m.forward(30)
  m.t.setHeading(-90)
  if m.colorInFront() != green:
    printNow("Test 15 failed, color is not green but " + str(m.colorInFront()))
  else:
    printNow("Test 15 passed")
  
  # Test 16: Checks that surroundings passes back [white,blue,blue,white]
  m.reset()
  if m.surroundings() != [white,blue,blue,white]:
    printNow("Test 16 failed, surroundings returned " + str(m.surroundings()))
  else:
    printNow("Test 16 passed.")
  
  
  # Test 17: Check for solve when turtle is at the cheese
  m.reset()
  penUp(m.t)
  moveTo(m.t,390,155)
  m.t.setHeading(180)
  if m.solve():
    printNow("Test 17 passed")
  else:
    printNow("Test 17 failed")
    
  # Test 18: Check for solve returning false from 150,230
  m.reset()
  penUp(m.t)
  moveTo(m.t,150,230)
  m.t.setHeading(0)
  if m.solve(): 
    printNow("Test 18 failed, returned true")
  else:
    printNow("Test 18 passed.")
    
  # Test 19: Check for a red trail
  m.reset()
  m.forward(50)
  m.t.setHeading(-90)
  m.forward(50)
  m.t.setHeading(90)
  if m.colorInFront() == red:
    printNow("Test 19 passed")
  else:
    printNow("Test 19 failed, expected red but got " + str(m.colorInFront())) 
  # Test xx: Check that surroundings returns ['empty','wall','wall','empty'] after reset
  # m.reset()
  # if m.surroundings() != ['empty','wall','wall','empty']:
  #   printNow("Test 15 failed, surroundings returned " + str(m.surroundings()))
  # else:
  #   printNow("Test 15 passed, surroundings are correct")
  
