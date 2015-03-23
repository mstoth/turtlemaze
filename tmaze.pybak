
# maze program by Michael Toth
setMediaPath('/Users/toth/Documents/Github/turtlemaze')
class Maze(object):
  """ Creates and solves a maze using turtles in JES. """
  def __init__(self):
    self.image = makePicture('maze.jpg')
    self.w = makeWorld(getWidth(self.image),getHeight(self.image))
    self.w.setPicture(self.image)
    self.t = makeTurtle(self.w)
    penUp(self.t)
    moveTo(self.t,25,184)
    self.t.setHeading(90)
    penDown(self.t)
    
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
assert m.t.getYPos() == 184, 'Turtle y position not correct.'

# tests for colorInFront
m=Maze()
c=m.colorInFront()
if c != white:
  raise "Bad Color from colorInFront" 
#forward(m.t,70)
#c=m.colorInFront()
#if c != blue:
#  raise "Bad Color from colorInFront" 
#moveTo(m.t,26,182)    