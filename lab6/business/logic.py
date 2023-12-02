import sys
sys.path.append(r"D:\lab6")
import math
from domain.point import MyPoint


class PointRepository:
    #Descr: contains the container with all the points
    def __init__(self):
    # Descr: initializes the container in the class with an empty array
        self.__pl = []

    '''
    Descr: the getter function and setter function return, respectively change the repository container at 
    a specific moment
    Input: the class itself
    Output: the container itself(in getter), respectively the container changed(in setter)
    '''
    def getList(self):
        return self.__pl
    def setList(self,pl):
        self.__pl=pl

    def __str__(self):
    # the string representation of the container
        s=""
        for i in range (0,len(self.__pl)):
            s+= str(self.__pl[i])+"\n"
        return s

    #1. Add a point to the repository
    def addPoint(self,x,y,color):
        '''
        Descr: adds a point to the repository (if its color is available)
        Precondition: x,y - numbers, color - string
        Input: (self),x,y,color
        Output: our self.__pl(modified)
        '''
        s=MyPoint(x,y,color)
        if s.available_color():
            self.__pl.append(s)
        else:
            print("The color is not an available option!")


    # 3. Get a point at a given index
    def getPointAtIndex(self,index):
        '''
        Descr: gets a point at a certain index
        Precondition: index - number
        Input: (self),index
        Output: the point at the requested index (self.__pl[index])
        '''
        if index<0 or index>=len(self.__pl):
             return "Not an available index"
        return self.__pl[index]

    #4. Get all points of a given color 
    def getPointsOfColor(self,color):
        '''
        Descr: forms an array with all the points that have a certain color
        Precondition: color - string
        Input: (self),color
        Output: our new array
        '''
        points=[]
        for elem in self.__pl:
            if elem.getColor()==color:
                points.append(str(elem))
        return points

    #5. Get all the points that are given into a square (we know top-left corner and length)
    def getInsideSquare(self,x,y,length):
       '''
       Descr: forms an array with all the points that are inside square
       Precondition: x,y,length - numbers
       Input: (self),x,y,length
       Output: points array
       '''
       points = []
       for elem in self.__pl:
          if elem.getxCoord()>x and elem.getxCoord()<length+x and elem.getyCoord()>y-length and elem.getyCoord()<y:
             points.append(str(elem))
       return points

    #6. Distance between 2 points
    def getDistance(self,index1,index2):
        '''
        Descr: forms the distances between 2 given points (given their indexes)
        Precondition: index1,index2 - numbers
        Input: (self),index1, index2
        Output: minimum distance between point at index1 and point at index2 or a message if the indexes are unavailable
        '''
        if index1<0 or index1>=len(self.__pl) or index2<0 or index2>=len(self.__pl):
             return "Indexes not available"
        x1 = self.__pl[index1].getxCoord()
        y1 = self.__pl[index1].getyCoord()
        x2 = self.__pl[index2].getxCoord()
        y2 = self.__pl[index2].getyCoord()
        return math.sqrt((x2-x1)**2+(y2-y1)**2)

    #7. Update point at index
    def updateByIndex(self,index,x,y,color):
        '''
        Descr: updates a point at index
        Precondition: index1,x,y -numbers, color - string
        Input: (self),index,x,y,color
        Output: the repository updated if the index is in range
        '''
        if index<0 or index>=len(self.__pl):
             return "Not an available index"
        self.__pl[index].setCoordX(x)
        self.__pl[index].setCoordY(y)
        self.__pl[index].setColor(color)

    #8. Delete point at index
    def deleteByIndex(self,index):
        '''
        Descr: deletes a point at index
        Precondition: index- number
        Input: index
        Output: the repository updated if the index is in range
        '''
        if index<0 or index>=len(self.__pl):
             return "Not an available index"
        del self.__pl[index]
    #9. Delete inside square
    def deleteInsideSquare(self,x,y,length):
        '''
        Descr: deletes the points inside square
        Precondition: x,y,length - numbers
        Input: (self),x,y,length
        Output: our repository changed
        '''
        for i in range(len(self.__pl)-1,-1,-1):
            if self.__pl[i].getxCoord()>x and self.__pl[i].getxCoord()<length+x and self.__pl[i].getyCoord()>y-length and self.__pl[i].getyCoord()<y:
                del self.__pl[i]

   #10. Forms arrays for the library matplotlib
    def showpoints(self,x,y,colorsSet):
        '''
        Descr: Forms arrays for the library matplotlib
        Input: x,y,colorsSet
        Output: x,y,colorSet containing the x,y coords and the colors of all points in the repository
        '''
        for point in self.__pl:
            x.append(point.getxCoord())
            y.append(point.getyCoord())
            colorsSet.append(point.getColor())

    #auxiliary function
    def getPointIndexByCoord(self,x,y):
        '''
        Descr: returns the index of a point given its coords
        Precondition: x,y-numbers
        Input: (self),x,y
        Output: index or -1 if we do not have such a point in the repository
        '''
        for i in range(0, len(self.__pl)):
           if self.__pl[i].getyCoord() == y and self.__pl[i].getxCoord() == x:
                return i
        return -1

    # 11.(15 from lab). Update a point given its coordonates
    def updateByCoord(self,x,y, newcolor):
        '''
        Descr: updates a point given its coords
        Precondition: x,y-numbers, newcolor- string
        Input: (self),x,y,newcolor
        Output: our repository changed or message if the index is not available
        '''
        index = self.getPointIndexByCoord(x,y)
        if index==-1:
            return "No such coords in the repository"
        self.__pl[index].setColor(newcolor)

    #12.(18 from lab) Delete a point given coords
    def deleteByCoords(self,x,y):
        '''
        Descr: deletes a point given its coords
        Precondition: x,y-numbers
        Input: (self),x,y
        Output: our repository changed or message if the index is not available
        '''
        index = self.getPointIndexByCoord(x, y)
        if index==-1:
            return "No such coords in the repository"
        del self.__pl[index]

    #13.(11 from lab) Get points inside a circle

    def getPointsInCircle(self,x,y,radius):
        '''
        Descr: forms an array with all the points in the circle
        Precondition: all the parameters -numbers
        Input: (self),x,y,radius
        Output: points array
        '''
        points = []
        for elem in self.__pl:
            distance = math.sqrt((elem.getxCoord() - x) ** 2 + (elem.getyCoord() - y) ** 2)
            if distance<=radius:
                points.append(str(elem))
        return points



#10 data examples for PointRepository initial classes

#1st
pointRepoInitial=PointRepository()
pointRepoInitial.addPoint(1,2,"red")
#pointRepoInitial.addPoint(1,2,"black") this will not be added - the color is not available
pointRepoInitial.addPoint(-1,0,"blue")
pointRepoInitial.addPoint(0,0,"green")
pointRepoInitial.addPoint(33,1101,"yellow")
pointRepoInitial.addPoint(45,22,"magenta")
pointRepoInitial.addPoint(9,29,"red")
pointRepoInitial.addPoint(90,21,"blue")
pointRepoInitial.addPoint(-101,-1,"green")
pointRepoInitial.addPoint(8,2,"magenta")
pointRepoInitial.addPoint(86,2,"blue")

'''
#2nd
pointRepoInitial=PointRepository()
pointRepoInitial.addPoint(8,2,"magenta")
pointRepoInitial.addPoint(86,2,"blue")

#3rd
pointRepoInitial=PointRepository()
pointRepoInitial.addPoint(9,29,"red")
pointRepoInitial.addPoint(90,21,"blue")
pointRepoInitial.addPoint(-101,-1,"green")

#4th
pointRepoInitial=PointRepository()
pointRepoInitial.addPoint(-1,0,"blue")
pointRepoInitial.addPoint(0,0,"green")
pointRepoInitial.addPoint(33,1101,"yellow")
pointRepoInitial.addPoint(45,22,"magenta")
pointRepoInitial.addPoint(9,29,"red")

#5th
pointRepoInitial=PointRepository()
pointRepoInitial.addPoint(1,2,"red")

#6th
pointRepoInitial=PointRepository()
pointRepoInitial.addPoint(86,2,"blue")

#7th
pointRepoInitial=PointRepository()
pointRepoInitial.addPoint(33,1101,"yellow")
pointRepoInitial.addPoint(45,202,"magenta")

#8th
pointRepoInitial=PointRepository()
pointRepoInitial.addPoint(1,222,"red")

#9th
pointRepoInitial=PointRepository()
pointRepoInitial.addPoint(0,0,"green")
pointRepoInitial.addPoint(33,1101,"yellow")
pointRepoInitial.addPoint(45,22,"magenta")
pointRepoInitial.addPoint(9,2,"red")
pointRepoInitial.addPoint(90,21,"blue")
pointRepoInitial.addPoint(-101,-1,"green")
pointRepoInitial.addPoint(8,2,"magenta")

#10th
pointRepoInitial=PointRepository()
pointRepoInitial.addPoint(-1,0,"blue")
pointRepoInitial.addPoint(0,0,"green")
pointRepoInitial.addPoint(33,101,"yellow")
'''


