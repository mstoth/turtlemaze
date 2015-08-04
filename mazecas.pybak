''' 
Maze program which creates a maze and solves it. 
'''

import unittest
import random

# states of a location
EMPTY=0
WALL=1
VISITED=2
END=3
REVISITED=4

# directions
NORTH=0
EAST=1
SOUTH=2
WEST=3

colors={EMPTY:white,WALL:blue,VISITED:green,END:yellow,REVISITED:red}
directions={0:'NORTH',1:'EAST',2:'SOUTH',3:'WEST'}
states={0:'EMPTY',1:'WALL',2:'VISITED',3:'END',4:'REVISITED'}

class Maze:
  ''' Class to create and solve a maze. '''
  def __init__(self):
    self.width=100
    self.height=100
    self.matrix=[[WALL for i in range(100)] for j in range(100)]
    self.matrix[1][1]=EMPTY
    self.path=Path()
    self.w = makeWorld(10*self.width,10*self.height)
    self.clear()
    self.w.hideFrame()
    
  def state(self,x,y):
    return self.matrix[x][y]

  def move(self,d,mark=True):
    ''' d is the direction to move; NORTH, SOUTH, EAST, WEST '''
    if d==EAST:
      xx=self.path.x+1; yy=self.path.y
    elif d==SOUTH:
      xx=self.path.x; yy=self.path.y+1
    elif d==NORTH:
      xx=self.path.x; yy=self.path.y-1
    elif d==WEST:
      xx=self.path.x-1; yy=self.path.y
    else:
      assert(False,"ERROR IN DIG, DIRECTION IS " + str(d))
    if xx<1 or xx>98 or yy<1 or yy>98:
      return (self.path.x,self.path.y) # CAN'T MOVE TO BORDER
    if self.state(xx,yy)==WALL:
      return (self.path.x,self.path.y) # CAN'T MOVE INTO WALL
    self.path.x=xx; self.path.y=yy
    if mark:
      if self.state(xx,yy)==EMPTY:
        self.matrix[xx][yy]=VISITED
      elif self.state(xx,yy)==VISITED:
        self.matrix[xx][yy]=REVISITED
    return (xx,yy)
    
      
  def dig(self,d):
    ''' d is the direction to dig; NORTH, SOUTH, EAST, WEST '''
    if d==EAST:
      xx=self.path.x+1; yy=self.path.y
    elif d==SOUTH:
      xx=self.path.x; yy=self.path.y+1
    elif d==NORTH:
      xx=self.path.x; yy=self.path.y-1
    elif d==WEST:
      xx=self.path.x-1; yy=self.path.y
    else:
      assert(False,"ERROR IN DIG, DIRECTION IS " + str(d))
    if xx<1 or xx>98 or yy<1 or yy>98:
      return False
    if self.state(xx,yy)!=WALL:
      return False
    self.matrix[xx][yy]=EMPTY
    addRectFilled(self.w.picture,xx*10,yy*10,10,10,white)
    return True
    
  def clear(self):
    for x in range(100):
      for y in range(100):
        addRectFilled(self.w.picture,x*10,y*10,10,10,blue)
        self.matrix[x][y]=WALL
    self.matrix[1][1]=EMPTY
    addRectFilled(self.w.picture,10,10,10,10,white)
    self.path.x=1
    self.path.y=1
    
  def draw(self):
    self.w.showFrame()
  
  def draw_random_path(self):
    while self.path.x<98 and self.path.y<98:
      printNow(self.path.x); printNow(self.path.y)
      dx=random.randint(-4,10)
      dy=random.randint(-4,10)
      while dx!=0:
        if dx<0: # move west
          self.dig(WEST)
          self.move(WEST,mark=False)
          dx=dx+1
        if dx>0: # move east
          self.dig(EAST)
          self.move(EAST,mark=False)
          dx=dx-1
      while dy!=0:
        if dy<0: # move north
          self.dig(NORTH)
          self.move(NORTH,mark=False)
          dy=dy+1
        elif dy>0: 
          self.dig(SOUTH)
          self.move(SOUTH,mark=False)
          dy=dy-1
  
  
class Path:
  ''' the path in the maze '''
  def __init__(self):
    self.start=(1,1)
    self.x=1
    self.y=1
    self.end=None





# TESTS

if True:  # change to False when no tests wanted.
  global m
  def setUp():
    global m
    m=Maze()
  setUp()
  assert(m.width==100)
  assert(m.height==100)

  # TEST STATES
  assert(m.state(1,1)==EMPTY)
  assert(m.state(2,1)==WALL)
  
  # TEST DIGGING
  assert(m.dig(EAST)==True)
  assert(m.matrix[2][1]==EMPTY)
  
  # TEST MOVING
  assert(m.move(EAST)==(2,1))
  assert(m.dig(SOUTH)==True)
  assert(m.move(SOUTH)==(2,2))
  assert(m.move(SOUTH)==(2,2)) # can't move further
  
  # TEST MAKING PATH
  m.clear()
  m.draw_random_path()
  assert(m.path.x==98 or m.path.y==98)