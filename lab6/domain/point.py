

class MyPoint:
  '''
  Descr: contains the initial, string representation, setter, getter
  and color-availability functions set for a point
  '''
  colors = ['red', 'green', 'blue', 'yellow', 'magenta']
  def __init__(self, x = 0, y = 0, color=""):
    '''
    Descr: initializes the coords of a point and its color in the class
    Precondition: x,y - numbers, color - string
    Input: (self),x,y,color
    '''
    self.__xCoord = x
    self.__yCoord = y
    self.__Color = color

  '''
  Descr: each getter function returns the x and y coords, and repectively, the color
  of a point predefined in the class
  Input: the class itself
  Output: x(1st) ,y(2nd), color(3rd) - accessed through the coresponding initial value defined in the 
  class for each function
  '''
  def getxCoord(self):
    return self.__xCoord
  def getyCoord(self):
    return self.__yCoord
  def getColor(self):
    return self.__Color

  '''
  Descr: each setter function changes the x and y coords, and repectively, the color
  of a point, predefined variables in the class, with new values
  Precondition: x,y - numbers, color - string
  Input: x(1st) ,y(2nd), color(3rd) - the new values
  Output: x(1st) ,y(2nd), color(3rd) - accessed through the coresponding initial value defined in the 
  class for each function and modificated with the new value
  '''
  def setCoordX(self , x=0):
    self.__xCoord=x
  def setCoordY(self, y=0):
    self.__yCoord=y
  def setColor(self, color=""):
    self.__Color=color

  def available_color(self):
    '''
    Descr: checks if the color of a point is in our predefined list of available colors in the class
    Input: the class itself
    Output: ok(True) - if the color is available, if not ok(False)
    '''
    ok = False
    for elem in self.colors:
      if elem == self.__Color:
        ok = True
        break
    return ok



  def __str__(self):
    '''
    Descr: string representation of a point
    Input: the class itself
    Output: the required string representation of a point in the lab assignment
    '''
    if self.available_color():
      return "Point ("+ str(self.__xCoord) + "," + str(self.__yCoord) +") of color " + self.__Color
    else:
      raise ValueError("the color is not an available option!")

'''
#Examples
point1=MyPoint(1,2,"red")
point2=MyPoint(1,2,"black")
point3=MyPoint(-1,0,"blue")
point4=MyPoint(0,0,"green")
point5=MyPoint(33,1101,"yellow")
point6=MyPoint(45,22,"magenta")
point7=MyPoint(9,29,"red")
point8=MyPoint(90,21,"blue")
point9=MyPoint(-101,-1,"green")
point10=MyPoint(8,2,"magenta")

print(str(point1))
#print(str(point2)) - we get an error, because the color is not available
print(str(point3))
print(str(point4))
print(str(point5))
print(str(point6))
print(str(point7))
print(str(point8))
print(str(point9))
print(str(point10))
'''














