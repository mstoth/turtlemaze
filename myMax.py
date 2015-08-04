# myMax(a,b) returns the maximum of a and b and throws an
# exception if a or b is not a number
def colorWheel(angle):
  assert angle >= 0
  assert angle <= 360
  
  if angle < 60:
    r=255
    b=0
    g=255*angle/60
  if angle >= 60 and angle < 120:
    g = 255
    b = 0
    r = 255-(255*(angle-60)/60)
  if angle >= 120 and angle < 180:
    g = 255
    r = 0
    b = 255*(angle-120)/60
  if angle >= 180 and angle < 240:
    b = 255
    r = 0
    g = 255-(255*(angle-180)/60)
  if angle >= 240 and angle < 300:
    b = 255
    g = 0
    r = 255*(angle-240)/60
  if angle >= 300 and angle < 360: 
    r = 255
    g = 0
    b = 255-(255*(angle-300)/60)
  return makeColor(r,g,b)
  
  
def drawColorWheel():
  w = makeWorld(200,200)
  t = makeTurtle(w)
  t.setPenWidth(4)
  
  for angle in range(360):
    t.setPenColor(colorWheel(angle))
    forward(t,100)
    turnRight(t)
    turnRight(t)
    forward(t,100)
    turnRight(t)
    turnRight(t)
    turn(t,1)

  
def myMax(a,b):
  if a.__class__ == str or b.__class__ == str:
    raise TypeError
  if a > b:
    return a
  else:
    return b
  
# Test 1: Verify we get a number from myMax
assert myMax(1,2).__class__ == int, "Test 1 failed, value returned is not an integer \
   (returned " + str(myMax(1,2).__class__) + ")"

# Test 2: Verify we get 0 for myMax(0,0)
assert myMax(0,0) == 0, "Test 2 failed, value returned is " + str(myMax(0,0))

# Test 3: Verify we get 1 for myMax(1,0)
assert myMax(1,0) == 1, "Test 3 failed, value returned is " + str(myMax(1,0))

# Test 4: Verify we get 1 for myMax(0,1)
assert myMax(0,1) == 1, "Test 4 failed, value returned is " + str(myMax(0,1))

# Test 5: Verify with negative numbers
assert myMax(0,-1) == 0, "Test 5 failed, value returned is " + str(myMax(0,-1))
assert myMax(-1,0) == 0, "Test 5 failed, value returned is " + str(myMax(0,-1))

# Test 6: Verify we get a TypeError when passing in a character
try: 
  r = myMax('a','b')
  printNow("Test 6 failed. No TypeError.")
except TypeError:
  pass
try: 
  r = myMax(0,'b')
  printNow("Test 6 failed for myMax(0,'b'). No TypeError.")
except TypeError:
  pass
try: 
  r = myMax('a',0)
  printNow("Test 6 failed for myMax('a',0). No TypeError.")
except TypeError:
  pass




def removeCheese():
  setMediaPath('/Users/toth/Documents/Github/turtlemaze')
  pic=makePicture('maze.jpg')
  for col in range(getWidth(pic)):
    for row in range(getHeight(pic)):
      p=getPixelAt(pic,col,row)
      c=getColor(p)
      if distance(c,yellow) < 150:
        setColor(p,white)
  show(pic)     
  