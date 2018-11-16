def cal(a,res,op1,op2,num1,num2,s1,s2,last):
    import string
    if a[0]=="=":
        if last=="+":
            res+=int(s1)
        elif last=="-":
            res-=int(s1)
        elif last=="*":
            res*=int(s1)
        elif last=="/":
            res=res/int(s1)
        else:
            res=int(s2)+num1
        return res
    elif a[0].isdigit()==True and op1==None and op2==None:
        s1+=a[0]
        return cal(a[1:],res,op1,op2,num1,num2,s1,s2,last)
    elif a[0] in ["+","-","*","/"] and op1==None:
        num1=int(s1)
        s1="0"
        op1=a[0]
        return cal(a[1:],res,op1,op2,num1,num2,s1,s2,last)
    elif a[0].isdigit()==True and op1!=None and op2==None:
        s2+=a[0]
        res+=num1
        return cal(a[1:],res,op1,op2,num1,num2,s1,s2,last)
    elif a[0] in ["+","-","*","/"] and op1!=None and op2==None:
        num2=int(s2)
        if op1=="+":
            num1+=num2
        elif op1=="-":
            num1-=num2
        elif op1=="*":
            num1*=num2
        elif op1=="/":
            num1=num1/num2
        res+=num1
        num2=0
        s2="0"
        op1,op2=None,None
        last=a[0]
        return cal(a[1:],res,op1,op2,num1,num2,s1,s2,last)
        
def c(a):
    return cal(a,0,None,None,0,0,"0","0",None)

print(c("5+2="))
# Basic Calculator
# Basic Animation Framework

from tkinter import *

####################################
# customize these functions
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
    def draw(self, canvas, color="#7DA87B"):
        canvas.create_rectangle(self.x0,
                                self.y0,
                                self.x1,
                                self.y1,
                                fill=color,width=10,outline="white")
        canvas.create_text(self.x0+(self.x1-self.x0)/2, 
        self.y0+(self.y1-self.y0)/2,fill="white",                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                            font="Arial 64 bold",
                            text=str(self.num))
        
    
    # Controller
    def inBox(self, otherX, otherY):
        cx=self.x0+(self.x1-self.x0)/2
        cy=self.y0+(self.y1-self.y0)/2
        diffX = cx - otherX
        diffY = cy - otherY
        diff = (diffX**2 + diffY**2)**0.5
        DIFF = (((self.x1-self.x0)/2)**2+((self.y1-self.y0)/2)**2)**0.5
        return diff<=DIFF
        
    def getNum(self):
        return str(self.num)

def generateNums(wid, hi):
    board=[ ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","-"],
            ["0","00","=","+"] ]
    box=[]
    row=wid/4
    col=hi/5
    mar=0
    for i in range(4):
        for j in range(1,5):
            x0=row*i
            y0=col*j
            x1=row*(i+1)
            y1=col*(j+1)
            num=board[j-1][i]
            newBox=Box(x0,y0,x1,y1,num)
            box+=[newBox]
    return box
    
    
def init(data):
    data.nums=generateNums(data.width, data.height)
    data.res1=""
    data.isOp=False
    data.op=""
    data.res2=""
    data.result=""
    
    
def mousePressed(event, data):
    for n in data.nums:
        if n.inBox(event.x, event.y) == True and\
        n.getNum()!="=":
            data.res1+=n.getNum()
        elif n.inBox(event.x, event.y) == True and\
        n.getNum()=="=":
            if "*" in data.res1:
                data.res2=c(data.res1+"+1=")-1
            else:
                print("no")
                data.res2=c(data.res1+"=")
                print(data.res1+"=",c(data.res1+"="))
            data.res2=str(data.res2)
            data.res1=""
        

def keyPressed(event, data):
    if event.keysym=="c":
        init(data)

def redrawAll(canvas, data):
    for num in data.nums:
        num.draw(canvas)

    canvas.create_text(data.width/2,data.height/30,text=str(data.res1)+
    str(data.res2),anchor=N,font="Arial 64 bold",fill="black")

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

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
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
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800,800)
        