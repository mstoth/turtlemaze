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

  def clear_in_front(self,x,y,d):
    ''' checks to see if the path is clear up front '''
    if d==EAST:
      xx=x+1; xxx=x+2; yy=y; yy1=y-1; yy2=y+1
      if self.state(xx,yy)==WALL and self.state(xx,yy1)==WALL and \
          self.state(xx,yy2)==WALL and self.state(xxx,yy)==WALL and \
          self.state(xxx,yy1)==WALL and self.state(xxx,yy2)==WALL:
        return true
      else:
        return false
        
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
      xxx=xx+1; yyy=yy
    elif d==SOUTH:
      xx=self.path.x; yy=self.path.y+1
      yyy=yy+1; xxx=xx
    elif d==NORTH:
      xx=self.path.x; yy=self.path.y-1
      yyy=yy-1; xxx=xx
    elif d==WEST:
      xx=self.path.x-1; yy=self.path.y
      xxx=xx-1; yyy=yy
    else:
      assert False,"ERROR IN DIG, DIRECTION IS " + str(d)
    if xx<1 or xx>98 or yy<1 or yy>98:
      return False
    if xxx<1 or xxx>98 or yyy<1 or yyy>98:
      return False
    if self.state(xxx,yyy)!=WALL:
      return False
    if self.state(xx,yy)!=WALL:
      return False
    self.set_block(xx,yy,EMPTY)
    return True
    
  def set_block(self,x,y,s):
    ''' sets the block at x,y to be state s '''
    if s==WALL:
      addRectFilled(self.w.picture,x*10,y*10,10,10,blue)
    if s==END:
      addRectFilled(self.w.picture,x*10,y*10,10,10,yellow)
    elif s==EMPTY:
      addRectFilled(self.w.picture,x*10,y*10,10,10,white)
    elif s==VISITED:
      addRectFilled(self.w.picture,x*10,y*10,10,10,green)
    elif s==REVISITED:
      addRectFilled(self.w.picture,x*10,y*10,10,10,red)
    self.matrix[x][y]=s
    
    self.matrix[x][y]=s
  def clear(self):
    for x in range(100):
      for y in range(100):
        self.set_block(x,y,WALL)
    self.set_block(1,1,EMPTY)
    self.path.x=1
    self.path.y=1
    
  def draw(self):
    self.w.showFrame()
  
  def draw_random_path(self,mark_end=False):
    ntimes=0
    while self.path.x<97 and self.path.y<97 and ntimes < 100:
      ntimes=ntimes+1
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
      if mark_end:
        if self.path.x==97:
          self.set_block(98,self.path.y,EMPTY)
          self.set_block(99,self.path.y,END)
        if self.path.y==97:
          self.set_block(self.path.x,98,EMPTY)
          self.set_block(self.path.x,99,END)
    return True  
  
  
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
  m.set_block(4,1,EMPTY)
  assert(m.matrix[3][1]==WALL)
  assert(m.matrix[4][1]==EMPTY)
  assert(m.dig(EAST)==False)
  # m.draw()
  
  # TEST MOVING
  assert(m.move(EAST)==(2,1))
  assert(m.dig(SOUTH)==True)
  assert(m.move(SOUTH)==(2,2))
  assert(m.move(SOUTH)==(2,2)) # can't move further
  
  # TEST CLEAR-IN-FRONT TEST
  m.clear()
  assert(m.clear_in_front(1,1,EAST)==True)
  
  # TEST MAKING PATH
  m.clear()
  m.draw_random_path(mark_end=True)
  m.draw()
  assert(m.path.x==97 or m.path.y==97)

