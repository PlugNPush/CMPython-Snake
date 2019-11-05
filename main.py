import random

class Element:
    def __init__(self, t, ex, ey):
        self.table = t
        self.elementx = ex
        self.elementy = ey

def initField():
    t = []
    for i in range(0, 10):
        t.append([])
        for s in range(0, 20):
            t[i].append('.')
    return t

def printField(t):
    for i in range(len(t)):
        for s in range(len(t[i])):
            print(t[i][s], end='')
        print("\n", end='')

def placeElement(x,y,t, e):
    t[x][y] = e
    return Element(t,x,y)

def deplaceX(x,y,a,b,t):
    if x < a:
        if y < b:
            y += 1
        elif y > b:
            y -= 1
        else:
            x += 1
    elif x > a:
        if y < b:
            y += 1
        elif y > b:
            y -= 1
        else:
            x -= 1
    else:
        if y < b:
            y += 1
        elif y > b:
            y -= 1
        else:
            print("gagné!")
    t[x][y] = 'X'
    if x == a and y == b:
        print("Le serpent a mangé la pommme")
    return t
    
t = initField()
printField(t)
print("\n----------------\n\n")
action = placeElement(5,5,t, 'O')
t = action.table
printField(t)
print(action.elementx, action.elementy)
actionx = placeElement(8,8,t, 'X')
print("\n----------------\n\n")
t = actionx.table
printField(t)
print("\n----------------\n\n")
t = deplaceX(actionx.elementx, actionx.elementy, action.elementx, action.elementy, t)
t = deplaceX(actionx.elementx, actionx.elementy-1, action.elementx, action.elementy, t)
t = deplaceX(actionx.elementx, actionx.elementy-2, action.elementx, action.elementy, t)
t = deplaceX(actionx.elementx-1, actionx.elementy-2, action.elementx, action.elementy, t)
t = deplaceX(actionx.elementx-2, actionx.elementy-2, action.elementx, action.elementy, t)
t = deplaceX(actionx.elementx-3, actionx.elementy-2, action.elementx, action.elementy, t)
printField(t)

