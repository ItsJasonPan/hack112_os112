# Mode Demo
# Multi Mode Calculator
from tkinter import *


####################################
# init
####################################

class Box(object):
    # Model
    def __init__(self, x0, y0, x1, y1, num):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.num = num

    # View
    def draw(self, canvas, color="#155E63"):
        canvas.create_rectangle(self.x0,
                                self.y0,
                                self.x1,
                                self.y1,
                                fill=color, width=10, outline="#F9F8EB")
        canvas.create_text(self.x0 + (self.x1 - self.x0) / 2,
                           self.y0 + (self.y1 - self.y0) / 2, fill="#F9F8EB",
                           font="Arial 64 bold",
                           text=str(self.num))

    # Controller
    def inBox(self, otherX, otherY):
        cx = self.x0 + (self.x1 - self.x0) / 2
        cy = self.y0 + (self.y1 - self.y0) / 2
        diffX = cx - otherX
        diffY = cy - otherY
        diff = (diffX ** 2 + diffY ** 2) ** 0.5
        DIFF = (((self.x1 - self.x0) / 2) ** 2 + ((self.y1 - self.y0) / 2) ** 2) ** 0.5
        return diff <= DIFF

    def getNum(self):
        return str(self.num)


def generateNums(wid, hi):
    board = [["7", "8", "9", "/"],
             ["4", "5", "6", "*"],
             ["1", "2", "3", "-"],
             ["0", "C", "=", "+"]]
    box = []
    row = wid / 4
    col = hi / 5
    mar = 0
    for i in range(4):
        for j in range(1, 5):
            x0 = row * i
            y0 = col * j
            x1 = row * (i + 1)
            y1 = col * (j + 1)
            num = board[j - 1][i]
            newBox = Box(x0, y0, x1, y1, num)
            box += [newBox]
    return box


def init(data):
    # There is only one init, not one-per-mode
    data.mode = "start"
    data.nums = generateNums(data.width, data.height)
    data.res1 = ""
    data.isOp = False
    data.op = ""
    data.res2 = ""
    data.result = ""
    data.eq = ""
    data.answer = ""
    data.history = ""


####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "basic"):
        basicMousePressed(event, data)
    elif (data.mode == "long"):
        longMousePressed(event, data)
    elif (data.mode == "special"):
        specialMousePressed(event, data)
    elif (data.mode == "help"):
        helpMousePressed(event, data)
    elif (data.mode == "start"):
        splashScreenMousePressed(event, data)


def keyPressed(event, data):
    if (data.mode == "basic"):
        basicKeyPressed(event, data)
    elif (data.mode == "long"):
        longKeyPressed(event, data)
    elif (data.mode == "special"):
        specialKeyPressed(event, data)
    elif (data.mode == "help"):
        helpKeyPressed(event, data)
    elif (data.mode == "start"):
        splashScreenKeyPressed(event, data)


def timerFired(data):
    if (data.mode == "basic"):
        basicTimerFired(data)
    elif (data.mode == "long"):
        longTimerFired(data)
    elif (data.mode == "special"):
        specialTimerFired(data)
    elif (data.mode == "help"):
        helpTimerFired(data)
    elif (data.mode == "start"):
        splashScreenTimerFired(data)


def redrawAll(canvas, data):
    if (data.mode == "basic"):
        basicRedrawAll(canvas, data)
    elif (data.mode == "long"):
        longRedrawAll(canvas, data)
    elif (data.mode == "special"):
        specialRedrawAll(canvas, data)
    elif (data.mode == "help"):
        helpRedrawAll(canvas, data)
    elif (data.mode == "start"):
        splashScreenRedrawAll(canvas, data)


####################################
# basic mode
####################################

def basicMousePressed(event, data):
    for n in data.nums:
        if n.inBox(event.x, event.y) == True and \
                n.getNum() == "C":
            data.res1 = ""
            data.isOp = False
            data.op = ""
            data.res2 = ""
            data.result = ""
        elif n.inBox(event.x, event.y) == True and \
                n.getNum() not in ["+", "-", "*", "/", "="] and \
                data.isOp == False:
            data.res1 += n.getNum()
        elif n.inBox(event.x, event.y) == True and \
                n.getNum() in ["+", "-", "*", "/"]:
            data.isOp = True
            data.op = str(n.getNum())
        elif n.inBox(event.x, event.y) == True and \
                n.getNum() not in ["+", "-", "*", "/", "="] and \
                data.isOp == True:
            data.res2 += n.getNum()
        elif n.inBox(event.x, event.y) == True and \
                n.getNum() == "=":
            if data.op == "+":
                data.result = int(data.res1) + int(data.res2)
            elif data.op == "-":
                data.result = int(data.res1) - int(data.res2)
            elif data.op == "*":
                data.result = int(data.res1) * int(data.res2)
            elif data.op == "/":
                data.result = int(data.res1) / int(data.res2)
            data.result = str(data.result)
            data.history += "Basic: " + data.res1 + data.op + \
                            data.res2 + "=" + data.result + "\n"
            data.op = ""
            data.res1 = ""
            data.isOp = False
            data.res2 = ""


def basicKeyPressed(event, data):
    if event.keysym == "l":
        data.mode = "long"
    elif event.keysym == "s":
        data.mode = "special"
    elif event.keysym == "h":
        data.mode = "help"
    elif event.keysym == "w":
        data.mode = "start"

    elif event.keysym == "C":
        data.res1 = ""
        data.isOp = False
        data.op = ""
        data.res2 = ""
        data.result = ""
    elif event.keysym in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] and \
            data.isOp == False:
        data.res1 += event.keysym
    elif event.keysym in ["plus", "minus", "asterisk", "slash"]:
        data.isOp = True
        if event.keysym == "plus":
            data.op = "+"
        elif event.keysym == "minus":
            data.op = "-"
        elif event.keysym == "asterisk":
            data.op = "*"
        elif event.keysym == "slash":
            data.op = "/"
    elif event.keysym in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] and \
            data.isOp == True:
        data.res2 += event.keysym
    elif event.keysym == "equal":
        if data.op == "+":
            data.result = int(data.res1) + int(data.res2)
        elif data.op == "-":
            data.result = int(data.res1) - int(data.res2)
        elif data.op == "*":
            data.result = int(data.res1) * int(data.res2)
        elif data.op == "/":
            data.result = int(data.res1) / int(data.res2)
        data.result = str(data.result)
        data.history += "Basic: " + data.res1 + data.op + \
                        data.res2 + "=" + data.result + "\n"
        data.op = ""
        data.res1 = ""
        data.isOp = False
        data.res2 = ""
    elif event.keysym == "BackSpace":
        if data.res2 != "":
            data.res2 = data.res2[:-1]
        elif data.op != "":
            data.op = data.op[:-1]
            data.isOp = False
        elif data.res1 != "":
            data.res1 = data.res1[:-1]


def basicTimerFired(data):
    pass


def basicRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="#F9F8EB", width=0)
    for num in data.nums:
        num.draw(canvas)
    canvas.create_text(0, 0, anchor=NW,
                       text="basic mode", font="Arial 24 bold", fill="#155E63")
    canvas.create_text(data.width / 2, data.height / 30,
                       text=str(data.res1 + data.op) + \
                            str(data.res2 + data.result), anchor=N,
                       font="Arial 64 bold", fill="#155E63")


####################################
# special mode
####################################

def specialMousePressed(event, data):
    pass


def specialKeyPressed(event, data):
    if event.keysym == "b":
        data.mode = "basic"
    elif event.keysym == "l":
        data.mode = "long"
    elif event.keysym == "h":
        data.mode = "help"
    elif event.keysym == "w":
        data.mode = "start"


def specialTimerFired(data):
    pass


def specialRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width,
                            data.height, fill="#F9F8EB", width=0)
    canvas.create_text(0, 0, anchor=NW, text="calculation history",
                       font="Arial 24 bold", fill="#155E63")
    canvas.create_text(0, 30, anchor=NW, text=data.history,
                       font="Arial 12", fill="#155E63")


####################################
# long mode
####################################

def longMousePressed(event, data):
    for n in data.nums:
        if n.inBox(event.x, event.y) == True and \
                n.getNum() == "C":
            data.eq, data.answer = "", ""
        elif n.inBox(event.x, event.y) == True and \
                n.getNum() != "=":
            data.eq += n.getNum()
        elif n.inBox(event.x, event.y) == True and \
                n.getNum() == "=":
            data.answer = str(eval(data.eq))
            data.history += "Long: " + data.eq + "=" + data.answer + "\n"
            data.eq = ""


def longKeyPressed(event, data):
    if event.keysym == "b":
        data.mode = "baisc"
    elif event.keysym == "s":
        data.mode = "special"
    elif event.keysym == "h":
        data.mode = "help"
    elif event.keysym == "w":
        data.mode = "start"

    elif event.keysym == "C":
        data.eq, data.answer = "", ""
    elif event.keysym in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        data.eq += str(event.keysym)
    elif event.keysym in ["plus", "minus", "asterisk", "slash"]:
        if event.keysym == "plus":
            data.eq += "+"
        elif event.keysym == "minus":
            data.eq += "-"
        elif event.keysym == "asterisk":
            data.eq += "*"
        elif event.keysym == "slash":
            data.eq += "/"
    elif event.keysym == "equal":
        data.answer = str(eval(data.eq))
        data.history += "Long: " + data.eq + "=" + data.answer + "\n"
        data.eq = ""
    elif event.keysym == "BackSpace":
        data.eq = data.eq[:-1]


def longTimerFired(data):
    pass


def longRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill="#F9F8EB", width=0)
    for num in data.nums:
        num.draw(canvas)
    canvas.create_text(0, 0, anchor=NW,
                       text="long mode", font="Arial 24 bold", fill="#155E63")
    canvas.create_text(data.width / 2, data.height / 30, text=str(data.eq) +
                                                              str(data.answer), anchor=N, font="Arial 64 bold",
                       fill="#155E63")


####################################
# help mode
####################################

def helpMousePressed(event, data):
    pass


def helpKeyPressed(event, data):
    if event.keysym == "b":
        data.mode = "basic"
    elif event.keysym == "l":
        data.mode = "long"
    elif event.keysym == "s":
        data.mode = "special"
    elif event.keysym == "w":
        data.mode = "start"


def helpTimerFired(data):
    pass


def helpRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill="#F9F8EB", width=0)
    canvas.create_text(data.width / 2, data.height / 15,
                       text="help", font="Arial 36 bold", fill="#155E63")
    canvas.create_text(data.width / 10, data.height / 4,
                       text="Press 'b' \nfor basic, 2-digit calculation",
                       font="Arial 36 bold", anchor=W, fill="#155E63")
    canvas.create_text(data.width / 10, data.height / 2,
                       text="Press 'l' \nfor long, multi-digits calculation",
                       font="Arial 36 bold", anchor=W, fill="#155E63")
    canvas.create_text(data.width / 10, data.height * 0.75,
                       text="Press 's' \nfor calculation history",
                       font="Arial 36 bold", anchor=W, fill="#155E63")


####################################
# splashScreen mode
####################################

def splashScreenMousePressed(event, data):
    pass


def splashScreenKeyPressed(event, data):
    if event.keysym == "b":
        data.mode = "basic"
    elif event.keysym == "s":
        data.mode = "special"
    elif event.keysym == "h":
        data.mode = "help"
    elif event.keysym == "l":
        data.mode = "long"


def splashScreenTimerFired(data):
    pass


def splashScreenRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill="#F9F8EB", width=0)
    canvas.create_text(data.width / 2, data.height / 15,
                       text="welcome", font="Arial 36 bold", fill="#155E63")
    canvas.create_text(data.width / 10, data.height / 4,
                       text="This is a basic calculator \nPress 'b' to start",
                       font="Arial 36 bold", anchor=W, fill="#155E63")
    canvas.create_text(data.width / 10, data.height / 2,
                       text="Press 'h' for help \nPress 'w' to come back",
                       font="Arial 36 bold", anchor=W, fill="#155E63")


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Set up data and call init
    class Struct(object): pass

    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100  # milliseconds
    root = Tk()
    root.resizable(width=False, height=False)  # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
    mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
    keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


run(800, 800)
