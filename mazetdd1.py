# MAZE PROGRAM 
# Michael Toth
# 
# This program will create a maze and solve it. 
# 

import random

MAZE_WIDTH=80
MAZE_HEIGHT=80
CELL_SIZE=10

# states of a location
EMPTY=0
WALL=1
VISITED=2
END=3
REVISITED=4

# directions
UP=0
DOWN=1
LEFT=2
RIGHT=3

class Maze:
  ''' A class to create and solve a maze.  '''
  def __init__(self):
    self.width=MAZE_WIDTH*CELL_SIZE
    self.height=MAZE_HEIGHT*CELL_SIZE
    self.reset()
    
  def reset(self):
    self.image=makeEmptyPicture(self.width,self.height,blue)
    addRectFilled(self.image,CELL_SIZE,CELL_SIZE,CELL_SIZE,CELL_SIZE,white)
    self.matrix = [[WALL for x in range(MAZE_WIDTH)] for y in range(MAZE_HEIGHT)]
    self.matrix[1][1]=EMPTY # empty cell at starting point. 
    self.location = (1,1)
    
  def draw(self):
    repaint(self.image)
    
  def dig(self,direction):
    # get our new coordinate for convenience (x,y)
    if direction==UP or direction==DOWN:
      x=self.location[0]
      if direction==UP:
        y=self.location[1]-1 # up
      else:
        y=self.location[1]+1 # down
    if direction==LEFT or direction==RIGHT:
      y=self.location[1]
      if direction==LEFT:
        x=self.location[0]-1 # left
      else:
        x=self.location[0]+1 # right
    if x==0 or y==0 or x==(self.width/CELL_SIZE)-1 or y==(self.height/CELL_SIZE)-1:
      return False
      
    addRectFilled(self.image,CELL_SIZE*x,\
      CELL_SIZE*y,CELL_SIZE,CELL_SIZE,white)
    self.matrix[x][y]=EMPTY
    return True
  
  def move(self,direction):
    if direction==RIGHT:
      if self.matrix[self.location[0]+1][self.location[1]]==EMPTY:
        self.location=(self.location[0]+1,self.location[1])
    if direction==LEFT:
      if self.matrix[self.location[0]-1][self.location[1]]==EMPTY:
        self.location=(self.location[0]-1,self.location[1])
    if direction==UP:
      if self.matrix[self.location[0]][self.location[1]-1]==EMPTY:
        self.location=(self.location[0],self.location[1]-1)
    if direction==DOWN:
      if self.matrix[self.location[0]][self.location[1]+1]==EMPTY:
        self.location=(self.location[0],self.location[1]+1)
    return self.location
  
  def make_path(self,addGold=True):
    while self.location[0]<(self.width/CELL_SIZE)-2 and self.location[1]<(self.height/CELL_SIZE)-2:
      dx=random.randint(5,15)
      dy=random.randint(5,15)
      while dx>0:
        dx=dx-1
        if self.dig(RIGHT):
          self.move(RIGHT)
      while dy>0:
        dy=dy-1
        if self.dig(DOWN):
          self.move(DOWN)
    if self.location[0]==(self.width/CELL_SIZE)-2:
      self.location=(self.location[0]+1,self.location[1])
    else:
      self.location=(self.location[0],self.location[1]+1)
    if addGold:
      addRectFilled(self.image,self.location[0]*CELL_SIZE,\
            self.location[1]*CELL_SIZE,CELL_SIZE,CELL_SIZE,yellow)
      self.matrix[self.location[0]][self.location[1]]=END
  
  def make_fill(self,direction):
    if direction==RIGHT:
      dx=random.randint(5,10)
      while dx>0 and self.dig(RIGHT):
        dx=dx-1
        self.move(RIGHT)
  
  def travel(self,direction):
    if direction==RIGHT:  
      while self.matrix[self.location[0]+1][self.location[1]]==EMPTY:
        self.move(RIGHT)
      return (self.location[0],self.location[1])
    if direction==DOWN:  
      while self.matrix[self.location[0]][self.location[1]+1]==EMPTY:
        self.move(DOWN)
      return (self.location[0],self.location[1])
    if direction==LEFT:  
      while self.matrix[self.location[0]-1][self.location[1]]==EMPTY:
        self.move(LEFT)
      return (self.location[0],self.location[1])
    if direction==UP:  
      while self.matrix[self.location[0]][self.location[1]-1]==EMPTY:
        self.move(UP)
      return (self.location[0],self.location[1])
  
  
  
  
# TESTS
#
# Change this to false to turn off testing.
if true: # then we want tests. 
  m=Maze() # create the maze
  # m.draw()
  img=m.image
  
  # check for white square at home location
  p=getPixel(m.image,CELL_SIZE,CELL_SIZE)
  assert getColor(p)==white, "Error: Home Location Not White."
  # check that location 1,1 is empty
  assert m.matrix[1][1]==0, "Location 1,1 should be empty."
  # get our location
  assert m.location == (1,1), "Location should be (1,1)" 
  
  # try to dig to the right
  assert m.dig(RIGHT), "Should be able to dig to the right."
  p=getPixel(m.image,2*CELL_SIZE,CELL_SIZE)
  assert getColor(p)==white, "Error: cell should be white after digging."
  assert m.matrix[m.location[0]+1][m.location[1]]==EMPTY,"Cell to the right should be empty." 
  # try to dig down
  assert m.dig(DOWN), "Should be able to dig down."
  p=getPixel(m.image,CELL_SIZE,2*CELL_SIZE)
  assert getColor(p)==white, "Error: cell should be white after digging."
  assert m.matrix[m.location[0]][m.location[1]+1]==EMPTY,"Cell to the right should be empty." 
  # try to dig to the left
  assert not m.dig(LEFT), "Should not be able to dig left."
  p=getPixel(m.image,0,CELL_SIZE)
  assert getColor(p)==blue, "Error: cell should be white after digging."
  assert m.matrix[m.location[0]-1][m.location[1]]==WALL,"Cell to the right should be empty." 
  # try to dig up
  assert not m.dig(UP), "Should not be able to dig up."
  p=getPixel(m.image,CELL_SIZE,0)
  assert getColor(p)==blue, "Error: cell should be white after digging."
  assert m.matrix[m.location[0]][m.location[1]-1]==WALL,"Cell to the right should be empty." 
  
  # test other two boundaries
  x=1; y=(m.height/CELL_SIZE)-2
  m.location=(x,y)
  assert not m.dig(DOWN), "Should not be able to dig down" 
  x=(m.width/CELL_SIZE)-2; y=1
  m.location=(x,y)
  assert not m.dig(RIGHT), "Should not be able to dig right" 
  
  # test we can reset the maze. 
  m.reset()
  assert m.location==(1,1), "Location after reset is not (1,1)"
  assert m.matrix[1][1]==EMPTY, "Loation 1,1 not empty after reset"
  assert m.matrix[2][1]==WALL, "Location 2,1 not a wall after reset"
  
  # test that we can move after digging
  m.dig(RIGHT)
  assert m.move(RIGHT)==(2,1),"We should get new coordinates from moving"
  assert m.location==(2,1),"Should be in a new cell after moving"
  
  # test that we can't move into a wall
  m.reset()
  assert m.move(RIGHT)==(1,1), "We should not be able to move after reset"
  
  # test the other 3 directions
  assert m.move(DOWN)==(1,1), "We should not be able to move down after reset"
  assert m.move(LEFT)==(1,1), "We should not be able to move left after reset"
  assert m.move(UP)==(1,1), "We should not be able to move right after reset"
  
  # test we can dig to the right border
  m.reset()
  while m.dig(RIGHT):
    m.move(RIGHT)
  assert m.location[0]==(m.width/CELL_SIZE)-2
  
  # test we can dig to the lower border
  m.reset()
  while m.dig(DOWN):
    m.move(DOWN)
  assert m.location[1]==(m.height/CELL_SIZE)-2
  
  # test we can make a path
  m.reset()
  m.make_path()
  assert m.location[0]==(m.width/CELL_SIZE)-1 or \
         m.location[1]==(m.height/CELL_SIZE)-1, "end point not on boundary"
  
  # test for the pot of gold.
  p=getPixel(m.image,m.location[0]*CELL_SIZE,m.location[1]*CELL_SIZE)
  assert getColor(p)==yellow, "Pot of gold not found." 
  
  # test location is correct. 
  assert m.matrix[m.location[0]][m.location[1]]==END
  # m.draw()
  
  # test travelling east
  m.reset()
  # make a right hand turn
  for i in range(10):
    m.dig(RIGHT)
    m.move(RIGHT)
  for i in range(10):
    m.dig(DOWN)
    m.move(DOWN)
  m.location=(1,1)
  assert m.travel(RIGHT)==(11,1), "We didn't get to the right hand turn." 
  # test travelling down
  assert m.travel(DOWN)==(11,11), "We didn't get to the lowest point." 
  # test travelling up
  assert m.travel(UP)==(11,1), "We didn't get to the lowest point." 
  # test travelling left
  assert m.travel(LEFT)==(1,1), "We didn't get to the lowest point." 
  
  # make an environment for make_fill()
  m.reset()
  for i in range(10):
    m.dig(RIGHT)
    m.move(RIGHT)
  for i in range(2):
    m.dig(DOWN)
    m.move(DOWN)
  for i in range(3):
    m.dig(RIGHT)
    m.move(RIGHT)
  for i in range(2):
    m.dig(UP)
    m.move(UP)
  m.location=(11,1)
  m.make_fill(RIGHT)
  assert m.matrix[12][1]==EMPTY
    