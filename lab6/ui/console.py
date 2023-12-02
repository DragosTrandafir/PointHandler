import sys
sys.path.append(r"D:\lab6")
from business.logic import PointRepository,pointRepoInitial

def printMenu():
    print("\n\n\nMenu:\n\t1. Add a point to the repository\n\t2. Get all points\n\t3. Get a point at a given index\n"
    +"\t4. Get all points of a given color\n"
    +"\t5. Get all points that are inside a given square (up-left corner and length given)\n"
    +"\t6. Get the minimum distance between two points\n"
    +"\t7. Update a point at a given index\n"
    +"\t8. Delete a point by index\n"
    +"\t9. Delete all points that are inside a given square\n"
    +"\t10. Plot all points in a chart (using library matplotlib)\n"
    +"\t11.Update a point given its coordonates\n"
    +"\t12.Delete a point given coords\n"
    +"\t13.Get points inside a circle\n"
    +"\t0. STOP")
def readOption():
    option=int(input("Option : "))
    return option
def printList(l):
    for elem in l:
        print(elem)


def start():
    startValue=False
    pointRepository = pointRepoInitial
    while startValue==False:
        printMenu()
        option=readOption()
        if option==1:
            x=int(input("X coord :"))
            y = int(input("Y coord :"))
            color = input("Color :")
            pointRepository.addPoint(x, y, color)
            print(pointRepository)
        elif option==2:
            print(pointRepository)
        elif option==3:
            index=int(input("Get point at given index : "))
            print(pointRepository.getPointAtIndex(index))
        elif option==4:
            color=input("Get all points with the color : ")
            print(pointRepository.getPointsOfColor(color))
        elif option==5:
            x = int(input("X coord of top-left:"))
            y = int(input("Y coord of top-left:"))
            length = int(input("Length :"))
            print(pointRepository.getInsideSquare(x,y,length))
        elif option==6:
            index1 = int(input("Get distance between the element at index:"))
            index2 = int(input("and the element at index:"))
            print(pointRepository.getDistance(index1,index2))
        elif option==7:
            index = int(input("Update point at index:"))
            x = int(input("X coord :"))
            y = int(input("Y coord :"))
            color = input("Color :")
            pointRepository.updateByIndex(index,x,y,color)
            print(pointRepository)
        elif option==8:
            index = int(input("Delete point at index:"))
            pointRepository.deleteByIndex(index)
            print(pointRepository)
        elif option==9:
            x = int(input("X coord of top-left:"))
            y = int(input("Y coord of top-left:"))
            length = int(input("Length :"))
            pointRepository.deleteInsideSquare(x,y,length)
            print(pointRepository)
        elif option==10:
            x = []
            y = []
            colorsSet = []
            pointRepository.showpoints(x, y, colorsSet)
            import matplotlib.pyplot as plt
            plt.scatter(x, y, c=colorsSet)
            plt.show()
        elif option==11:
            x = int(input("X coord:"))
            y = int(input("Y coord:"))
            color = input("Color :")
            pointRepository.updateByCoord(x,y,color)
            print(pointRepository)
        elif option==12:
            x = int(input("X coord:"))
            y = int(input("Y coord:"))
            pointRepository.deleteByCoords(x,y)
            print(pointRepository)
        elif option==13:
            x = int(input("X coord of center:"))
            y = int(input("Y coord of center:"))
            radius = int(input("Radius :"))
            print(pointRepository.getPointsInCircle(x,y,radius))
        elif option==0:
            startValue=True
        else:
            print("Option does not exist!")
