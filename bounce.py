import random
import time

w=makeWorld(400,400)
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
  print(s[0])

def forwardAndTurn(t):
  forward(t)
  turn(t)
  
def box(t):
  [forwardAndTurn(t) for i in range(4)]
  
def boxAndTurn(t):
  box(t)
  turn(t,20)

def design(t):
  [boxAndTurn(t) for i in range(19)]
  
