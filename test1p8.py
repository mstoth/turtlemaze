 	

def redline(p):
  for times in range(0,100):
    for row in range(4,50):
      addLine(p,0,row,49,row,red)
      repaint(p)
      addLine(p,0,row-1,49,row-1,blue)
      for i in range(9):
        repaint(p)
  return p