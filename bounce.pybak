import random
import time
w=makeWorld(200,200)
t=makeTurtle(w)
while 0:
  while t.getXPos() > 5 and t.getXPos() < 195 and t.getYPos() > 5 and t.getYPos() < 195:
    forward(t,1)
    time.sleep(0.01)
  turn(t,180)
  turn(t,random.randint(-5,5))
  forward(t,2)
  
  
def rev(s):
  if (len(s)>1):
    rev(s[1:len(s)]);
  print(s[0]);
