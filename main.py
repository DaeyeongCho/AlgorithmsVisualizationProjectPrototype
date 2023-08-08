import ctypes
import random
import threading
import time
import tkinter
from tkinter import *
from tkinter import messagebox, ttk

from define import *

def main():
## ====================== 정의 ====================== ##

    # 윈도우 창 정의
    window = Tk()
    window.title(TITLE)
    window.geometry(GEOMETRY)
    window.resizable(width=FALSE, height=FALSE)

    # 입력 타입 정의
    intVarRadioButtonSelectAlgorithm = IntVar()
    strVarComboboxSelectAlgorithm = StringVar()
    boolVarCheckbuttonAdvancedMenu = BooleanVar()

    intVarSpinboxDataSize = IntVar()
    intVarSpinboxDataSize.set(DATA_SIZE_DEFAULT)
    doubleVarSpeedLimit = DoubleVar()
    doubleVarSpeedLimit.set(SPEED_LIMIT_DEFAULT)
    intVarShuffleTimes = IntVar()
    intVarShuffleTimes.set(SHUFFLE_TIMES_DEFAULT)
    boolVarShuffleVisible = BooleanVar()
    boolVarShuffleVisible.set(True)
    intVarSearchValue = IntVar()
    intVarSearchValue.set(SEARCH_VALUE_DEFAULT)

    # 프레임 정의
    frameGeneralMenu = tkinter.Frame(window)
    frameAdvancedMenu = tkinter.Frame(window)
    frameSimulation = tkinter.Frame(window)

    frameSimulationHint = tkinter.Frame(frameSimulation)
    frameSimulationState = tkinter.Frame(frameSimulation)
    frameSimulationElapsedTime = tkinter.Frame(frameSimulation)
    frameSimulationEndButtons = tkinter.Frame(frameSimulation)

    # General Menu 프레임 하위 위젯 정의
    radioButtonSelectAlgorithm = [ Radiobutton(frameGeneralMenu, text=RADIO_BUTTON_SELECT_ALGORITHM[0], variable=intVarRadioButtonSelectAlgorithm, value=0, command=lambda: radioButtonSelectAlgorithmFunc(intVarRadioButtonSelectAlgorithm)),
                                   Radiobutton(frameGeneralMenu, text=RADIO_BUTTON_SELECT_ALGORITHM[1], variable=intVarRadioButtonSelectAlgorithm, value=1, command=lambda: radioButtonSelectAlgorithmFunc(intVarRadioButtonSelectAlgorithm)) ]
    
    comboboxSelectAlgorithm = ttk.Combobox(frameGeneralMenu, textvariable=strVarComboboxSelectAlgorithm, values=SORT_ALGORITHMS, state="readonly")
    comboboxSelectAlgorithm.set(SORT_ALGORITHMS[0])

    checkbuttonAdvancedMenu = ttk.Checkbutton(frameGeneralMenu, text=ADVANCED_MENU, variable=boolVarCheckbuttonAdvancedMenu, command=lambda: checkbuttonAdvancedMenuFunc(boolVarCheckbuttonAdvancedMenu))

    buttonStart = Button(frameGeneralMenu, text=START, command=lambda: buttonStartFunc())
    
    # Advanced Menu 프레임 하위 위젯 정의
    labelDataSize = Label(frameAdvancedMenu, text=DATA_SIZE)
    spinboxDataSize = Spinbox(frameAdvancedMenu, from_=DATA_SIZE_MIN, to=DATA_SIZE_MAX, increment=DATA_SIZE_INCREMENT, textvariable=intVarSpinboxDataSize, width=SPIN_BOX_WIDTH, command=lambda: spinboxDataSizeFunc())

    labelSpeedLimit = Label(frameAdvancedMenu, text=SPEED_LIMIT)
    spinboxSpeedLimit = Spinbox(frameAdvancedMenu, from_=SPEED_LIMIT_MIN, to=SPEED_LIMIT_MAX, increment=SPEED_LIMIT_INCREMENT, textvariable=doubleVarSpeedLimit, width=SPIN_BOX_WIDTH)

    labelShuffleTimes = Label(frameAdvancedMenu, text=SHUFFLE_TIMES)
    spinboxShuffleTimes = Spinbox(frameAdvancedMenu, from_=SHUFFLE_TIMES_MIN, to=SHUFFLE_TIMES_MAX, increment=SHUFFLE_TIMES_INCREMENT, textvariable=intVarShuffleTimes, width=SPIN_BOX_WIDTH)

    checkbuttonShuffleVisible = ttk.Checkbutton(frameAdvancedMenu, text=SHUFFLE_VISIBLE, variable=boolVarShuffleVisible)

    labelSearchValue = Label(frameAdvancedMenu, text=SEARCH_VALUE)
    spinboxSearchValue = Spinbox(frameAdvancedMenu, from_=SEARCH_VALUE_MIN, to=int(intVarSpinboxDataSize.get()), increment=SEARCH_VALUE_INCREMENT, textvariable=intVarSearchValue, width=SPIN_BOX_WIDTH)

    # Simulation 프레임 하위 위젯 정의
    canvas = Canvas(frameSimulation, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background=CANVAS_COLOR)

    labelHint = [ Label(frameSimulationHint, text=LABEL_HINT[0], foreground=RED),
                  Label(frameSimulationHint, text=LABEL_HINT[1], foreground=BLUE),
                  Label(frameSimulationHint, text=LABEL_HINT[2], foreground=YELLOW), 
                  Label(frameSimulationHint, text=LABEL_HINT[3], foreground=BLACK), 
                  Label(frameSimulationHint, text=LABEL_HINT[4], foreground=BLACK), ]
    
    labelState = [ Label(frameSimulationState, text=LABEL_STATE[0]),
                   Label(frameSimulationState, text=LABEL_STATE[1]) ]

    labelElapsedTime = [ Label(frameSimulationElapsedTime, text=ELAPSED_TIME[0]),
                         Label(frameSimulationElapsedTime, text=ELAPSED_TIME[1]) ]
    
    buttonEnd = [ Button(frameSimulationEndButtons, text=END_BUTTONS[0], command=lambda: buttonStopFunc(), state="disabled"),
                  Button(frameSimulationEndButtons, text=END_BUTTONS[1], command=lambda: buttonReplayFunc(), state="disabled"),
                  Button(frameSimulationEndButtons, text=END_BUTTONS[2], command=lambda: buttonEndFunc(), state="disabled")]



## ====================== 프로그램 ====================== ##

    # General Menu 프로그램
    def radioButtonSelectAlgorithmFunc(intVar):
        if intVar.get() == 0:
            comboboxSelectAlgorithm.configure(values=SORT_ALGORITHMS)
            comboboxSelectAlgorithm.set(SORT_ALGORITHMS[0])
            labelShuffleTimes.pack(side=LEFT, padx=(10, 0))
            spinboxShuffleTimes.pack(side=LEFT, padx=(2, 0))
            checkbuttonShuffleVisible.pack(side=LEFT, padx=(10, 0))
            labelSearchValue.pack_forget()
            spinboxSearchValue.pack_forget()
        else:
            comboboxSelectAlgorithm.configure(values=SEARCH_ALGORITHMS)
            comboboxSelectAlgorithm.set(SEARCH_ALGORITHMS[0])
            labelShuffleTimes.pack_forget()
            spinboxShuffleTimes.pack_forget()
            checkbuttonShuffleVisible.pack_forget()
            labelSearchValue.pack(side=LEFT, padx=(10, 0))
            spinboxSearchValue.pack(side=LEFT, padx=(2, 0))

    def checkbuttonAdvancedMenuFunc(boolVar):
        if not boolVar.get():
            frameAdvancedMenu.pack_forget()
        else:
            frameAdvancedMenu.pack(side=TOP)

    def buttonStartFunc():
        global sortOrSearchAlgorithm
        global algorithm
        global dataSize
        global speedLimit
        global shuffleTime
        global shuffleVisible
        global searchValue
        global remindSearchValue
        global data

        canvas.delete(ALL)
        data = []

        labelState[1].config(text=LABEL_STATE[1])
        labelElapsedTime[1].config(text=ELAPSED_TIME[1])
        labelHint[4].configure(text=LABEL_HINT[4])
        buttonEnd[1].config(state="disabled")
        buttonEnd[2].config(state="disabled")

        frameSimulation.pack(side=BOTTOM, pady=(0, 10))
        sortOrSearchAlgorithm = intVarRadioButtonSelectAlgorithm.get()
        algorithm = strVarComboboxSelectAlgorithm.get()
        dataSize = intVarSpinboxDataSize.get()
        speedLimit = doubleVarSpeedLimit.get()
        shuffleTime = intVarShuffleTimes.get()
        shuffleVisible = boolVarShuffleVisible.get()
        searchValue = intVarSearchValue.get()
        remindSearchValue = searchValue

        buttonStart.config(state="disabled")

        createSticks()
        startSimulationThread()


    # Advanced Menu 프로그램
    def spinboxDataSizeFunc() :
        spinboxSearchValue.config(to=int(intVarSpinboxDataSize.get()))

    # Simulation 프로그램
    def buttonStopFunc():
        pass

    def buttonReplayFunc():
        global searchValue
        global data

        canvas.delete(ALL)
        data = []

        labelState[1].config(text=LABEL_STATE[1])
        labelElapsedTime[1].config(text=ELAPSED_TIME[1])
        labelHint[4].configure(text=LABEL_HINT[4])
        buttonStart.config(state="disabled")
        buttonEnd[1].config(state="disabled")
        buttonEnd[2].config(state="disabled")

        if remindSearchValue == 0:
            searchValue = random.randint(1, dataSize)
        
        createSticks()

        startSimulationThread()

    def buttonEndFunc():
        global data

        canvas.delete(ALL)
        data = []

        frameSimulation.pack_forget()

        labelState[1].config(text=LABEL_STATE[1])
        labelElapsedTime[1].config(text=ELAPSED_TIME[1])
        labelHint[4].configure(text=LABEL_HINT[4])
        buttonEnd[1].config(state="disabled")
        buttonEnd[2].config(state="disabled")

## ====================== 타이머 함수 ====================== ##
    def timerFunc():
        if timerRunning:
            global timerStartTime
            timerNowTime = int((time.time() - timerStartTime) * 1000)
            labelElapsedTime[1].config(text=str(timerNowTime // 60000).zfill(2) + ":" + str((timerNowTime % 60000) // 1000).zfill(2) + "." + str(timerNowTime % 1000).zfill(3))
        window.after(1, timerFunc)


## ====================== buttonStart 클릭 이후 함수들 ====================== ##

    # canvas의 data[데이터 값, 막대 그래프] 리스트 생성 및 순서에 따라 재배치
    def createSticks():
        for i in range(dataSize - 1, -1, -1):
            data.append([i + 1, canvas.create_rectangle(0, 0, CANVAS_WIDTH / dataSize, CANVAS_HEIGHT * (i + 1) / dataSize, fill=WHITE)])
        data.reverse()

        for i in data:
            canvas.moveto(i[1], CANVAS_WIDTH * data.index(i) / dataSize + 1, CANVAS_HEIGHT - CANVAS_HEIGHT * i[0] / dataSize + 1)

    # canvas의 data[데이터 값, 막대 그래프] 리스트 순서에 따라 재배치
    def relocationStick():
        for i in data:
            canvas.moveto(i[1], CANVAS_WIDTH * data.index(i) / dataSize + 1, CANVAS_HEIGHT - CANVAS_HEIGHT * i[0] / dataSize + 1)

    # 막대 하나를 자신의 자리에 배치
    def relocationOneStick(index):
        canvas.moveto(data[index][1], CANVAS_WIDTH * index / dataSize + 1, CANVAS_HEIGHT - CANVAS_HEIGHT * data[index][0] / dataSize + 1)

    # 시작 버튼 클릭 시 시뮬레이션 하는 쓰레드 생성
    def startSimulationThread():
        thread = threading.Thread(target=startSimulation)
        thread.daemon = True
        thread.start()

    # 시뮬레이션 메인 함수
    def startSimulation():
        global timerRunning
        global timerStartTime
        global searchValue

        buttonEnd[0].config(state="normal")

        if sortOrSearchAlgorithm == 0: # 정렬 알고리즘
            labelState[1].config(text=LABEL_STATE[2])
            if shuffleVisible:
                shuffleStick()
            else:
                shuffleStickNotVisible()
                relocationStick()
            labelState[1].config(text=LABEL_STATE[5])
            time.sleep(1)
            labelState[1].config(text=LABEL_STATE[3])
            timerStartTime = time.time()
            timerRunning = True

            if algorithm == SORT_ALGORITHMS[0]:
                bubbleSort()
            elif algorithm == SORT_ALGORITHMS[1]:
                selectSort()
            elif algorithm == SORT_ALGORITHMS[2]:
                insertSort()
            elif algorithm == SORT_ALGORITHMS[3]:
                mergeSort()
            elif algorithm == SORT_ALGORITHMS[4]:
                quickSort()
            elif algorithm == SORT_ALGORITHMS[5]:
                heapSort()
            else:
                pass

            timerRunning = False
            labelState[1].config(text=LABEL_STATE[6])
        else: # 탐색 알고리즘
            if searchValue == 0:
                searchValue = random.randint(1, dataSize)
            labelHint[4].configure(text=str(searchValue))
            labelState[1].config(text=LABEL_STATE[4])
            timerStartTime = time.time()
            timerRunning = True

            if algorithm == SEARCH_ALGORITHMS[0]:
                linearSearch()
            elif algorithm == SEARCH_ALGORITHMS[1]:
                binarySearch()
            else:
                pass

            timerRunning = False
            labelState[1].config(text=LABEL_STATE[7])

        buttonStart.config(state="normal")
        spinboxSearchValue.config(state="normal")
        buttonEnd[1].config(state="normal")
        buttonEnd[2].config(state="normal")
        buttonEnd[0].config(state="disable")


    # 두 막대 교환 함수
    def exchangePairStick(attentionStickIndex, compareStickIndex, attentionStickColor = RED, compareStickColor = BLUE):
        canvas.itemconfig(data[attentionStickIndex][1], fill=attentionStickColor)
        canvas.itemconfig(data[compareStickIndex][1], fill=compareStickColor)

        if speedLimit != 0:
            time.sleep(speedLimit)
        data[attentionStickIndex], data[compareStickIndex] = data[compareStickIndex], data[attentionStickIndex]
        canvas.moveto(data[attentionStickIndex][1], CANVAS_WIDTH * attentionStickIndex / dataSize + 1, CANVAS_HEIGHT - CANVAS_HEIGHT * data[attentionStickIndex][0] / dataSize + 1)
        canvas.moveto(data[compareStickIndex][1], CANVAS_WIDTH * compareStickIndex / dataSize + 1, CANVAS_HEIGHT - CANVAS_HEIGHT * data[compareStickIndex][0] / dataSize + 1)

        if speedLimit != 0:
            time.sleep(speedLimit)
        canvas.itemconfig(data[attentionStickIndex][1], fill=WHITE)
        canvas.itemconfig(data[compareStickIndex][1], fill=WHITE)

    # 두 막대를 교환하지 않고 색상만 표현하는 함수
    def notExchangePairStick(attentionStickIndex, compareStickIndex, attentionStickColor = RED, compareStickColor = BLUE):
        canvas.itemconfig(data[attentionStickIndex][1], fill=attentionStickColor)
        canvas.itemconfig(data[compareStickIndex][1], fill=compareStickColor)

        if speedLimit != 0:
            time.sleep(speedLimit)
        canvas.itemconfig(data[attentionStickIndex][1], fill=WHITE)
        canvas.itemconfig(data[compareStickIndex][1], fill=WHITE)

    # 막대 색상 변경 (딜레이 없음)
    def changeColor(stickIndex, color):
        canvas.itemconfig(data[stickIndex][1], fill=color)

    # 막대 색상 변경 (딜레이 있음)
    def changeColorDelay(stickIndex, color):
        canvas.itemconfig(data[stickIndex][1], fill=color)

        if speedLimit != 0:
            time.sleep(speedLimit)

    # 정렬 선택 시 막대 섞기 함수
    def shuffleStick():
        global speedLimit
    
        drawTwoStick = []
        tempSpeedLimitMemory = speedLimit
        speedLimit = 0.0

        for i in range(shuffleTime):
            drawTwoStick = random.sample(data, 2)
            exchangePairStick(drawTwoStick[0][0] - 1, drawTwoStick[1][0] - 1, RED, RED)

        speedLimit = tempSpeedLimitMemory

    # 정렬 선택 시 막대 섞기 함수
    def shuffleStickNotVisible():
        global speedLimit
    
        drawTwoStick = []
        tempSpeedLimitMemory = speedLimit
        speedLimit = 0.0

        for i in range(shuffleTime):
            drawTwoStick = random.sample(data, 2)
            data[drawTwoStick[0][0] - 1], data[drawTwoStick[1][0] - 1] = data[drawTwoStick[1][0] - 1], data[drawTwoStick[0][0] - 1]

        speedLimit = tempSpeedLimitMemory

## ====================== 정렬 알고리즘 ====================== ##
    # 버블 정렬
    def bubbleSort():
        for i in range(dataSize):
            for y in range(dataSize - 1, i, -1):
                if data[y][0] < data[y - 1][0]:
                    exchangePairStick(y, y - 1)
                elif speedLimit != 0:
                    notExchangePairStick(y, y - 1)
                else:
                    continue

            changeColor(i, YELLOW)

    # 선택 정렬
    def selectSort():
        minimumIndex = 0
        minimumValue = data[0][0]

        for i in range(dataSize):
            minimumIndex = i
            minimumValue = data[i][0]
            for y in range(i + 1, dataSize):
                notExchangePairStick(minimumIndex, y)
                if minimumValue > data[y][0]:
                    minimumIndex = y
                    minimumValue = data[y][0]
            exchangePairStick(i, minimumIndex, RED, RED)
            changeColor(i, YELLOW)

    # 삽입 정렬
    def insertSort():
        for i in range(1, dataSize):
            for y in range(i, 0, -1):
                if data[y][0] < data[y - 1][0]:
                    exchangePairStick(y, y - 1)
                    changeColor(y, YELLOW)
                    changeColor(y - 1, YELLOW)
                else:
                    notExchangePairStick(y, y - 1)
                    changeColor(y, YELLOW)
                    changeColor(y - 1, YELLOW)
                    break

    #병합 정렬
    def mergeSort():
        mergeSortInplace(data)

    def mergeSortInplace(arr):
        n = len(arr)
        step = 1
        while step < n:
            left = 0
            while left + step < n:
                mid = left + step
                right = min(left + 2 * step, n)
                merge(arr, left, mid, right)
                left += 2 * step
            step *= 2

    def merge(arr, left, mid, right):
        temp = []
        for i in range(left, right):
            changeColor(i, BLUE)
        i, j = left, mid
        while i < mid and j < right:
            if arr[i][0] <= arr[j][0]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i < mid:
            temp.append(arr[i])
            i += 1
        while j < right:
            temp.append(arr[j])
            j += 1
        for i in range(left, right):
            arr[i] = temp[i - left]
            changeColorDelay(i, RED)
            relocationOneStick(i)
            changeColor(i, YELLOW)
        if right - left < dataSize - 1:
            for i in range(left, right):
                changeColor(i, WHITE)

    #퀵 정렬
    def quickSort():
        quickSortRecursive(data, 0, dataSize - 1)

    def quickSortRecursive(array, start, end):
        if start == end :
            changeColorDelay(start, RED)
            changeColor(start, YELLOW)
            return
        elif start >= end :
            return
        pivot = start
        left = start
        right = end

        changeColor(pivot, RED)
        
        while left <= right:
            while left <= end and array[left] <= array[pivot]:
                left += 1
            while right > start and array[right] >= array[pivot]:
                right -= 1
            if left > right:
                exchangePairStick(pivot, right)
                changeColor(right, YELLOW)
            else:
                exchangePairStick(right, left, BLUE)
        
        
        quickSortRecursive(array, start, right - 1)
        quickSortRecursive(array, right + 1, end)

    # 힙 정렬
    def heapSort():
        heap_sort(data)

    def heap_sort(arr):
        n = len(arr)
        
        labelState[1].config(text=LABEL_STATE[8])

        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        
        labelState[1].config(text=LABEL_STATE[3])

        for i in range(n - 1, 0, -1):
            exchangePairStick(0, i)
            changeColor(i, YELLOW)
            heapify(arr, i, 0)
        
        changeColor(0, YELLOW)


    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left][0] > arr[largest][0]:
            largest = left
        
        if right < n and arr[right][0] > arr[largest][0]:
            largest = right
        
        if largest != i:
            exchangePairStick(i, largest)
            heapify(arr, n, largest)


## ====================== 탐색 알고리즘 ====================== ##
    def linearSearch():
        for i in data:
            changeColorDelay(i[0] - 1, RED)
            if i[0] == searchValue:
                changeColor(i[0] - 1, YELLOW)
                break
            else:
                changeColor(i[0] - 1, WHITE)

    def binarySearch():
        center = 0
        left = 0
        right = dataSize - 1

        while True:
            center = left + (right - left) // 2
            changeColor(left, BLUE)
            changeColor(right, BLUE)
            changeColorDelay(center, RED)
            if data[center][0] == searchValue:
                break
            elif data[center][0] > searchValue:
                changeColor(right, WHITE)
                right = center - 1
            else:
                changeColor(left, WHITE)
                left = center + 1
            changeColor(center, WHITE)
        changeColor(center, YELLOW)


## ====================== 배치 ====================== ##

    # 프레임 패킹
    frameGeneralMenu.pack(side=TOP)
    frameAdvancedMenu.pack_forget()
    frameSimulation.pack_forget()

    # General Menu 패킹
    radioButtonSelectAlgorithm[0].pack(side=LEFT)
    radioButtonSelectAlgorithm[1].pack(side=LEFT)
    comboboxSelectAlgorithm.pack(side=LEFT, padx=(10, 0))
    checkbuttonAdvancedMenu.pack(side=LEFT, padx=(10, 0))
    buttonStart.pack(side=LEFT, padx=5, pady=5, ipadx=15, ipady=3)

    # Advanced Menu 패킹
    labelDataSize.pack(side=LEFT)
    spinboxDataSize.pack(side=LEFT, padx=(2, 0))
    labelSpeedLimit.pack(side=LEFT, padx=(10, 0))
    spinboxSpeedLimit.pack(side=LEFT, padx=(2, 0))
    labelShuffleTimes.pack(side=LEFT, padx=(10, 0))
    spinboxShuffleTimes.pack(side=LEFT, padx=(2, 0))
    checkbuttonShuffleVisible.pack(side=LEFT, padx=(10, 0))
    labelSearchValue.pack_forget()
    spinboxSearchValue.pack_forget()

    # Simulation 패킹
    canvas.pack()

    frameSimulationHint.pack(side=TOP)
    frameSimulationState.pack(side=TOP)
    frameSimulationElapsedTime.pack(side=TOP)
    frameSimulationEndButtons.pack(side=TOP)

    labelHint[0].pack(side=LEFT)
    labelHint[1].pack(side=LEFT)
    labelHint[2].pack(side=LEFT)
    labelHint[3].pack(side=LEFT)
    labelHint[4].pack(side=LEFT)

    labelState[0].pack(side=LEFT)
    labelState[1].pack(side=LEFT)

    labelElapsedTime[0].pack(side=LEFT)
    labelElapsedTime[1].pack(side=LEFT)

    buttonEnd[0].pack(side=LEFT, padx=5, pady=5, ipadx=15, ipady=3)
    buttonEnd[1].pack(side=LEFT, padx=5, pady=5, ipadx=15, ipady=3)
    buttonEnd[2].pack(side=LEFT, padx=5, pady=5, ipadx=15, ipady=3)

    timerFunc()
    window.mainloop()

## 전역 변수 ##
timerRunning = False
timerStartTime = time.time()

sortOrSearchAlgorithm = 0
algorithm = ""
dataSize = 0
speedLimit = 0.0
shuffleTime = 0
shuffleVisible = False
searchValue = 0
remindSearchValue = 0

data = []

if __name__=="__main__":
    main()