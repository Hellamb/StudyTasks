import tkinter as tk
from tkinter import Toplevel, messagebox
from tkinter import filedialog as fd
import codecs as cod

BUTTON_TEXT_FONT = ("Comfotraa", 12)
TEXTAREA_TEXT_FONT = ('Comfortaa', 14)
ACTIVEBG_COLOR = '#C0C0C0'

DARK_BUTTON_COLOR = '#686868'
DARK_TEXT_COLOR_1 = '#F0EEB8'
DARK_TEXTAREA_COLOR = '#303030'
DARK_TOOLBAR_COLOR = '#444444'

LIGHT_BUTTON_COLOR = '#ECECEC'
LIGHT_TEXT_COLOR_1 = '#272727'
LIGHT_TEXTAREA_COLOR = '#F2F2EF'
LIGHT_TOOLBAR_COLOR = '#F5F5F5'

textFont = 14
darkmode = True
searchWord = ''
searchWordPosition = ''
searchCoursorPosition = '1.0'
openedFile = False
isChanged = True



def openFile():
    global openedFile
    fileName = fd.askopenfilename()
    file = cod.open(fileName, 'r+', "utf_8_sig")
    fileText = file.read()
    mainTextArea.delete(1.0,tk.END)
    mainTextArea.insert(1.0, fileText)
    root.title('Notepad# открыто: '+ fileName)
    openedFile = fileName

def saveFile():
    global openedFile
    if (not openedFile):
        saveAsFile()
    else:
        file = cod.open(openedFile, 'w', 'utf_8_sig')
        fileText = mainTextArea.get(1.0,tk.END)
        file.write(fileText)
        file.close()

def closeFile():
    global openedFile
    isSave = messagebox.askyesno(title = 'Вспомагательное окно', message = 'Сохранить файл?')
    if isSave:
        saveFile()
    mainTextArea.delete(1.0,tk.END)
    if (openedFile):
        root.title('Notepad#')
        openedFile = False

def saveAsFile():
    fileName = fd.asksaveasfilename(filetypes = (('файл типа txt', '*.txt'),('Любой тип файла', '*.*')))
    file = open(fileName, 'w')
    fileText = mainTextArea.get(1.0,tk.END)
    file.write(fileText)

def exitProgramm():
    root.destroy()

def themeChanger():
    global darkmode
    if(darkmode):
        themeButton.config(bg = LIGHT_BUTTON_COLOR, fg = LIGHT_TEXT_COLOR_1,text = 'К тёмной')
        changeButton.config(bg = LIGHT_BUTTON_COLOR, fg = LIGHT_TEXT_COLOR_1)
        mainTextArea.config(bg = LIGHT_TEXTAREA_COLOR,fg = LIGHT_TEXT_COLOR_1)
        searchEnter.config(bg= LIGHT_TEXTAREA_COLOR, fg =LIGHT_TEXT_COLOR_1)
        changeEnter.config(bg= LIGHT_TEXTAREA_COLOR, fg =LIGHT_TEXT_COLOR_1)
        leftSearchButton.config(bg = LIGHT_BUTTON_COLOR, fg = LIGHT_TEXT_COLOR_1)
        centralSearchButton.config(bg = LIGHT_BUTTON_COLOR, fg = LIGHT_TEXT_COLOR_1)
        rightSearchButton.config(bg = LIGHT_BUTTON_COLOR, fg = LIGHT_TEXT_COLOR_1)
        toolBarFrame['bg'] = LIGHT_TOOLBAR_COLOR
        darkmode = False
    else:
        themeButton.config(bg = DARK_BUTTON_COLOR, fg = DARK_TEXT_COLOR_1,text = 'К светлой')
        changeButton.config(bg = DARK_BUTTON_COLOR, fg = DARK_TEXT_COLOR_1)
        mainTextArea.config(bg = DARK_TEXTAREA_COLOR,fg = DARK_TEXT_COLOR_1)
        searchEnter.config(bg= DARK_TEXTAREA_COLOR, fg =DARK_TEXT_COLOR_1)
        changeEnter.config(bg= DARK_TEXTAREA_COLOR, fg =DARK_TEXT_COLOR_1)
        leftSearchButton.config(bg = DARK_BUTTON_COLOR, fg = DARK_TEXT_COLOR_1)
        centralSearchButton.config(bg = DARK_BUTTON_COLOR, fg = DARK_TEXT_COLOR_1)
        rightSearchButton.config(bg = DARK_BUTTON_COLOR, fg = DARK_TEXT_COLOR_1)
        toolBarFrame['bg'] = DARK_TOOLBAR_COLOR
        darkmode = True

def nextPos(word, pos):
    try:
        ans = []
        pos = mainTextArea.search(searchWord,pos, stopindex = 'end')
        length = len(word)
        row, col = pos.split('.')
        end = int(col) + length
        end = row + '.' + str(end)
        ans.append(pos)
        ans.append(end)
        return ans
    except:
        print('')

def fontPlusSize():
    global textFont
    textFont += 2
    mainTextArea['font'] = ('Comfortaa',textFont)

def fontMinusSize():
    global textFont
    textFont -= 2
    mainTextArea['font'] = ('Comfortaa',textFont)   
    
def textChange():
    try:
        mainTextArea.tag_remove('searchedText', '1.0' , tk.END)
        global isChanged
        global searchWord
        global searchWordPosition
        global searchCoursorPosition   
        if(searchCoursorPosition == '1.0'):
            if(searchWord != searchEnter.get()):
                searchWord = searchEnter.get()
            pos = mainTextArea.search(searchWord,'1.0', stopindex = 'end')
            while pos:
                startEnd = nextPos(searchWord, pos)
                pos = startEnd[0]
                cur = startEnd[1]
                mainTextArea.delete(pos, cur)
                mainTextArea.insert(pos, changeEnter.get())
                row, col = pos.split('.')
                length = len(changeEnter.get())
                pos = int(col) + length
                pos = row + '.' + str(pos)
            return
        if (isChanged) :
            return     
        isChanged = True
        mainTextArea.delete(searchWordPosition, searchCoursorPosition)
        mainTextArea.insert(searchWordPosition, changeEnter.get())
    except:
        print('')    
     

def search():
    global isChanged
    isChanged = False
    mainTextArea.tag_remove('searchedText', '1.0' , tk.END)
    if(searchEnter.get() == ''):
        return 
    global searchWordPosition
    global searchCoursorPosition
    searchCoursorPosition = '1.0'
    searchWordPosition = '1.0'

    searchWord = searchEnter.get()

    pos = mainTextArea.search(searchWord,'1.0', stopindex = 'end')
    while pos:
        length = len(searchWord)
        row, col = pos.split('.')
        end = int(col) + length
        end = row + '.' + str(end)
        mainTextArea.tag_add('searchedText', pos, end)
        pos = mainTextArea.search(searchWord, end, stopindex=tk.END)

def searchRight():
    try:
        mainTextArea.tag_remove('searchedText', '1.0' , tk.END)
        global isChanged
        global searchWordPosition
        global searchCoursorPosition
        global searchWord
        isChanged = False
        if(searchWord != searchEnter.get()):
            searchWord = searchEnter.get()
            searchWordPosition = '1.0' 
            searchCoursorPosition = '1.0'   
        startEnd = nextPos(searchWord, searchCoursorPosition)
        searchWordPosition = startEnd[0]
        searchCoursorPosition = startEnd[1]
        mainTextArea.tag_add('searchedText', searchWordPosition, searchCoursorPosition)
    except:
        searchWordPosition = '1.0' 
        searchCoursorPosition = '1.0'

def searchLeft():
    
    lastPos = ''
    lastCur = ''
    global isChanged
    isChanged = False
    global searchWord
    if(searchWord != searchEnter.get()):
        searchWord = searchEnter.get()
    if(searchWord == ''):
        return    
    try:
        mainTextArea.tag_remove('searchedText', 1.0 , tk.END)
        global searchWordPosition
        global searchCoursorPosition

        startEnd = nextPos(searchWord, '1.0')
        pos = startEnd[0] 
        cur = startEnd[1]
        while True:
            lastPos = pos
            lastCur = cur
            startEnd = nextPos(searchWord, cur)
            pos = startEnd[0]
            cur = startEnd[1]
            if(not pos or pos == searchWordPosition):
                searchWordPosition = lastPos
                searchCoursorPosition = lastCur
                mainTextArea.tag_add('searchedText', searchWordPosition, searchCoursorPosition)
                return
    except:
        searchWordPosition = lastPos
        searchCoursorPosition = lastCur
        mainTextArea.tag_add('searchedText', searchWordPosition, searchCoursorPosition)  


def palindromWin():
    palWin = tk.Toplevel(root)
    palWin.title("Palindrom")
    palWin.resizable(False,False)
    palWin.geometry('300x160')

    inValue = tk.Entry(palWin, width = 100, font = 'Comfortaa 30')
    processButton = tk.Button(palWin,text = 'Обработать данные',width=30, font = 'Comfortaa 20',bg = 'gray', command = lambda: outValue.config(text = palindrom(inValue.get())))
    outValue = tk.Label(palWin,width = 100, font = 'Comfortaa 30')

    inValue.pack()
    processButton.pack()
    outValue.pack()

def palindrom(word):
    if(word == ""):
        return 'Error'
    pal = True
    l = len(word)

    for i in range(l//2):
        if(word[i] !=  word[l - i-1] ):
            pal = False

    if(pal):
        return 'Палиндром'
    else:
        return 'Не палиндром'

def calculatorWin():
    calcWin = tk.Toplevel(root)
    calcWin.title("Calculator")
    calcWin.resizable(False,False)
    calcWin.geometry('300x160')

    inValue = tk.Entry(calcWin,width = 100, font = 'Comfortaa 30')
    processButton = tk.Button(calcWin,text = 'Обработать данные',width=30, font = 'Comfortaa 20',bg = 'gray', command = lambda: outValue.config(text = calc(inValue.get())))
    outValue = tk.Label(calcWin,width = 100, font = 'Comfortaa 30')

    inValue.pack()
    processButton.pack()
    outValue.pack()



def calc(row):
    l = len(row)
    result = 0
    current =''
    isPositive = True
    try:
        for i in range(l):
            if(row[i].isnumeric()):
                current += row[i]
            elif(row[i] == '+'):
                if(isPositive):
                    result += int(current)
                    current = ''
                else:
                    result -= int(current)
                    isPositive = True
                    current = ''
            elif(row[i] == '-'):
                if(isPositive):
                    result += int(current)
                    isPositive = False
                    current = ''
                else:
                    result -= int(current)
                    current =''
        if(isPositive):
            result += int(current)
        else:
            result -= int(current)    


        return result
    except:
        return 'ERROR'

def romanWin():
    romWin = tk.Toplevel(root)
    romWin.geometry('300x160')
    romWin.title('Roman')
    romWin.resizable(False, False)

    inValue = tk.Entry(romWin,width = 100, font = 'Comfortaa 30')
    processButton = tk.Button(romWin,text = 'Обработать данные',width=30, font = 'Comfortaa 20',bg = 'gray', command = lambda: outValue.config(text = toRoman(inValue.get())))
    outValue = tk.Label(romWin,width = 100, font = 'Comfortaa 30')

    inValue.pack()
    processButton.pack()
    outValue.pack()

def toRoman(num):
    roman = {
        1000 : 'M',
        900 : 'CM',
        500 : 'D',
        400 : 'CD',
        100 : 'C',
        90 : 'XC',
        50 : 'L',
        40 : 'XL',
        10 : 'X',
        9 : 'IX',
        5 : 'V',
        4 : 'IV',
        1 : 'I'
    }
    try:
        num = int(num)
        result = ''
        for i in roman.keys():
            rNum = num // i
            num -= rNum * i
            result += roman[i] * rNum
        return result
    except:
        return 'ERROR'   


root = tk.Tk()

root.geometry('1200x700')
root.title('Notepad#')
root.wm_attributes('-alpha' , 0.95)
root.iconbitmap('materials/headIcon.ico')


mainTextArea = tk.Text(
    root, 
    width = 240, 
    height= 180, 
    wrap = 'word',
    bg = DARK_TEXTAREA_COLOR,
    fg = DARK_TEXT_COLOR_1,
    font = TEXTAREA_TEXT_FONT
)

scrollFrame = tk.Frame(root)
verticalScrollBar = tk.Scrollbar(scrollFrame, command = mainTextArea.yview)
mainTextArea.config(yscrollcommand=verticalScrollBar.set)

topMenu = tk.Menu(root)
root.config(menu = topMenu)

fileSubmenu = tk.Menu(topMenu, tearoff=0)
fileSubmenu.add_command(label = "Открыть файл...", command = openFile)
fileSubmenu.add_command(label= "Сохранить", command = saveFile)
fileSubmenu.add_command(label = "Сохранить как...", command = saveAsFile)
fileSubmenu.add_command(label = "Закрыть файл", command = closeFile)
fileSubmenu.add_command(label = "Выйти", command = exitProgramm)

vievSubmenu = tk.Menu(topMenu, tearoff = 0)
vievSubmenu.add_command(label = "Увеличить шрифт", command = fontPlusSize)
vievSubmenu.add_command(label = "Уменьшить шрифт", command = fontMinusSize)

taskSubmenu = tk.Menu(topMenu, tearoff = 0)
taskSubmenu.add_command(label = "Палиндром", command = palindromWin)
taskSubmenu.add_command(label = "Калькулятор", command = calculatorWin)
taskSubmenu.add_command(label = "В Римские", command = romanWin)

topMenu.add_cascade(label = 'Файл', menu = fileSubmenu)
topMenu.add_cascade(label = 'Вид', menu = vievSubmenu)
topMenu.add_cascade(label = 'Задания', menu = taskSubmenu)


toolBarFrame = tk.Frame(root,bg = DARK_TOOLBAR_COLOR)
searchButtonsFrame = tk.Frame(toolBarFrame,width = 12, bg = DARK_TOOLBAR_COLOR)


leftSearchButton = tk.Button( 
    searchButtonsFrame,
    text = '<',
    width = 2,
    bg = DARK_BUTTON_COLOR,
    fg = DARK_TEXT_COLOR_1,
    font = BUTTON_TEXT_FONT,
    relief= tk.FLAT,
    activebackground= ACTIVEBG_COLOR,
    command= searchLeft
    )

centralSearchButton = tk.Button( 
    searchButtonsFrame,
    width = 4,
    text = '🔎',
    bg = DARK_BUTTON_COLOR,
    fg = DARK_TEXT_COLOR_1,
    font = BUTTON_TEXT_FONT,
    relief= tk.FLAT,
    activebackground= ACTIVEBG_COLOR,
    command = search
)


rightSearchButton = tk.Button( 
    searchButtonsFrame,
    text = '>',
    width = 2,
    bg = DARK_BUTTON_COLOR,
    fg = DARK_TEXT_COLOR_1,
    font = BUTTON_TEXT_FONT,
    relief= tk.FLAT,
    activebackground= ACTIVEBG_COLOR,
    command = searchRight
    )            



searchEnter = tk.Entry(
    toolBarFrame,
    width = 10,
    bg = DARK_TEXTAREA_COLOR,
    fg = DARK_TEXT_COLOR_1,
    font = BUTTON_TEXT_FONT
)

changeEnter = tk.Entry(
    toolBarFrame,
    width = 10,
    bg = DARK_TEXTAREA_COLOR,
    fg = DARK_TEXT_COLOR_1,
    font = BUTTON_TEXT_FONT
)

mainTextArea.tag_config('searchedText', background= 'yellow', foreground= 'black')

themeButton = tk.Button(
    toolBarFrame,
    width = 10,
    text = 'К светлой',
    bg =  DARK_BUTTON_COLOR,
    fg = DARK_TEXT_COLOR_1,
    font = BUTTON_TEXT_FONT,
    command = themeChanger,
    relief= tk.FLAT,
    activebackground= ACTIVEBG_COLOR
)

changeButton = tk.Button(
    toolBarFrame,
    width = 10,
    text = 'Заменить',
    bg =  DARK_BUTTON_COLOR,
    fg = DARK_TEXT_COLOR_1,
    font = BUTTON_TEXT_FONT,
    relief= tk.FLAT,
    command = textChange,
    activebackground= ACTIVEBG_COLOR
)

toolBarFrame.pack(side = tk.LEFT, fill = tk.Y)
themeButton.pack(side = tk.TOP)
searchEnter.pack(side = tk.TOP)
searchButtonsFrame.pack(side = tk.TOP)
leftSearchButton.pack(side = tk.LEFT)
centralSearchButton.pack(side = tk.LEFT)
rightSearchButton.pack(side = tk.RIGHT)
changeEnter.pack(side = tk.TOP)
changeButton.pack(side = tk.TOP)

scrollFrame.pack(side = tk.RIGHT, fill = tk.Y)
verticalScrollBar.pack(side = tk.RIGHT, fill = tk.Y)

mainTextArea.pack(side = tk.LEFT,fill = tk.X)


root.mainloop()