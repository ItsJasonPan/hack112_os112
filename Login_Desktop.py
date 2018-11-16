# Updated Animation Starter Code

from tkinter import *
import os
import shutil
import managesFiles


####################################
# login_chooseUser
####################################

def drawLogin_chooseUser(canvas, data):
    userIndex = 0
    data.image = []
    data.users = []
    for users in os.listdir("users"):
        if os.path.isdir("users/"+users) and users != "Logos_Images":
            #print(users)
            data.image.append(PhotoImage(file=str("users/"+users + "/logo.gif")))
            pos = data.logoPosition[userIndex]
            posX, posY = pos[0], pos[1]
            userIndex += 1
            data.users.append(str(users))
            canvas.create_image(posX, posY,
                                anchor=NW,
                                image=data.image[-1])
            canvas.create_text(posX + data.logoSize // 2, posY + data.logoSize + 30,
                               text=str(users),
                               font="Helvetica 20 bold")
    canvas.create_rectangle(data.width // 2 - 2 * data.width // 30,
                            data.height - 8 * data.height // 30,
                            data.width // 2 + 2 * data.width // 30,
                            data.height - 7 * data.height // 30,
                            fill=None)
    canvas.create_text(data.width // 2,
                       data.height - 15 * data.height // 60,
                       text="Create New Account",
                       font="Helvetica 15 bold")
    canvas.create_text(data.width // 2,
                       data.height // 6,
                       text="OS 112",
                       font="Chalkduster 150 bold")


def initLogin_chooseUser(data):
    data.logoSize = 150
    data.logoHeight = data.height // 2
    data.logoPosition = []
    data.accountNumber = 0
    for files in os.listdir("users"):
        if os.path.isdir("users/"+files) and files != "Logos_Images":
            data.accountNumber += 1
    data.logoHeightPos = data.height // 2 - data.logoSize // 2  # changable
    data.logoWidth = data.logoSize  # changable
    data.logoDistance = data.logoSize  # changable
    if data.accountNumber % 2 == 0:
        for accounts in range(1, data.accountNumber + 1):
            # logo x is x-coordinate of top-left corner
            if accounts % 2 == 1:
                logoX = data.width // 2 + data.logoDistance // 2 + \
                        (accounts // 2) * (data.logoWidth + data.logoDistance)
            else:
                logoX = data.width // 2 + data.logoDistance // 2 - \
                        (accounts // 2) * (data.logoWidth + data.logoDistance)
            data.logoPosition.append([logoX, data.logoHeightPos])
    else:
        for accounts in range(1, data.accountNumber + 1):
            if accounts % 2 == 0:
                logoX = data.width // 2 - data.logoDistance // 2 + \
                        (accounts // 2) * (data.logoWidth + data.logoDistance)
            else:
                logoX = data.width // 2 - data.logoWidth // 2 - \
                        (accounts // 2) * (data.logoWidth + data.logoDistance)
            data.logoPosition.append([logoX, data.logoHeightPos])


def login_chooseUser_MP(event, data):
    if data.width // 2 - 2 * data.width // 30 < event.x < data.width // 2 + 2 * data.width // 30 and \
            data.height - 8 * data.height // 30 < event.y < data.height - 7 * data.height // 30:
        data.mode = "create_account"
    userIndex = -1
    for pos in data.logoPosition:
        userIndex += 1
        posX, posY = pos[0], pos[1]
        if posX < event.x < posX + data.logoSize and posY < event.y < posY + data.logoSize:
            data.mode = "login"
            data.currentUser = [data.users[userIndex], data.image[userIndex]]
            data.fileIcons = []
            pathString = "users/" + data.currentUser[0]
            filesList = getFiles(pathString)
            for i in range(0,len(filesList)):
                curpath = pathString + "/" + filesList[i]
                curIcon = managesFiles.fakeFileIcon(curpath,200,200*(i+1))
                data.fileIcons.append(curIcon)
            break


####################################
# create_account
####################################
def initCreat_account(data):
    data.createAccountName = ""
    data.createAccountPassword = ""
    data.createAccountImage = None
    data.CAImageX, data.CAImageY = None, None
    data.createAccountBox = [data.width // 6, data.height // 20]
    data.enteringName = False
    data.enteringPassword = False
    # data.createAccount
    data.createAccountlogos = []
    data.createAccountlogoPos = []
    logoDistance = data.width // 20
    logoStartingHeight = 2 * data.height // 5
    logoStartingWidth = data.width // 4
    for i in range(1, 9):
        posY = logoStartingHeight + (i - 1) // 4 * (logoDistance + data.logoSize)
        posX = logoStartingWidth + ((i - 1) % 4) * (logoDistance + data.logoSize)
        data.createAccountlogos.append([PhotoImage(file="Logos_Images/" + str(i) + ".gif"), posX, posY])


def drawCreate_account(canvas, data):
    # account name
    canvas.create_text(data.width // 2,
                       data.height // 8,
                       text="Please enter your account name",
                       font="Helvetica 18 bold")
    canvas.create_rectangle(data.width // 2 - data.createAccountBox[0] // 2,
                            1 * data.height // 6 - data.createAccountBox[1] // 2,
                            data.width // 2 + data.createAccountBox[0] // 2,
                            1 * data.height // 6 + data.createAccountBox[1] // 2,
                            fill=None,
                            outline="red" if data.enteringName else "black")
    canvas.create_text(data.width // 2,
                       data.height // 6,
                       text=data.createAccountName,
                       font="Helvetica 26 bold")
    # password
    canvas.create_text(data.width // 2,
                       data.height // 8 + data.height // 9,
                       text="Please enter your password",
                       font="Helvetica 18 bold")
    canvas.create_rectangle(data.width // 2 - data.createAccountBox[0] // 2,
                            2 * data.height // 7 - data.createAccountBox[1] // 2,
                            data.width // 2 + data.createAccountBox[0] // 2,
                            2 * data.height // 7 + data.createAccountBox[1] // 2,
                            fill=None,
                            outline="red" if data.enteringPassword else "black")
    canvas.create_text(data.width // 2,
                       2 * data.height // 7,
                       text=data.createAccountPassword,
                       font="Helvetica 26 bold")
    # logos
    canvas.create_text(data.width // 2,
                       data.height // 8 + 3 * data.height // 12,
                       text="Please choose your account logo",
                       font="Helvetica 18 bold")
    if data.createAccountImage != None:
        canvas.create_rectangle(data.CAImageX, data.CAImageY,
                                data.CAImageX + data.logoSize,
                                data.CAImageY + data.logoSize,
                                fill=None,
                                outline="red",
                                width=5)
    for logos in data.createAccountlogos:
        myimage, posX, posY = logos[0], logos[1], logos[2]
        canvas.create_image(posX, posY, anchor=NW, image=myimage)
    # cancel
    canvas.create_rectangle(2 * data.width // 20,
                            data.height - 3 * data.width // 30,
                            3 * data.width // 20,
                            data.height - 2 * data.width // 30,
                            fill=None)
    canvas.create_text(5 * data.width // 40,
                       data.height - 5 * data.width // 60,
                       text="Cancel",
                       font="Helvetica 15 bold")
    # Create
    canvas.create_rectangle(data.width // 2 - data.width // 20,
                            7 * data.height // 8 - data.createAccountBox[1] // 2,
                            data.width // 2 + data.width // 20,
                            7 * data.height // 8 + data.createAccountBox[1] // 2)
    canvas.create_text(data.width // 2, 7 * data.height // 8, text="Create", font="Helvetica 20 bold")


def createAccount_MP(event, data):
    if 2 * data.width // 20 < event.x < 3 * data.width // 20 \
            and data.height - 3 * data.width // 30 < event.y < data.height - 2 * data.width // 30:
        data.mode = "login_chooseUser"
        initCreat_account(data)
    elif data.width // 2 - data.createAccountBox[0] // 2 < event.x < \
            data.width // 2 + data.createAccountBox[0] // 2 and \
            1 * data.height // 6 - data.createAccountBox[1] // 2 < event.y < \
            1 * data.height // 6 + data.createAccountBox[1] // 2:
        data.enteringName = True
        data.enteringPassword = False
    elif data.width // 2 - data.createAccountBox[0] // 2 < event.x < \
            data.width // 2 + data.createAccountBox[0] // 2 and \
            2 * data.height // 7 - data.createAccountBox[1] // 2 < event.y < \
            2 * data.height // 7 + data.createAccountBox[1] // 2:
        data.enteringPassword = True
        data.enteringName = False
    elif (data.width // 2 - data.width // 20) < event.x < (data.width // 2 + data.width // 20) and \
            (7 * data.height // 8 - data.createAccountBox[1] // 2) < event.y \
            < (7 * data.height // 8 + data.createAccountBox[1] // 2):
        createAccount_Create(data)
    else:
        for logoIndex in range(len(data.createAccountlogos)):
            logos = data.createAccountlogos[logoIndex]
            myimage, posX, posY = logos[0], logos[1], logos[2]
            if posX < event.x < posX + data.logoSize and posY < event.y < posY + data.logoSize:
                data.createAccountImage = logoIndex + 1
                data.CAImageX, data.CAImageY = posX, posY
                break


def createAccount_KP(event, data):
    import string
    if data.enteringName:
        if event.char in string.ascii_letters or event.char in string.digits or event.char == "_":
            data.createAccountName += event.char
        elif event.keysym == "BackSpace":
            if len(data.createAccountName) > 0:
                data.createAccountName = data.createAccountName[:-1]
    elif data.enteringPassword:
        if event.char in string.ascii_letters or event.char in string.digits or event.char == "_":
            data.createAccountPassword += event.char
        elif event.keysym == "BackSpace":
            if len(data.createAccountPassword) > 0:
                data.createAccountPassword = data.createAccountPassword[:-1]


def createAccount_Create(data):
    name = data.createAccountName
    password = data.createAccountPassword
    logo = data.createAccountImage
    os.mkdir("users/"+name)
    f = open("users/"+name + "/Info", "w+")
    f.write("account:" + name + "\n" + "password:" + password + "\n")
    src = "Logos_Images/" + str(data.createAccountImage) + ".gif"
    shutil.copy(src, "users/"+name)
    os.rename("users/"+name + "/" + str(data.createAccountImage) + ".gif", "users/"+name + "/logo.gif")
    data.mode = "login_chooseUser"
    initLogin_chooseUser(data)
    initCreat_account(data)


####################################
# login
####################################
def drawLogin(canvas, data):
    canvas.create_image(data.width // 2, 2 * data.height // 5,
                        image=data.currentUser[1])
    canvas.create_text(data.width // 2, 11 * data.height // 20,
                       text="Please enter your password...",
                       font="Helvetica 20 bold")
    canvas.create_rectangle(data.width // 2 - data.passwordBox[0] // 2,
                            3 * data.height // 5 - data.passwordBox[1] // 2,
                            data.width // 2 + data.passwordBox[0] // 2,
                            3 * data.height // 5 + data.passwordBox[1] // 2,
                            fill=None
                            )
    canvas.create_text(data.width // 2,
                       3 * data.height // 5,
                       text="*" * len(data.passwordInput),
                       font="Helvetica 26 bold")
    if data.wrongPassword and data.loginTimer > 0:
        canvas.create_text(data.width // 2,
                           13 * data.height // 20,
                           text="*Wrong Password*",
                           font="Helvetica 20 bold")
    canvas.create_rectangle(2 * data.width // 20,
                            data.height - 3 * data.width // 30,
                            3 * data.width // 20,
                            data.height - 2 * data.width // 30,
                            fill=None)
    canvas.create_text(5 * data.width // 40,
                       data.height - 5 * data.width // 60,
                       text="Go Back",
                       font="Helvetica 15 bold")


def initLogin(data):
    data.passwordBox = [3 * data.logoSize / 2, 40]
    data.passwordInput = ""
    data.wrongPassword = False


def login_KP(event, data):
    if event.keysym == "Return":
        checkPassword(data)
    elif event.keysym == "BackSpace":
        if len(data.passwordInput) > 0:
            data.passwordInput = data.passwordInput[:-1]
    elif event.char != "":
        data.passwordInput += event.char


def login_MP(event, data):
    if 2 * data.width // 20 < event.x < 3 * data.width // 20 \
            and data.height - 3 * data.width // 30 < event.y < data.height - 2 * data.width // 30:
        data.mode = "login_chooseUser"
        initLogin(data)


def login_TF(data):
    if data.wrongPassword and data.loginTimer > 0:
        data.loginTimer -= data.timerDelay


def checkPassword(data):
    with open(str("users/"+data.currentUser[0] + "/info"), "rt") as f:
        userInfo = f.read()
    for lines in userInfo.splitlines():
        if lines.startswith("password"):
            password = lines.split(":")[1]
            break
    if data.passwordInput == password:
        data.mode = "home_screen"
    else:
        data.passwordInput = ""
        data.wrongPassword = True
        data.loginTimer = 1500


####################################
# home_screen
####################################

def initHomeScreen(data):
    data.topBarHeight = 30
    data.topBarOffset = 10

def drawTopBar(canvas, data):
    import datetime
    canvas.create_rectangle(0, 0, data.width, data.topBarHeight, fill="grey")
    canvas.create_text(data.width - data.topBarOffset,
                       data.topBarOffset,
                       anchor=NE,
                       text=str(datetime.datetime.now())[:-7],
                       font="Helvetica 15 bold")
    canvas.create_text(data.topBarOffset, data.topBarOffset,
                       anchor=NW, text="About OS 112",font="Helvetica 15 bold")

def drawBottombar(canvas, data):
    pass

def drawFileIcons(canvas,data):
    for icon in data.fileIcons:
        icon.draw(canvas)


def drawDeskTop(canvas, data):
    canvas.create_rectangle(4*data.width // 10, data.height//6,
                            6*data.width // 10, 2*data.height //6,
                            fill="red")
    canvas.create_text(5*data.width//10, 3*data.height//12, text="Tetris",
                       font="Chalkduster 50 bold")
    #sokoban
    canvas.create_rectangle(7*data.width // 10, data.height//6,
                            9*data.width // 10, 2*data.height //6,
                            fill="yellow")
    canvas.create_text(8*data.width//10,
                       data.height//4,
                       text="Sokoban",
                       font="Chalkduster 50 bold")
    canvas.create_rectangle(7 * data.width // 10, 12 * data.height // 24,
                            9 * data.width // 10, 16 * data.height //24,
                            fill="green")
    canvas.create_text(8 * data.width // 10,
                       14*data.height // 24,
                       text="Calculator",
                       font="Chalkduster 50 bold")

    canvas.create_rectangle(2 * data.width // 20, 20 * data.height // 24,
                            3 * data.width // 20, 22 * data.height // 24,
                            fill="white")
    canvas.create_text(5 * data.width // 40,
                       21 * data.height // 24,
                       text="Log out",
                       font="Chalkduster 16 bold")
    canvas.create_rectangle(4*data.width // 10, 12 * data.height // 24,
                            6 * data.width // 10, 16 * data.height //24,
                            fill="white")
    canvas.create_text(5 * data.width // 10,
                       14 * data.height // 24,
                       text="Create File",
                       font="Chalkduster 50 bold")

def drawHomeScreen(canvas, data):
    drawFileIcons(canvas,data)
    drawTopBar(canvas, data)
    drawBottombar(canvas, data)
    drawDeskTop(canvas, data)

def homescreen_MP(event, data):
    import random
    if 4*data.width // 10 < event.x < 6*data.width // 10 and\
            data.height//6 < event.y < 2*data.height //6:
        data.mode = "Tetris"
        initGames(data)
    elif 7*data.width // 10<event.x<9*data.width // 10 and \
            data.height // 6<event.y<2*data.height //6:
            data.mode="SokobanOptions"
            initGames(data)
    elif 7 * data.width // 10 <event.x< 9 * data.width // 10 and \
            12 * data.height // 24 < event.y < 16 * data.height //24:
        data.mode = "Calculator"
    elif 2 * data.width // 20<event.x<3 * data.width // 20 and\
            20 * data.height // 24<event.y<22 * data.height // 24:
        data.mode = "login_chooseUser"
        initLogin(data)
    elif 4 * data.width // 10<event.x<6 * data.width // 10 and\
            12 * data.height // 24<event.y<16 * data.height // 24:
        f = open("users/" + data.currentUser[0] + "/"+str(random.randint(1, 100)), "w+")
        f.write("Try to edit this file!")
        data.fileIcons= []
        pathString = "users/" + data.currentUser[0]
        filesList = getFiles(pathString)
        for i in range(0, len(filesList)):
            curpath = pathString + "/" + filesList[i]
            curIcon = managesFiles.fakeFileIcon(curpath, 200, 200 * (i + 1))
            data.fileIcons.append(curIcon)
    else:
        #checks if they clicked an icon
        for icon in data.fileIcons:
            if icon.isInBounds(event.x,event.y):
                data.mode = "Text_file"
                data.triggerIcon = icon
                initUtilities(data)

#gets all the files except logo and info
def getFiles(path):
    outList = []
    for fileName in os.listdir(path):
        if fileName != "logo.gif" and fileName != "Info" and fileName!=".DS_Store":
            outList.append(fileName)
    return outList
    

####################################
# BoundingBox
####################################
def initBoundingBox(data):
    data.boundingMargin_side = 3
    data.boundingMargin_top = 18
    data.bounding_x = 1
    data.bounding_xSize = data.boundingMargin_top - 2 * data.bounding_x

def drawBoundingBox(canvas, data):
    canvas.create_rectangle(data.wX - data.boundingMargin_side,
                            data.wY - data.boundingMargin_top,
                            data.wX + data.wW + data.boundingMargin_side,
                            data.wY + data.wH + data.boundingMargin_side,
                            fill="grey")
    canvas.create_oval(data.wX, data.wY - data.boundingMargin_top + data.bounding_x,
                       data.wX + data.bounding_xSize, data.wY - data.bounding_x,
                       fill="red")
    canvas.create_text(data.wX + data.bounding_xSize/2, data.wY - data.bounding_xSize/2 -1,
                       text="X", fill="black", font="Helvetica 15")

def BoundingBox_MP(event,data):
    centerX = data.wX + data.bounding_xSize//2
    centerY = data.wY - data.bounding_x - data.bounding_xSize//2
    if ((event.x-centerX)**2+(event.y-centerY)**2)**0.5 <= data.bounding_xSize/2 + 2:
        if data.mode == "Text_file":
            data.curActiveFile.writeChangesToFile()
        data.mode = "home_screen"
####################################
# Games
####################################

def initGames(data):
    data.GameNames = ["Tetris", "Sudoku", "SokobanOptions",
                      "Sokoban1", "Sokoban2","Sokoban3", "Asteroid"]
    if data.mode == "Tetris":
        data.wX, data.wY = data.width//5, data.height//5
        data.wH, data.wW = Tetris_playTetris()
        Tetris_init(data)
    elif data.mode == "Sudoku":
        pass
    elif "Sokoban" in str(data.mode):
        if data.mode == "Sokoban1":
            data.wX, data.wY = data.width // 6, data.height // 7
            data.wH, data.wW = 660,550
            initSokoban(data)
        elif data.mode == "Sokoban2":
            data.wX, data.wY = data.width // 6, data.height // 7
            data.wH, data.wW = 600,1000
            initSokoban(data)
        elif data.mode == "Sokoban3":
            data.wX, data.wY = data.width // 6, data.height // 7
            data.wH, data.wW = 780, 1000
            initSokoban(data)
        elif data.mode == "SokobanOptions":
            data.wX, data.wY = data.width // 6, data.height // 7
            data.wH, data.wW = 600, 600
            initSokobanOptions(data)
    elif data.mode == "Asteroid":
        pass


def Games_KP(event, data):
    if data.mode == "Tetris":
        Tetris_KP(event, data)
    elif data.mode == "Sudoku":
        pass
    elif "Sokoban" in data.mode:
        if data.mode == "SokobanOptions":
            SokobanOptions_MP(event, data)
        else:
            keyPressedSokoban(event, data)
    elif data.mode == "Asteroid":
        pass


def Games_MP(event, data):
    BoundingBox_MP(event, data)
    if data.mode == "Tetris":
        Tetris_MP(event, data)
    elif data.mode == "Sudoku":
        pass
    elif "Sokoban" in data.mode:
        if data.mode=="SokobanOptions":
            SokobanOptions_MP(event, data)
        else:
            mousePressedSokoban(event, data)
    elif data.mode == "Asteroid":
        pass


def Games_TF(data):
    if data.mode == "Tetris":
        Tetris_TF(data)
    elif data.mode == "Sudoku":
        pass
    elif data.mode == "Sokoban":
        pass
    elif data.mode == "Asteroid":
        pass


def drawGames(canvas, data):
    drawHomeScreen(canvas, data)
    drawBoundingBox(canvas, data)
    if data.mode == "Tetris":
        Tetris_Tetris_redrawAll(canvas, data)
    elif data.mode == "Sudoku":
        pass
    elif "Sokoban" in str(data.mode):
        if data.mode=="SokobanOptions":
            drawSokobanOptions(canvas, data)
        else:
            redrawAllSokoban(canvas, data)
    elif data.mode == "Asteroid":
        pass

####################################
# Games - Tetris
####################################
def Tetris_gameDimensions():
    # preset the dimension
    rows = 20
    cols = 10
    cellSize = 30
    margin = 40
    return rows, cols, cellSize, margin

def Tetris_playTetris():
    rows, cols, cellSize, margin = Tetris_gameDimensions()
    # calculate the board size and start the game!
    height = rows * cellSize + 2 * margin
    width = cols * cellSize + 2 * margin
    return height, width

def Tetris_init(data):
    data.rows, data.cols, data.cellSize, data.margin = Tetris_gameDimensions()
    # empty board is all blue
    data.board = [["blue"] * data.cols for i in range(data.rows)]
    Tetris_newFallingPiece(data)
    data.score = 0
    data.gameover = False

def Tetris_MP(event, data):
    if data.wX + data.wW // 3 < event.x < data.wX + 2 * data.wW // 3 \
            and data.wY + data.wH - 30 < event.y < data.wY + data.wH - 10:
        Tetris_init(data)

def Tetris_KP(event, data):
    import copy
    if not data.gameover:
        if event.char == "s":
            Tetris_newFallingPiece(data)
        # move down, left or right when movable
        if event.keysym == "Down":
            if Tetris_fallingPieceIsLegal(data, 1, 0):
                Tetris_moveFallingPiece(data, 1, 0)
        if event.keysym == "Left":
            if Tetris_fallingPieceIsLegal(data, 0, -1):
                Tetris_moveFallingPiece(data, 0, -1)
        if event.keysym == "Right":
            if Tetris_fallingPieceIsLegal(data, 0, 1):
                Tetris_moveFallingPiece(data, 0, 1)
        # rotate when nothing is blocking
        if event.keysym == "Up":
            temp = copy.deepcopy(data.fallingPiece[0])
            tempStorage = data.fallingPieceRow, data.fallingPieceCol
            Tetris_rotateFallingPiece(data)
            # restore to original orientation when the rotation is illegal
            if not Tetris_fallingPieceIsLegal(data, 0, 0):
                data.fallingPiece = temp, data.fallingPiece[1]
                data.fallingPieceRow, data.fallingPieceCol = tempStorage

def Tetris_TF(data):
    if not data.gameover:
        # move the falling piece down by one block when movable
        if Tetris_fallingPieceIsLegal(data, 1, 0):
            Tetris_moveFallingPiece(data, 1, 0)
        else:
            # place falling piece when not movable
            Tetris_placeFallingPiece(data)

def Tetris_drawCell(row, col, color, canvas, data):
    canvas.create_rectangle(data.wX+col * data.cellSize + data.margin,
                            data.wY+row * data.cellSize + data.margin,
                            data.wX +(col + 1) * data.cellSize + data.margin,
                            data.wY + (row + 1) * data.cellSize + data.margin,
                            fill=color, width=3)

def Tetris_drawBoard(canvas, data):
    # draw the entire board cell by cell
    for row in range(data.rows):
        for col in range(data.cols):
            color = data.board[row][col]
            Tetris_drawCell(row, col,color, canvas, data)

def Tetris_tetrisPiece(data):
    # 7 types of tetris piece
    iPiece = [
        [  True,  True,  True,  True ]
    ]

    jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]

    lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]
    ]

    oPiece = [
        [  True,  True ],
        [  True,  True ]
    ]

    sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]

    tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]

    zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]
    ]
    data.tetrisPieces = [iPiece, jPiece, lPiece, oPiece,
                         sPiece, tPiece, zPiece]
    # each piece corresponds to a specific color
    data.tetrisPieceColors = ["red", "yellow", "magenta",
                              "pink", "cyan", "green", "orange"]

def Tetris_newFallingPiece(data):
    Tetris_tetrisPiece(data)
    import random
    # choose a random shape for the new piece
    randomIndex = random.randint(0, len(data.tetrisPieces) - 1)
    data.fallingPiece = (data.tetrisPieces[randomIndex],
                         data.tetrisPieceColors[randomIndex])
    # row location of the top left piece
    data.fallingPieceRow = 0
    numFallingPieceCols = len(data.fallingPiece[0][0])
    # column location of the top left piece
    data.fallingPieceCol = len(data.board[0]) // 2 - numFallingPieceCols//2
    # test if it's game over
    for row in range(len(data.fallingPiece[0])):
        for col in range(len(data.fallingPiece[0][0])):
            if data.fallingPiece[0][row][col]:
                # game over when the spawn area are not all empty
                r, c = data.fallingPieceRow, data.fallingPieceCol
                if data.board[row + r][col + c] != "blue":
                    data.gameover = True

def Tetris_drawFallingPiece(canvas, data):
    # draw falling piece cell by cell
    for row in range(len(data.fallingPiece[0])):
        for col in range(len(data.fallingPiece[0][0])):
            if data.fallingPiece[0][row][col]:
                color = data.fallingPiece[1]
                Tetris_drawCell(row + data.fallingPieceRow,
                         col + data.fallingPieceCol,
                         color, canvas, data)

def Tetris_moveFallingPiece(data, drow, dcol):
    data.fallingPieceRow += drow
    data.fallingPieceCol += dcol

def Tetris_fallingPieceIsLegal(data, drow, dcol):
    for row in range(len(data.fallingPiece[0])):
        for col in range(len(data.fallingPiece[0][0])):
            if data.fallingPiece[0][row][col]:
                nextRow = data.fallingPieceRow + row + drow
                nextCol = data.fallingPieceCol + col + dcol
                if nextRow > data.rows-1 or nextCol > data.cols-1\
                        or nextCol < 0:
                    return False
                elif data.board[nextRow][nextCol] != "blue":
                    return False
    return True

def Tetris_rotateFallingPiece(data):
    myPiece = data.fallingPiece[0]
    newPiece = [[None] * len(myPiece) for i in range(len(myPiece[0]))]
    # rotate the original piece counterclockwise 90 degrees
    for row in range(len(newPiece)):
        for col in range(len(newPiece[0])):
            newPiece[row][col] = myPiece[col][len(myPiece[0])-1-row]
    # update the location and shape of the original falling piece
    newRow = data.fallingPieceRow + int(len(myPiece) / 2 - len(myPiece[0]) / 2)
    newCol = data.fallingPieceCol + int(len(myPiece[0]) / 2 - len(myPiece) / 2)
    data.fallingPiece = (newPiece, data.fallingPiece[1])
    data.fallingPieceRow = newRow
    data.fallingPieceCol = newCol

def Tetris_placeFallingPiece(data):
    piece, color = data.fallingPiece
    for row in range(len(piece)):
        for col in range(len(piece[0])):
            if piece[row][col] == True:
                # place color on the original board when
                # the falling piece is interrupted
                rowBoard = row + data.fallingPieceRow
                colBoard = col + data.fallingPieceCol
                data.board[rowBoard][colBoard] = color
    # generate a new falling piece
    Tetris_newFallingPiece(data)
    # check if any rows can be removed
    Tetris_removeFullRows(data)

def Tetris_removeFullRows(data):
    totalRemoved = 0
    for row in range(len(data.board)):
        if "blue" not in data.board[row]:
            data.board.pop(row)
            # remove rows when it's completely full
            data.board.insert(0, ["blue"] * data.cols)
            totalRemoved += 1
    # total score will be # of lines removed square
    data.score += totalRemoved ** 2

def Tetris_drawScore(canvas, data):
    canvas.create_text(data.wX+data.wW/2, data.wY+15, text=("Score:", data.score),
                       fill="dark blue", font="30")

def Tetris_drawGameOver(canvas, data):
    # draw text and background when game over
    canvas.create_rectangle(data.wX + data.margin, data.wY + data.wH * 2/5,
                            data.wX + data.wW - data.margin, data.wY+data.wH/2,
                            fill="maroon")
    canvas.create_text(data.wX+data.wW/2, data.wY+data.wH/2, text="Game Over!",
                       fill="white", font="Chalkduster 28 bold", anchor=S)

def Tetris_Tetris_redrawAll(canvas, data):
    canvas.create_rectangle(data.wX, data.wY, data.wX + data.wW, data.wY + data.wH, fill="orange")
    Tetris_drawBoard(canvas, data)
    Tetris_drawFallingPiece(canvas, data)
    Tetris_drawScore(canvas, data)
    canvas.create_rectangle(data.wX+data.wW//3, data.wY+data.wH-30,
                            data.wX+2*data.wW//3, data.wY+data.wH-10,
                            fill=None, width=3)
    canvas.create_text(data.wX+data.wW//2, data.wY+data.wH-20, text="Restart", font="Helvetica 15 bold")
    if data.gameover:
        Tetris_drawGameOver(canvas, data)

####################################
# Games - Sokoban
####################################
def initSokobanOptions(data):
    pass


def SokobanOptions_MP(event, data):
    if data.wX + data.wW // 4 < event.x < data.wX + 3 * data.wW // 4 and \
            data.wY + data.wH // 7 < event.y < data.wY + 2 * data.wH // 7:
        data.mode = "Sokoban1"
        initGames(data)
        initSokoban(data)
    elif data.wX + data.wW // 4 < event.x < data.wX + 3 * data.wW // 4 and \
            data.wY + 3 * data.wH // 7 < event.y < data.wY + 4 * data.wH // 7:
        data.mode = "Sokoban2"
        initGames(data)
        initSokoban(data)
    elif data.wX + data.wW // 4 < event.x < data.wX + 3 * data.wW // 4 and \
            data.wY + 5 * data.wH // 7 < event.y < data.wY + 6 * data.wH // 7:
        data.mode = "Sokoban3"
        initGames(data)
        initSokoban(data)


def drawSokobanOptions(canvas, data):
    canvas.create_rectangle(data.wX, data.wY, data.wX + data.wW, data.wY + data.wH, fill="pink")
    canvas.create_rectangle(data.wX + data.wW // 4,
                            data.wY + data.wH // 7,
                            data.wX + 3 * data.wW // 4,
                            data.wY + 2 * data.wH // 7,
                            fill="white")
    canvas.create_text(data.wX + data.wW // 2, data.wY + 1.5 * data.wH // 7, text="Level 1",
                       font="Chalkduster 50 bold")
    canvas.create_rectangle(data.wX + data.wW // 4,
                            data.wY + 3 * data.wH // 7,
                            data.wX + 3 * data.wW // 4,
                            data.wY + 4 * data.wH // 7,
                            fill="white")
    canvas.create_text(data.wX + data.wW // 2, data.wY + 3.5 * data.wH // 7, text="Level 2",
                       font="Chalkduster 50 bold")
    canvas.create_rectangle(data.wX + data.wW // 4,
                            data.wY + 5 * data.wH // 7,
                            data.wX + 3 * data.wW // 4,
                            data.wY + 6 * data.wH // 7,
                            fill="white")
    canvas.create_text(data.wX + data.wW // 2, data.wY + 5.5 * data.wH // 7, text="Level 3",
                       font="Chalkduster 50 bold")


def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)


def starterBoardSokoban(data):
    # land = 0, wall = 1, box = 2, storage =3, finished = 4, man = 5, man on storage =6
    # please use 700,850 for dimension
    # map 1 difficulty level 2/10
    mymap1 = [[0, 0, 1, 1, 1, 1, 1, 0],
              [1, 1, 1, 0, 0, 0, 1, 0],
              [1, 3, 5, 2, 0, 0, 1, 0],
              [1, 1, 1, 0, 2, 3, 1, 0],
              [1, 3, 1, 1, 2, 0, 1, 0],
              [1, 0, 1, 0, 3, 0, 1, 1],
              [1, 2, 0, 4, 2, 2, 3, 1],
              [1, 0, 0, 0, 3, 0, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 1]]
    # please use 1000,600 for dimension
    # map 3 difficulty level 5/10
    mymap2 = [[0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 1, 1, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 3, 3, 1],
              [1, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1],
              [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 5, 1, 1, 0, 0, 0, 3, 3, 1],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    # please use 1000 780 for dimension
    # map 3 difficulty level 8/10
    mymap3 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
              [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
              [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 1, 0],
              [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 3, 1, 0, 0, 1, 0],
              [1, 0, 1, 0, 1, 0, 2, 0, 0, 2, 0, 3, 5, 3, 0, 0, 1, 0],
              [1, 0, 1, 0, 1, 0, 0, 2, 0, 1, 0, 1, 3, 1, 0, 0, 1, 1],
              [1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1],
              [1, 0, 1, 0, 0, 0, 0, 3, 0, 0, 2, 0, 0, 0, 2, 0, 1, 0],
              [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1],
              [1, 0, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    if data.mode == "Sokoban1":
        return mymap1
    elif data.mode == "Sokoban2":
        return mymap2
    elif data.mode == "Sokoban3":
        return mymap3


def initSokoban(data):
    import copy
    data.board = starterBoardSokoban(data)
    data.originalBoard = copy.deepcopy(data.board)
    data.dimensionR = len(data.board)
    data.dimensionC = len(data.board[0])
    data.size = data.cellSize = min((data.wW // data.dimensionC),
                                    (data.wH // data.dimensionR))
    data.landPos = []
    data.wallPos = []
    data.boxPos = []
    data.stoPos = []
    data.finPos = []
    data.man = []
    # track the positions of land, wall, box, storage, finished box, man, and man on storage
    for row in range(data.dimensionR):
        for col in range(data.dimensionC):
            if data.board[row][col] == 0:
                data.landPos.append((row, col))
            elif data.board[row][col] == 1:
                data.wallPos.append((row, col))
            elif data.board[row][col] == 2:
                data.boxPos.append((row, col))
            elif data.board[row][col] == 3:
                data.stoPos.append((row, col))
            elif data.board[row][col] == 4:
                data.finPos.append((row, col))
            elif data.board[row][col] == 5 or data.board[row][col] == 6:
                data.man.append((row, col))
    data.currentR, data.currentC = data.man[0]


def updataAll(data):
    data.landPos = []
    data.wallPos = []
    data.boxPos = []
    data.stoPos = []
    data.finPos = []
    data.man = []
    # update the position of all elements
    for row in range(data.dimensionR):
        for col in range(data.dimensionC):
            if data.board[row][col] == 0:
                data.landPos.append((row, col))
            elif data.board[row][col] == 1:
                data.wallPos.append((row, col))
            elif data.board[row][col] == 2:
                data.boxPos.append((row, col))
            elif data.board[row][col] == 3:
                data.stoPos.append((row, col))
            elif data.board[row][col] == 4:
                data.finPos.append((row, col))
            elif data.board[row][col] == 5 or data.board[row][col] == 6:
                data.man.append((row, col))
    data.currentR, data.currentC = data.man[0]
    data.finished = False


def mousePressedSokoban(event, data):
    import copy
    # allow users to restart the game
    #print(event.x, event.y, data.wX, data.wY, data.wH, data.wW)
    if data.wX + data.wW / 3 <= event.x <= data.wX + 2 * data.wW / 3 \
            and data.wY + data.wH - 50 <= event.y <= data.wY + data.wH:
        data.board = copy.deepcopy(data.originalBoard)


def keyPressedSokoban(event, data):
    # move only when the move is legal
    if data.finished: return None
    if event.keysym == "Up":
        if movable(data, 0, -1):
            move(data, 0, -1)
    elif event.keysym == "Down":
        if movable(data, 0, 1):
            move(data, 0, 1)
    elif event.keysym == "Right":
        if movable(data, 1, 0):
            move(data, 1, 0)
    elif event.keysym == "Left":
        if movable(data, -1, 0):
            move(data, -1, 0)


def move(data, x, y):
    next = data.board[data.currentR + y][data.currentC + x]
    # when next cell is land
    if next == 0:
        data.board[data.currentR + y][data.currentC + x] = 5
        if data.board[data.currentR][data.currentC] == 6:
            data.board[data.currentR][data.currentC] = 3
        else:
            data.board[data.currentR][data.currentC] = 0
    # when next cell is box
    elif next == 2:
        data.board[data.currentR + y][data.currentC + x] = 5
        if data.board[data.currentR + 2 * y][data.currentC + 2 * x] == 3:
            data.board[data.currentR + 2 * y][data.currentC + 2 * x] = 4
        else:
            data.board[data.currentR + 2 * y][data.currentC + 2 * x] = 2
        if data.board[data.currentR][data.currentC] == 6:
            data.board[data.currentR][data.currentC] = 3
        else:
            data.board[data.currentR][data.currentC] = 0
    # when next cell is storage
    elif next == 3:
        data.board[data.currentR + y][data.currentC + x] = 6
        if data.board[data.currentR][data.currentC] == 6:
            data.board[data.currentR][data.currentC] = 3
        else:
            data.board[data.currentR][data.currentC] = 0
    # when next cell is finished box
    elif next == 4:
        data.board[data.currentR + y][data.currentC + x] = 6
        if data.board[data.currentR + 2 * y][data.currentC + 2 * x] == 3:
            data.board[data.currentR + 2 * y][data.currentC + 2 * x] = 4
        elif data.board[data.currentR + 2 * y][data.currentC + 2 * x] == 0:
            data.board[data.currentR + 2 * y][data.currentC + 2 * x] = 2
        if data.board[data.currentR][data.currentC] == 6:
            data.board[data.currentR][data.currentC] = 3
        else:
            data.board[data.currentR][data.currentC] = 0


def movable(data, x, y):  # check if the new move is legal
    if 0 <= data.currentC + x < data.dimensionC and \
            0 <= data.currentR + y < data.dimensionR:
        next = data.board[data.currentR + y][data.currentC + x]
    else:
        return False
    # illegal if next cell is wall
    if next == 1:
        return False
    elif next == 2 or next == 4:
        # illegal if the cell after the next cell is a wall, a box, or a finished box
        if 0 <= data.currentC + 2 * x < data.dimensionC and \
                0 <= data.currentR + 2 * y < data.dimensionR:
            newNext = data.board[data.currentR + 2 * y][data.currentC + 2 * x]
        else:
            return False
        if newNext == 1 or newNext == 2 or newNext == 4: return False
    return True


def drawAllSokoban(canvas, data):
    size = data.cellSize
    # draw all cells
    for row in range(data.dimensionR):
        for col in range(data.dimensionC):
            canvas.create_rectangle(data.wX + col * size, data.wY + row * size,
                                    data.wX + col * size + data.cellSize,
                                    data.wY + row * size + data.cellSize,
                                    fill="tan",
                                    outline="tan")
            # following are not using if-else statement to avoid bugs when man on a storage
            # draw walls
            if (row, col) in data.wallPos:
                drawWall(canvas, data, row, col)
            # draw boxes
            if (row, col) in data.boxPos:
                boxColor = rgbString(216, 142, 55)
                drawBox(canvas, data, row, col, boxColor)
            # draw storage
            if (row, col) in data.stoPos or data.board[row][col] == 6:
                shrink = size / 3
                canvas.create_oval(data.wX + col * size + shrink,
                                   data.wY + row * size + shrink,
                                   data.wX + col * size + data.cellSize - shrink,
                                   data.wY + row * size + data.cellSize - shrink,
                                   fill="pink",
                                   outline="pink")
            # draw finished box
            if (row, col) in data.finPos:
                finboxColor = rgbString(124, 52, 19)
                drawBox(canvas, data, row, col, finboxColor)
            # draw man
            if (row, col) in data.man or data.board[row][col] == 6:
                drawMan(canvas, data, row, col)
    canvas.create_rectangle(data.wX + data.wW / 3, data.wY + data.wH - 50,
                            data.wX + 2 * data.wW / 3, data.wY + data.wH, outline="red")
    canvas.create_text(data.wX + data.wW / 2, data.wY + data.wH - 25, text="Restart", font="red 24 bold")


def drawWall(canvas, data, row, col):
    size = data.cellSize
    brown = rgbString(159, 149, 93)
    # draw wall
    canvas.create_rectangle(data.wX + col * size, data.wY + row * size,
                            data.wX + col * size + data.cellSize,
                            data.wY + row * size + data.cellSize,
                            fill=brown,
                            outline=brown)
    # draw texture lines on the wall
    for i in range(4):
        canvas.create_line(data.wX + col * size,
                           data.wY + row * size + i * size / 4,
                           data.wX + col * size + data.cellSize,
                           data.wY + row * size + i * size / 4)
    for rows in range(4):
        canvas.create_line(data.wX + col * size + (rows % 2) * size / 4,
                           data.wY + row * size + rows * size / 4,
                           data.wX + col * size + (rows % 2) * size / 4,
                           data.wY + row * size + rows * size / 4 + size / 4)
        canvas.create_line(data.wX + col * size + (rows % 2) * size / 4 + size / 2,
                           data.wY + row * size + rows * size / 4,
                           data.wX + col * size + (rows % 2) * size / 4 + size / 2,
                           data.wY + row * size + rows * size / 4 + size / 4)


def drawBox(canvas, data, row, col, color):  # draw boxes on desired coordinate
    size = data.cellSize
    canvas.create_rectangle(data.wX + col * size,
                            data.wY + row * size,
                            data.wX + col * size + size,
                            data.wY + row * size + size,
                            fill=color)
    shrink = size / 5
    canvas.create_rectangle(data.wX + col * size + shrink,
                            data.wY + row * size + shrink,
                            data.wX + col * size + size - shrink,
                            data.wY + row * size + size - shrink,
                            fill=color)


def drawMan(canvas, data, row, col):
    # draw man on desired coordinate
    size = data.cellSize
    rx = col * size
    ry = row * size
    # draw head
    canvas.create_oval(data.wX + rx + (size / 3), data.wY + ry + 0,
                       data.wX + rx + 2 * size / 3, data.wY + ry + (size / 3), fill="black")
    # draw body
    canvas.create_line(data.wX + rx + (size / 2), data.wY + ry + (size / 3), data.wX + rx + (size / 2),
                       data.wY + ry + (size / 3) + size / 3, width=4)
    dir1 = [(-1, -1), (1, -1)]
    # draw legs
    for a, b in dir1:
        canvas.create_line(data.wX + rx + (size / 2),
                           data.wY + ry + (size / 3) + 2 * size / 9,
                           data.wX + rx + (size / 2) + a * size / 4,
                           data.wY + ry + (size / 3) + 2 * size / 9 + b * size / 4,
                           width=4)
    # draw arms
    dir2 = [(-1, 1), (1, 1)]
    for a, b in dir2:
        canvas.create_line(data.wX + rx + (size / 2),
                           data.wY + ry + (size / 3) + size / 3,
                           data.wX + rx + (size / 2) + a * size / 4,
                           data.wY + ry + (size / 3) + size / 3 + b * size / 4,
                           width=4)


def isfinishedSokoban(data):  # check if the board is completed
    for row in range(data.dimensionR):
        for col in range(data.dimensionC):  # finished when no there is no unfinished box
            if data.board[row][col] == 2:
                return False
    return True


def redrawAllSokoban(canvas, data):
    updataAll(data)
    drawAllSokoban(canvas, data)
    if isfinishedSokoban(data):  # escape when finished
        data.finished = True
        # draw some nice messages to congrats the user
        canvas.create_rectangle(data.wX + 0, data.wY + 2 * data.wH / 5,
                                data.wX + data.wW,
                                data.wX + 3 * data.wH / 5, fill="green")
        canvas.create_text(data.wW / 2, data.wH / 2,
                           text="You Won!",
                           fill="yellow",
                           font="blue 35 bold underline")


####################################
# Utilities
####################################

def initUtilities(data):
    data.UtilityNames = ["Calculator", "Chat_Bot", "Text_file"]
    if data.mode == "Calculator":
        pass
    elif data.mode == "Chat_Bot":
        pass
    elif data.mode == "Text_file":
        initTextFile(data)



def drawUtilities(canvas, data):
    drawHomeScreen(canvas,data)
    drawBoundingBox(canvas,data)
    if data.mode == "Calculator":
        drawBoundingBox(canvas, data)
    elif data.mode == "Chat_Bot":
        drawBoundingBox(canvas, data)
    elif data.mode == "Text_file":
        drawTextFile(canvas,data)


def Utilities_KP(event, data):
    if data.mode == "Calculator":
        pass
    elif data.mode == "Chat_Bot":
        pass
    elif data.mode == "Text_file":
        text_file_KP(event,data)


def Utilities_MP(event, data):
    BoundingBox_MP(event,data)
    if data.mode == "Calculator":
        pass
    elif data.mode == "Chat_Bot":
        pass
    elif data.mode == "Text_file":
        pass


def Utilities_TF(data):
    if data.mode == "Calculator":
        pass
    elif data.mode == "Chat_Bot":
        pass
    elif data.mode == "Text_file":
        pass

"""
####################################
# Calculator
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
    if (data.modeCal == "basic"):
        basicMousePressed(event, data)
    elif (data.modeCal == "long"):
        longMousePressed(event, data)
    elif (data.modeCal == "special"):
        specialMousePressed(event, data)
    elif (data.modeCal == "help"):
        helpMousePressed(event, data)
    elif (data.modeCal == "start"):
        splashScreenMousePressed(event, data)


def keyPressed(event, data):
    if (data.modeCal == "basic"):
        basicKeyPressed(event, data)
    elif (data.modeCal == "long"):
        longKeyPressed(event, data)
    elif (data.modeCal == "special"):
        specialKeyPressed(event, data)
    elif (data.modeCal == "help"):
        helpKeyPressed(event, data)
    elif (data.modeCal == "start"):
        splashScreenKeyPressed(event, data)


def timerFired(data):
    if (data.modeCal == "basic"):
        basicTimerFired(data)
    elif (data.modeCal == "long"):
        longTimerFired(data)
    elif (data.modeCal == "special"):
        specialTimerFired(data)
    elif (data.modeCal == "help"):
        helpTimerFired(data)
    elif (data.modeCal == "start"):
        splashScreenTimerFired(data)


def redrawAll(canvas, data):
    if (data.modeCal == "basic"):
        basicRedrawAll(canvas, data)
    elif (data.modeCal == "long"):
        longRedrawAll(canvas, data)
    elif (data.modeCal == "special"):
        specialRedrawAll(canvas, data)
    elif (data.modeCal == "help"):
        helpRedrawAll(canvas, data)
    elif (data.modeCal == "start"):
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


# special mode

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


# long mode

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

"""
####################################
# Text Files
####################################
def initTextFile(data):
                        #Left, top, right, bot
                    #CHANGE THIS TO CHANGE TEXT WINDOW LOCATION!
    bounds = (data.width//3,data.height//4,2*data.width//4,None)
    data.wH,data.wW,data.wX,data.wY = (0,0,0,0)
    data.curActiveFile = managesFiles.fakeFile(data,data.triggerIcon.associatedFilePath,bounds)
    width = abs(bounds[0] - bounds[2])
    data.wW,data.wX,data.wY = width,bounds[0],bounds[1]


def text_file_KP(event,data):
    if event.keysym == "BackSpace":
        data.curActiveFile.text = data.curActiveFile.text[:-1]
    elif len(event.keysym) == 1:
        data.curActiveFile.text += event.keysym
    elif event.keysym == "Return":
        data.curActiveFile.text += "\n"
    elif event.keysym == "space":
        data.curActiveFile.text += " "
    elif event.keysym == "question":
        data.curActiveFile.text += "?"
    elif event.keysym == "period":
        data.curActiveFile.text += "."
    elif event.keysym == "exclam":
        data.curActiveFile.text += "!"
    elif event.keysym == "quoteright":
        data.curActiveFile.text += "'"
    elif event.keysym == "F2":
        pass
        data.curActiveFile.writeChangesToFile()
        #LeftEdge,secondLayer TopEdge, RightEdge, None (always)
        #bounds = (data.width//4,data.height//4,3*data.width//4,None)
        #data.curActiveFile = managesFiles.fakeFile(data,"NoneName",bounds)
    else:
        pass
        #print(event.keysym)
    
    
def text_file_MP(event,data):
    if data.curActiveFile.isInBoundsOfCloseButton(event.x,event.y):
        data.curActiveFile.writeChangesToFile()
        data.mode = "home_screen"

def drawTextFile(canvas,data):
    #drawHomescreen()
    data.curActiveFile.draw(data,canvas)


####################################
# Main Functions
####################################

def init(data):
    data.mode = "login_chooseUser"
    data.currentUser = ""
    initLogin_chooseUser(data)
    initLogin(data)
    initHomeScreen(data)
    initCreat_account(data)
    initGames(data)
    initUtilities(data)
    initBoundingBox(data)


def mousePressed(event, data):
    if data.mode == "login_chooseUser":
        login_chooseUser_MP(event, data)
    elif data.mode == "login":
        login_MP(event, data)
    elif data.mode == "home_screen":
        homescreen_MP(event, data)
    elif data.mode == "create_account":
        createAccount_MP(event, data)
    elif data.mode in data.GameNames:
        Games_MP(event, data)
    elif data.mode in data.UtilityNames:
        Utilities_MP(event,data)



def keyPressed(event, data):
    if data.mode == "login":
        login_KP(event, data)
    elif data.mode == "create_account":
        createAccount_KP(event, data)
    elif data.mode in data.GameNames:
        Games_KP(event, data)
    elif data.mode in data.UtilityNames:
        Utilities_KP(event,data)


def timerFired(data):
    if data.mode == "login":
        login_TF(data)
    elif data.mode in data.GameNames:
        Games_TF(data)


def redrawAll(canvas, data):
    #print(data.mode)
    # print(data.currentUser)
    if data.mode == "login_chooseUser":
        drawLogin_chooseUser(canvas, data)
    elif data.mode == "login":
        drawLogin(canvas, data)
    elif data.mode == "home_screen":
        drawHomeScreen(canvas, data)
    elif data.mode == "create_account":
        drawCreate_account(canvas, data)
    elif data.mode in data.GameNames:
        drawGames(canvas, data)
    elif data.mode in data.UtilityNames:
        drawUtilities(canvas,data)



####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='light blue', width=0)
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
    root.resizable(width=True, height=True)  # prevents resizing window
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


run(1680, 920)
# run(900, 600)