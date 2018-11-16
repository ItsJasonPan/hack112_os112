#Handles reading, writing, and creating files
from image_util import *


#a fake file object
class fakeFile(object):
    #needs as inputs a font type (arial, times, etc.) a font size in points,
    #and a margin in pixels
    #Note, works 100% for all sizes of arial. Not so much for any other font.
    def __init__(self,data,filePath,bounds,font="ariel",fontSize=12,margin = 20):
        self.fontSize = fontSize
        self.font = font
        self.filePath = filePath
        try:
            fin = open(filePath, "r")
        except:
            f = open(filePath, "w")
            f.close()
            fin = open(filePath, "r")
        text = ""
        for line in fin:
            text += line
        self.text = text
        self.margin = margin
        #left,top,right,bot
        self.bounds = bounds
        self.curHeight = 10

        left,top,right,bot = self.bounds
        winWidth = abs(left - right)
        wrapedText = self.wrapText(self.fontSize,winWidth,self.margin)
        if bot == None:
            bot = top + self.margin + self.getHeightInPixels(wrapedText)
        
        data.wH = bot

    
    #draws the fake file object, in the location provided.
    #If bot is not provided, it will adjust the height as necicary dependent
    #on the length of the text file
    def draw(self,data,canvas):
        left,top,right,bot = self.bounds
        winWidth = abs(left - right)
        wrapedText = self.wrapText(self.fontSize,winWidth,self.margin)
        if bot == None:
            bot = top + self.margin + self.getHeightInPixels(wrapedText)
        
        fullFontString = self.font + " " + str(self.fontSize)
        canvas.create_rectangle(left,top,right,bot,fill = "white")
        data.wH = bot+self.margin - 240
        #canvas.create_rectangle(left,top,left+self.margin,top+self.margin,fill = "red")
        canvas.create_text(left+self.margin, top+self.margin, text = wrapedText,
                                        anchor = "nw", font = fullFontString)

    def getHeightInPixels(self,wrapedText):
        numLines = len(wrapedText.split("\n"))
        pointToPixelHeight = .75
        self.curHeight = (self.fontSize * numLines) / pointToPixelHeight
        return self.curHeight

    #returns a text string that can fit inside the boundries specified
    def wrapText(self,textSizeInPoints,windowWidthInPixels,marginInPixels):
        pointToPixelRatio = .48
        windowWidthInPoints = (windowWidthInPixels - 2 * marginInPixels) / pointToPixelRatio
        numCharsPerLine = (windowWidthInPoints) // textSizeInPoints
        wrapedText = insureNumCharsPerLine(self.text, numCharsPerLine)
        return wrapedText

    
    def isInBounds(self,clickX,clickY):
        left,top,right,bot = self.bounds
        if bot == None:
            bot = top + self.margin + self.getHeightInPixels(wrapedText)

        if left <= clickX <= right and top <= clickY <= bot:
            return True
        else:
            return False
    
    def isInBoundsOfCloseButton(self,clickX,clickY):
        return False
    
    #save changes
    def writeChangesToFile(self):
        fin = open(self.filePath, "w")
        fin.write(self.text)


def insureNumCharsPerLine(inputText, numCharsPerLine):
    outText = ""
    lineList = inputText.split("\n")
    for i in range(len(lineList)):
        lineList[i] = lineList[i].split(" ")
    for i in range(len(lineList)):
        curString = ""
        for j in range(len(lineList[i])):
            if 1 + len(lineList[i][j]) + len(curString) < numCharsPerLine or\
                    (curString == "" and len(lineList[i][j]) + len(curString) < numCharsPerLine):
                if curString == "":
                    curString += lineList[i][j]
                else:
                    curString += " " + lineList[i][j]
            else:
                curString += "\n" 
                outText += curString
                curString = lineList[i][j]
        curString += "\n"
        outText += curString
    return outText

#The icon on the desktop which represents a fake file     
class fakeFileIcon(object):
    def __init__(self,associatedFilePath,leftEdge,topEdge):
        self.associatedFilePath = associatedFilePath
        self.leftEdge = leftEdge
        self.topEdge = topEdge
        self.image = PhotoImage(file="RealFileIcon.gif")
        self.imageXLen = 120
        self.imageYLen = 150
        self.name = associatedFilePath[6:]
    
    def draw(self,canvas):
        canvas.create_image(self.leftEdge,self.topEdge,image = self.image)
        canvas.create_text(self.leftEdge + self.imageXLen, self.topEdge, anchor = "n", font = "arial 12", text= self.name)
    
    #needs to be changed if changing file icon
    def isInBounds(self,clickX,clickY):
        if self.leftEdge - self.imageXLen*.5 <= clickX <= self.leftEdge + self.imageXLen*.5 and\
                        self.topEdge - self.imageYLen*.5 <= clickY <= self.topEdge + self.imageYLen*.5:
            return True
        else:
            return False
    




    

    

    

#actually, is uncecary now. can just make a fakeFile with a path which doesn't yet exist
def makeNewFile(fileName,userDirPath):
    fin.write(userDirPath + "/" + fileName + ".txt","w")
    fin.close()


#all the test crap
if __name__ == "__main__":
    def testInsureNumCharsPerLine():
        fName = insureNumCharsPerLine
        input1 = "hello hello hello hello"
        expected1 = "hello\nhello\nhello\nhello\n"
        expected1_2 = "hello hello\n hello hello\n"
        input2 = "hey hey hey\nhey hey hey"
        expected2 = "hey\nhey\nhey\nhey\nhey\nhey\n"

        myAssert(fName,[input1,6],expected1)
        myAssert(fName,[input1,100],expected1_2)
        myAssert(fName,[input1,11],expected1_2)
        myAssert(fName,[input2,4],expected2)

    def myAssert(theFunction, theInputs, expectedOutput):
        assert(isinstance(theInputs,list))
        if len(theInputs) == 1:
            actualOutput = theFunction(theInputs[0])
        elif len(theInputs) == 2:
            actualOutput = theFunction(theInputs[0], theInputs[1])

        if actualOutput != expectedOutput:
            print(str(theFunction), end = "")
            print(" failed a Test Case\nThe Inputs were: ", end = "")
            for element in theInputs:
                print(element, "", end = "")
            print(". Expected output was: ", end = "")
            print(expectedOutput, end = "")
            print(". Actual function output was: ", end = "")
            print(actualOutput)
    #testInsureNumCharsPerLine()


    #print(myFile.text)

    from tkinter import *

    width = 900
    height = 900


    def init(data):
        data.filePath = ""
        fileList = []

    def mousePressed(event, data):
        # use event.x and event.y
        pass

    def keyPressed(event, data):
        # use event.char and event.keysym
        pass

    def timerFired(data):
        pass

    def redrawAll(canvas, data):
        # draw in canvas
        pass

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
        data.timerDelay = 100 # milliseconds
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
        timerFiredWrapper(canvas, data)
        # and launch the app
        root.mainloop()  # blocks until window is closed
        print("bye!")
