import sys
sys.path.append(r"D:\lab6")
from domain.point import MyPoint
from business.logic import PointRepository


#Test point iteration
def test_create():
  point = MyPoint(1, 2, "red")
  assert point.getxCoord() == 1
  point.setCoordX(4)
  assert point.getxCoord() == 4

  assert point.getyCoord() == 2
  point.setCoordY(0)
  assert point.getyCoord() == 0

  assert point.getColor() == "red"
  point.setColor("magenta")
  assert point.getColor() == "magenta"

  point = MyPoint(-2, 0, "blue")
  assert point.getxCoord() == -2
  point.setCoordX(9)
  assert point.getxCoord() == 9

  assert point.getyCoord() == 0
  point.setCoordY(99)
  assert point.getyCoord() == 99

  assert point.getColor() == "blue"
  point.setColor("black") #unavailable colors can be set for a point, but the error will appear in the str representation
  assert point.getColor() == "black"

  point = MyPoint(100, -5, "magenta")
  assert point.getxCoord() == 100
  point.setCoordX(100)
  assert point.getxCoord() == 100

  assert point.getyCoord() == -5
  point.setCoordY(999)
  assert point.getyCoord() == 999

  assert point.getColor() == "magenta"
  point.setColor("yellow")
  assert point.getColor() == "yellow"
test_create()


def test_available_color():
  point = MyPoint(1, 2, "red")
  assert point.available_color()

  point = MyPoint(100, -5, "black")
  assert point.available_color() == False

  point = MyPoint(100, -5, "re")
  assert point.available_color() == False
test_available_color()


def test_str():
  point = MyPoint(1, 2, "red")
  assert str(point)=="Point (1,2) of color red"

  point = MyPoint(-2, 0, "blue")
  assert str(point) == "Point (-2,0) of color blue"

  point = MyPoint(100, -5, "black")
  #assert str(point) == "Point (100,-5) of color black" - this will raise a ValueError, as expected, because the color is unavailable
test_str()




#Test point repository iteration
def test_createRepoandFunctions():
  #string repr is obviously checked more then 3 times
  # we first check function 1

  pointRepo = PointRepository()
  point = MyPoint(1, 4, "red")
  pointRepo.addPoint(point.getxCoord(),point.getyCoord(),point.getColor())
  assert str(pointRepo) == "Point (1,4) of color red"+"\n"

  point = MyPoint(-7, 0, "magenta")
  pointRepo.addPoint(point.getxCoord(), point.getyCoord(), point.getColor())
  assert str(pointRepo) == "Point (1,4) of color red"+"\n"+"Point (-7,0) of color magenta" + "\n"

  point = MyPoint(-7, 0, "black")
  pointRepo.addPoint(point.getxCoord(), point.getyCoord(), point.getColor())
  assert str(pointRepo) == "Point (1,4) of color red" + "\n" + "Point (-7,0) of color magenta" + "\n"
  #the repo is not updated - black is not an available color!

  point = MyPoint(0, 0, "red")
  pointRepo.addPoint(point.getxCoord(), point.getyCoord(), point.getColor())
  assert str(pointRepo) == "Point (1,4) of color red" + "\n" + "Point (-7,0) of color magenta" + "\n"+ "Point (0,0) of color red" + "\n"

  #we can now check the other functions, because we have a nonempty repository already created


  #2 is exactly the string repr of the repository, which we have already checked

  #3
  assert str(pointRepo.getPointAtIndex(0)) == "Point (1,4) of color red"
  assert str(pointRepo.getPointAtIndex(2)) == "Point (0,0) of color red"
  assert str(pointRepo.getPointAtIndex(3)) == "Not an available index"
  assert str(pointRepo.getPointAtIndex(-1)) == "Not an available index"

  #4
  assert pointRepo.getPointsOfColor("red") ==["Point (1,4) of color red","Point (0,0) of color red"]
  assert pointRepo.getPointsOfColor("magent") ==[]
  assert pointRepo.getPointsOfColor("magenta") == ["Point (-7,0) of color magenta"]

  #5
  assert pointRepo.getInsideSquare(-1,7,40)==['Point (1,4) of color red', 'Point (0,0) of color red']
  assert pointRepo.getInsideSquare(0,1,20)==[]
  assert pointRepo.getInsideSquare(0,0,0)==[]

  #6
  assert pointRepo.getDistance(0,1)==8.94427190999916
  assert pointRepo.getDistance(1, 2) == 7.0
  assert pointRepo.getDistance(3, 0) == "Indexes not available"

  #7
  pointRepo.updateByIndex(0,22,23,"red")
  assert str(pointRepo)=="Point (22,23) of color red" + "\n" + "Point (-7,0) of color magenta" + "\n"+ "Point (0,0) of color red" + "\n"
  #If the color is unaivalable, we get an error
  #pointRepo.updateByIndex(0, 22, 23, "re")
  #assert str(pointRepo) == "Point (22,23) of color re" + "\n" + "Point (-7,0) of color magenta" + "\n" + "Point (0,0) of color red" + "\n"
  assert pointRepo.updateByIndex(11, 22, 23, "red")=="Not an available index"

  #8
  #I put this in commentaries because I want to keep the list for the other tests
  '''
  pointRepo.deleteByIndex(0)
  assert str(pointRepo) =="Point (-7,0) of color magenta" + "\n"+ "Point (0,0) of color red" + "\n"
  assert pointRepo.deleteByIndex(4)=="Not an available index"
  pointRepo.deleteByIndex(1)
  assert str(pointRepo) == "Point (-7,0) of color magenta" + "\n"
  '''

  #9
  # I put this in commentaries because I want to keep the list for the other tests
  '''
  pointRepo.deleteInsideSquare(-1,2,4)
  assert str(pointRepo)=="Point (22,23) of color red"+"\n"+"Point (-7,0) of color magenta"+"\n"

  pointRepo.deleteInsideSquare(0, 44, 100)
  assert str(pointRepo)=="Point (-7,0) of color magenta"+"\n"

  pointRepo.deleteInsideSquare(-8, 44, 100)
  assert str(pointRepo) == ""
  '''

  #11
  assert str(pointRepo.updateByCoord(1, 4, "yellow"))=="No such coords in the repository"
  pointRepo.updateByCoord(22, 23, "yellow")
  assert str(pointRepo)=="Point (22,23) of color yellow"+"\n"+"Point (-7,0) of color magenta"+"\n"+"Point (0,0) of color red"+"\n"
  #The color is not available
  #pointRepo.updateByCoord(0, 0, "blu")
  #assert str(pointRepo) == "Point (22,23) of color yellow" + "\n" + "Point (-7,0) of color magenta" + "\n" + "Point (0,0) of color blu" + "\n"

  #12
  # I put this in commentaries because I want to keep the list for the other tests
  '''
  assert str(pointRepo.deleteByCoords(1, 4)) == "No such coords in the repository"
  pointRepo.deleteByCoords(22, 23)
  assert str(pointRepo) == "Point (-7,0) of color magenta"+"\n"+"Point (0,0) of color red"+"\n"
  pointRepo.deleteByCoords(-7, 0)
  assert str(pointRepo) == "Point (0,0) of color red"+"\n"
  '''

  #13
  assert pointRepo.getPointsInCircle(0, 0, 7)==['Point (-7,0) of color magenta', 'Point (0,0) of color red']
  assert pointRepo.getPointsInCircle(0, 0, 400) == ['Point (22,23) of color yellow','Point (-7,0) of color magenta', 'Point (0,0) of color red']
  assert pointRepo.getPointsInCircle(-10, -10, 1) == []

test_createRepoandFunctions()

