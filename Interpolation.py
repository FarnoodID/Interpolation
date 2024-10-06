import matplotlib.pyplot as plt
import numpy as np
import turtle as t

#x and y are arrays of the x coordinates and corrosponding y coordinates
#CodeBy FarnoodID
def get_equation(x,y,degr=5):
    degree = degr
    coefs, res, _, _, _ = np.polyfit(x,y,degree, full = True)
    return coefs

def getY(x,coef):
    rCoef = coef[::-1]
    return sum([rCoef[p]*x**p for p in range(len(rCoef))])

def showFunc(coef):
    for i in range(len(coef)):
        if  coef[i]<0.00000000000001:
            coef[i] = 0
    ffit = np.poly1d(coef)
    print (ffit)
    return ffit

def setTitle(coef):
    poly = ""
    for i in range(len(coef)):
        if coef[i]!= 0 and i != len(coef) -1:
            poly = poly+str("{:.2e}".format(coef[i]))+"x^("+str(len(coef) - i -1)+") + "
        elif coef[i]!= 0:
            poly = poly+str("{:.2e}".format(coef[i])) + " + "
    poly = poly[:-3]
    return poly

def getCoordinates():
    X = []
    Y = []
    while True:
        inp = input()
        if inp == "end":
            return X,Y
        x, y = inp.split()
        x = int(x)
        y = int(y)
        X.append(x)
        Y.append(y)

def tutorial():
    print("Please enter (x, y) coordinates of the points in format of \"x y\". for example:")
    print("*****Example*****")
    print("\t1 0")
    print("\t2 1")
    print("\t0 1")
    print("\t3 4")
    print("\t-1 4")
    print("\t-2 9")
    print("\t4 9")
    print("\tend")
    print("*****************")

def Tutorial():
    print()
    print("!!! ATTENTION !!!")
    print("The program does only work if the given points, are points of a function!")
    print("Meaning that (2,3) and (2,7) can't be accepted as points of a function!")
    print()
    print("HINT: The more points given to it, the more accurate the program can be.")
    print("Enter as much points as you can.")
    print()
    print()

def drawShape(x1, y1):
    global working
    working = True ##True while drawing.
    t.penup()
    t.goto(x1, y1)
    t.dot(5, "blue")    
    working = False ##false, drawing is over.
    #CodeBy FarnoodID

def clicked(x1, y1):
    global working
    global x
    global y
    x.append(x1)
    y.append(y1)
    print(x1, y1)
    if working == False : ##if turtle not drawing
        drawShape(x1, y1)

def stopped(x, y):
    t.bye()

degr = 100
fig = plt.gcf()
fig.canvas.manager.set_window_title('FarnoodID')
plt.xlabel('X')
plt.ylabel('Y')

Tutorial()

print("How do you enter your coordinates?")
print("1. Draw on whiteboard")
print("2. Type coordinates")
choice = int(input())
print()

if choice == 1 :
    print("Right-Click to finish")
    t.speed(0)
    t.ht()
    working = False
    x = []
    y = []
    t.onscreenclick(stopped, 3)
    t.onscreenclick(clicked)
    t.mainloop()

    print(x)
    print(y)

else:
    tutorial()
    x, y = getCoordinates()

'''
x = [0,1,-1,2,-2,3,-3]
y = [0,1,1,4,4,9,9]

x = [0,1,2,3,4,5,6,7,8]
y = [0,1,2,3,4,5,6,7,8]
'''
minX = min(x);maxX = max(x)
plt.axis([minX-20, maxX + 20,minX-20, maxX + 20])
coef = get_equation(x,y,degr)
x = np.arange(minX-20,maxX+20, 0.01)
y = getY(x,coef)

ffit = showFunc(coef)
poly = setTitle(coef)
plt.title(poly)

plt.plot(x, y)

plt.show()